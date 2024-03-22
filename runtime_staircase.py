import argparse
import math
import os
import pandas as pd
import numpy as np
import random
import time
from haversine import haversine, inverse_haversine, Unit

EARTH_RADIUS = 6371000

def lat_lon_to_y_x(lat, lon):
    x = EARTH_RADIUS * np.radians(lon)
    y = EARTH_RADIUS * np.radians(lat)
    return y, x

def y_x_to_lat_lon(y, x):
    lon = np.degrees(x / EARTH_RADIUS)
    lat = np.degrees(y / EARTH_RADIUS)
    return lat, lon

def pdf_values(epsilon, x_interval, L):
    b = (1 - np.exp(-epsilon)) / x_interval
    intervals = int(L / x_interval)
    positions = np.linspace(0, L - x_interval, intervals)
    unnormalized_pdf_samples = b * np.exp(-epsilon * positions)
    
    # Normalize
    area = np.sum(unnormalized_pdf_samples) * x_interval
    normalized_pdf_samples = unnormalized_pdf_samples / area
    return positions, normalized_pdf_samples

def draw_from_pdf(epsilon, x_interval, L):
    positions, normalized_pdf_samples = pdf_values(epsilon, x_interval, L)
    
    # Compute the cumulative distribution
    cdf = np.cumsum(normalized_pdf_samples)
    cdf /= cdf[-1]
    
    # Draw a random number between 0 and 1
    r = np.random.rand()
    
    # Find the index where the random number fits into the CDF
    index = np.searchsorted(cdf, r)
    
    # Get radial distance from the selected interval
    start_of_interval = positions[index]
    end_of_interval = start_of_interval + x_interval
    random_r_value = np.random.uniform(start_of_interval, end_of_interval)
    
    # Generate the random theta value
    theta = np.random.uniform(0, 2 * np.pi)
    
    # Convert r and theta to x and y
    x = random_r_value * np.cos(theta)
    y = random_r_value * np.sin(theta)
    
    return x, y

def generate_psm_noise_samples(epsilon, x_interval, L, n_samples):
    samples = []
    for _ in range(n_samples):
        x, y = draw_from_pdf(epsilon, x_interval, L)
        samples.append((x, y))
    return samples

def PSM_optimized(Data, noise_samples_staircase):
    Data['Perturbed_Latitude_S'] = np.nan
    Data['Perturbed_Longitude_S'] = np.nan
    
    for i in range(len(Data)):
        Latitude = Data.at[i, 'Latitude']
        Longitude = Data.at[i, 'Longitude']
        
        y, x = lat_lon_to_y_x(Latitude, Longitude)
        
        Noise_X, Noise_Y = random.choice(noise_samples_staircase)
        
        Perturbed_X = x + Noise_X
        Perturbed_Y = y + Noise_Y
        
        Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
        
        Data.at[i, 'Perturbed_Latitude_S'] = Perturbed_Latitude
        Data.at[i, 'Perturbed_Longitude_S'] = Perturbed_Longitude
    
    return Data

def apply_perturbation_and_measure_time(df, noise_samples_staircase, runs):
    start_time = time.time()
    for _ in range(runs):
        perturbed_df = PSM_optimized(df.copy(), noise_samples_staircase)
    end_time = time.time()
    total_time = end_time - start_time
    total_points = len(df) * runs
    return total_time, total_points


def process_files_in_directory(directory_path, noise_samples_staircase, runs):
    total_time = 0
    total_points = 0
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            time_taken, points_count = apply_perturbation_and_measure_time(df, noise_samples_staircase, runs)
            total_time += time_taken  # Correctly add only the time to the total_time
            total_points += points_count  # Add points count to total_points
    if total_points > 0:
        average_time_per_point = total_time / total_points
        print(f"Total time: {total_time:.4f} seconds, Average time per point across all runs: {average_time_per_point:.8f} seconds")
    else:
        print("No data points found in the directory.")


def main():
    parser = argparse.ArgumentParser(description="Geoprivacy Perturbation Script with Staircase Mechanism")
    parser.add_argument("directory", type=str, help="Directory path to process CSV files")
    parser.add_argument("--epsilon", type=float, default=1.0, help="Epsilon value for noise generation")
    parser.add_argument("--x_interval", type=float, default=0.1, help="X interval for PDF calculation")
    parser.add_argument("--L", type=float, default=10, help="Maximum range for noise generation")
    parser.add_argument("--n_samples", type=int, default=10, help="Number of noise samples to generate")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs for timing measurement")
    args = parser.parse_args()

    # Generate noise samples based on the Staircase (PSM) mechanism
    noise_samples_staircase = generate_psm_noise_samples(args.epsilon, args.x_interval, args.L, args.n_samples)
    
    print(f"Processing CSV files in directory: {args.directory}")
    process_files_in_directory(args.directory, noise_samples_staircase, args.runs)

if __name__ == "__main__":
    main()

