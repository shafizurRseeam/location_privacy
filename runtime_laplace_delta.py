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
def planar_laplace_mechanism_point(location, noise_laplace):
    latitude, longitude = location
    y, x = lat_lon_to_y_x(latitude, longitude)
    noise_x, noise_y = random.choice(noise_laplace)
    Perturbed_X = x + noise_x
    Perturbed_Y = y + noise_y
    Perturbed_Latitude, Perturbed_Longitude = y_x_to_lat_lon(Perturbed_Y, Perturbed_X)
    
    return Perturbed_Latitude, Perturbed_Longitude

def planar_laplace_mechanism_delta(dataset, noise_laplace, delta):

    dataset['perturbed_latitude'] = np.nan
    dataset['perturbed_longitude'] = np.nan
    true_location      = (dataset.at[0, 'latitude'], dataset.at[0, 'longitude'])            
    Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)
    dataset.at[0, 'perturbed_latitude']  =  Perturbed_Location[0]
    dataset.at[0, 'perturbed_longitude'] =  Perturbed_Location[1]
    distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
             
    current_focus = true_location
    current_reported = Perturbed_Location

    for i in range(1, len(dataset)):

        true_location = (dataset.at[i, 'latitude'], dataset.at[i, 'longitude'])
        distance_from_focus = haversine(true_location, current_focus, unit = Unit.METERS)

        if distance_from_focus < delta:
      
            dataset.at[i, 'perturbed_latitude'] = current_reported[0]
            dataset.at[i, 'perturbed_longitude'] = current_reported[1]
                
            distance = haversine(true_location, (dataset.at[i, 'perturbed_latitude'], dataset.at[i, 'perturbed_longitude']), unit = Unit.METERS)

        else:

            Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)
            
            dataset.at[i, 'perturbed_latitude']  =  Perturbed_Location[0]
            dataset.at[i, 'perturbed_longitude'] =  Perturbed_Location[1]

            distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
           
            current_reported = (dataset.at[i,'perturbed_latitude'], dataset.at[i,'perturbed_longitude'])
            current_focus    = (  dataset.at[i,'latitude'], dataset.at[i,'longitude'])

    return dataset

def apply_perturbation_and_measure_time(df, noise_samples_laplace, runs, delta):
    start_time = time.time()
    for _ in range(runs):
        perturbed_df = planar_laplace_mechanism_delta(df.copy(), noise_samples_laplace, delta)
    end_time = time.time()
    total_time = end_time - start_time
    points_count = len(df) * runs
    return total_time, points_count

def process_files_in_directory(directory_path, noise_samples_laplace, runs, delta):
    total_time = 0
    total_points = 0
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            time_taken, points_count = apply_perturbation_and_measure_time(df, noise_samples_laplace, runs, delta)
            total_time += time_taken
            total_points += points_count
    if total_points > 0:
        average_time_per_point = total_time / total_points
        print(f"Total time: {total_time:.4f} seconds, Average time per point across all runs: {average_time_per_point:.8f} seconds")
    else:
        print("No data points found in the directory.")


def main():
    parser = argparse.ArgumentParser(description="Geoprivacy Perturbation Script")
    parser.add_argument("directory", type=str, help="Directory path to process CSV files")
    parser.add_argument("--epsilon", type=float, default=1, help="Epsilon value for Laplace noise")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs for timing measurement")
    parser.add_argument("--delta", type=int, default=5, help="distance")

    args = parser.parse_args()

    directory_path = args.directory
    noise_samples_laplace = generate_laplace_noise_samples(10, args.epsilon)
    print(f"Processing CSV files in directory: {directory_path}")
    process_files_in_directory(directory_path, noise_samples_laplace, args.runs, args.delta)

if __name__ == "__main__":
    main()


#python main_runtime.py C:\Path\To\Your\Directory --epsilon 1.5 --runs 5
