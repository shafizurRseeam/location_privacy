import argparse
import math
import os
import pandas as pd
import numpy as np
import random
import scipy.special
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

def random_laplace_noise(epsilon):
    theta = np.random.uniform(0, 2 * math.pi)
    p = random.random()
    r = -1 / epsilon * (scipy.special.lambertw((p - 1) / math.e, k=-1, tol=1e-8).real + 1)
    x, y = r * math.cos(theta), r * math.sin(theta)
    return x, y

def generate_laplace_noise_samples(n_samples, epsilon):
    samples = []
    for _ in range(n_samples):
        samples.append(random_laplace_noise(epsilon))
    return samples

def PLM_optimized(Data, noise_samples_laplace):
    Data['Perturbed_Latitude_G'] = np.nan
    Data['Perturbed_Longitude_G'] = np.nan

    for i in range(len(Data)):
        Latitude = Data.at[i, 'latitude']
        Longitude = Data.at[i, 'longitude']
        y, x = lat_lon_to_y_x(Latitude, Longitude)
        Noise_X, Noise_Y = random.choice(noise_samples_laplace)
        Perturbed_X = x + Noise_X
        Perturbed_Y = y + Noise_Y
        Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
        Data.at[i, 'Perturbed_Latitude_G'] = Perturbed_Latitude
        Data.at[i, 'Perturbed_Longitude_G'] = Perturbed_Longitude
    return Data

def apply_perturbation_and_measure_time(df, noise_samples_laplace, runs):
    start_time = time.time()
    for _ in range(runs):
        perturbed_df = PLM_optimized(df.copy(), noise_samples_laplace)
    end_time = time.time()
    total_time = end_time - start_time
    points_count = len(df) * runs
    return total_time, points_count

def process_files_in_directory(directory_path, noise_samples_laplace, runs):
    total_time = 0
    total_points = 0
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            time_taken, points_count = apply_perturbation_and_measure_time(df, noise_samples_laplace, runs)
            total_time += time_taken
            total_points += points_count
    if total_points > 0:
        average_time_per_point = total_time / total_points
        print(f"Processed directory: {directory_path}\nTotal time: {total_time:.4f} seconds, Average time per point across all runs: {average_time_per_point:.8f} seconds")
    else:
        print(f"No data points found in the directory: {directory_path}.")

def main():
    parser = argparse.ArgumentParser(description="Geoprivacy Perturbation Script")
    parser.add_argument("base_directory", type=str, help="Base directory path to process CSV files in subdirectories")
    parser.add_argument("--epsilon", type=float, default=1, help="Epsilon value for Laplace noise")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs for timing measurement")
    args = parser.parse_args()

    directories = ['uci', 'collected', 'geolife', 'tdrive']
    for dir in directories:
        directory_path = os.path.join(args.base_directory, dir)
        print(f"Processing CSV files in directory: {directory_path}")
        noise_samples_laplace = generate_laplace_noise_samples(10, args.epsilon)
        process_files_in_directory(directory_path, noise_samples_laplace, args.runs)

if __name__ == "__main__":
    main()
