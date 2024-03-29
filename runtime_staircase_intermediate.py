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

# Constants and utility functions as previously defined...
def get_direction(loc1, loc2):
    dLon = (loc2[1] - loc1[1])
    y = math.sin(math.radians(dLon)) * math.cos(math.radians(loc2[0]))
    x = math.cos(math.radians(loc1[0])) * math.sin(math.radians(loc2[0])) - math.sin(math.radians(loc1[0])) * math.cos(math.radians(loc2[0])) * math.cos(math.radians(dLon))
    brng = math.atan2(y, x)
    return brng

def lat_lon_to_y_x(lat, lon):
    # Convert latitude and longitude to x and y coordinates using Equirectangular Projection.
    x = EARTH_RADIUS * np.radians(lon)
    y = EARTH_RADIUS * np.radians(lat)
    return y, x

def y_x_to_lat_lon(y, x):
    # Convert x and y coordinates to latitude and longitude using inverse Equirectangular Projection.
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
        Latitude = Data.at[i, 'latitude']
        Longitude = Data.at[i, 'longitude']
        
        y, x = lat_lon_to_y_x(Latitude, Longitude)
        
        Noise_X, Noise_Y = random.choice(noise_samples_staircase)
        
        Perturbed_X = x + Noise_X
        Perturbed_Y = y + Noise_Y
        
        Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
        
        Data.at[i, 'Perturbed_Latitude_S'] = Perturbed_Latitude
        Data.at[i, 'Perturbed_Longitude_S'] = Perturbed_Longitude
    
    return Data

def SLLPM(Location, noise_samples_staircase):
    
    Latitude, Longitude = Location
    
    y, x = lat_lon_to_y_x(Latitude, Longitude)
    

    
    Noise_X, Noise_Y = random.choice(noise_samples_staircase)
    
    Perturbed_X = x + Noise_X
    Perturbed_Y = y + Noise_Y
    Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
    
    return Perturbed_Latitude, Perturbed_Longitude
def BSLLPM(Location, noise_samples_staircase):
    
    Latitude, Longitude = Location
    
    y, x = lat_lon_to_y_x(Latitude, Longitude)
    

    
    Noise_X, Noise_Y = random.choice(noise_samples_staircase)
    
    Perturbed_X = x + Noise_X
    Perturbed_Y = y + Noise_Y
    
    Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
    
    return Perturbed_Latitude, Perturbed_Longitude
def intermediate(dataset, noise_samples_staircase):
    
    dataset = dataset.copy()  # Make a copy to avoid modifying the original DataFrame
    num_locations = len(dataset['latitude'])

    # Initialize intermediate and final reported locations
    dataset['intermediate_lat'] = np.nan
    dataset['intermediate_lon'] = np.nan

    
    # Handle the first location separately
    true_location = (dataset['latitude'][0], dataset['longitude'][0])
    intermediate_location = BSLLPM(true_location, noise_samples_staircase)
    
    distance_first = haversine(true_location, intermediate_location, unit=Unit.METERS)


    dataset.at[0, 'intermediate_lat'] = intermediate_location[0]
    dataset.at[0, 'intermediate_lon'] = intermediate_location[1]
    #dataset.at[0, 'distance_first'] = distance_first

    
    # Handle subsequent locations
    for i in range(1, num_locations):
        true_location = (dataset.at[i, 'latitude'], dataset.at[i, 'longitude'])
        last_true = (dataset.at[i-1, 'latitude'], dataset.at[i-1, 'longitude'])
        distance = haversine(true_location, last_true, unit=Unit.METERS)
        direction = get_direction(last_true, true_location)
        
        intermediate_location = inverse_haversine(
            (dataset.at[i-1, 'intermediate_lat'], dataset.at[i-1, 'intermediate_lon']),
            distance,
            direction,
            Unit.METERS
        )
        
        dataset.at[i, 'intermediate_lat'] = intermediate_location[0]
        dataset.at[i, 'intermediate_lon'] = intermediate_location[1]
        
        

    return dataset

# Update your existing intermediate function to include the generation of reported locations

def only_reported_locations(dataset, noise_samples_staircase,delta):
    
    #dataset = intermediate(dataset, epsilon, x_interval, bl)  # Assume this generates intermediate locations y1, y2, ..., yn
    
    # Initialize the reported locations column
    dataset['reported_lat'] = np.nan
    dataset['reported_lon'] = np.nan
    
    # Handle the first location separately
#     dataset.at[0, 'reported_lat'], dataset.at[0, 'reported_lon'] = SSLLPM(
#         (dataset.at[0, 'intermediate_lat'], dataset.at[0, 'intermediate_lon'])
#     )
    
    
    dataset.at[0, 'reported_lat'], dataset.at[0, 'reported_lon'] = SLLPM(
        (dataset.at[0, 'intermediate_lat'], dataset.at[0, 'intermediate_lon']), noise_samples_staircase)
    
    
    
    
    # Store the current focus point (start with the first point)
    current_focus = (dataset.at[0, 'latitude'], dataset.at[0, 'longitude'])
    current_reported = (dataset.at[0, 'reported_lat'], dataset.at[0, 'reported_lon'])
    
    # Iterate over the remaining locations
    for i in range(1, len(dataset)):
        
        true_location = (dataset.at[i, 'latitude'], dataset.at[i, 'longitude'])
        distance_from_focus = haversine(true_location, current_focus, unit=Unit.METERS)
        
        if distance_from_focus < delta:
            # If the distance is below the threshold, report the same location as the current reported location
            dataset.at[i, 'reported_lat'] = current_reported[0]
            dataset.at[i, 'reported_lon'] = current_reported[1]
        
        else:
            # If the distance is above the threshold, perturb the intermediate location to get the reported location
            dataset.at[i, 'reported_lat'], dataset.at[i, 'reported_lon'] = SLLPM(
                (dataset.at[i, 'intermediate_lat'], dataset.at[i, 'intermediate_lon']), noise_samples_staircase
            )
            
            # Update the current focus and reported locations
            current_focus = true_location
            current_reported = (dataset.at[i, 'reported_lat'], dataset.at[i, 'reported_lon'])
    
    return dataset

def process_file(data, noise_samples_staircase,delta):
    
    
    
    
    intermediate_dataset = intermediate(data, noise_samples_staircase)

    
    Perturbed_Our = only_reported_locations(intermediate_dataset, noise_samples_staircase, delta)
    
    return Perturbed_Our

def apply_perturbation_and_measure_time(df, noise_samples_staircase, runs, delta):
    points_count = len(df)
    start_time = time.time()
    for _ in range(runs):
        perturbed_df = process_file(df.copy(), noise_samples_staircase, delta)
    end_time = time.time()
    total_time = (end_time - start_time) / runs
    return total_time, points_count

def process_directory(directory_path, noise_samples_staircase, runs, delta):
    total_time = 0
    total_points = 0
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            time_taken, points_count = apply_perturbation_and_measure_time(df, noise_samples_staircase, runs, delta)
            total_time += time_taken
            total_points += points_count
    if total_points > 0:
        average_time_per_point = total_time / total_points
        print(f"Total time: {total_time:.4f} seconds, Average time per point across all runs: {average_time_per_point:.8f} seconds")
    else:
        print("No data points found in the directory.")

def main():
    parser = argparse.ArgumentParser(description="Location Privacy Perturbation with Staircase Mechanism")
    parser.add_argument("base_directory", type=str, help="Base directory path to process CSV files in subdirectories")
    parser.add_argument("--epsilon", type=float, default=1.0, help="Epsilon value for noise generation")
    parser.add_argument("--delta", type=float, default=5, help="Delta value for distance threshold in reported locations")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs for timing measurement")
    args = parser.parse_args()

    # Generate noise samples for the staircase mechanism
    noise_samples_staircase = generate_psm_noise_samples(args.epsilon, 0.1, 10000, 10000)  # Adjust parameters as needed
    
    subdirectories = ['uci', 'collected', 'geolife', 'tdrive']  # Example subdirectories, adjust as needed or dynamically list directories in the base directory

    for subdir in subdirectories:
        directory_path = os.path.join(args.base_directory, subdir)
        print(f"Processing CSV files in directory: {directory_path}")
        process_directory(directory_path, noise_samples_staircase, args.runs, args.delta)

if __name__ == "__main__":
    main()