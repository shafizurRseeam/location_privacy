import os
import pandas as pd
import math
import sys  # Import sys to access command-line arguments

# Function to calculate the haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000.0  # Earth radius in meters
    phi1, phi2 = map(math.radians, [lat1, lat2])
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Function to calculate the L1 distance
def l1_distance(lat1, lon1, lat2, lon2):
    lat_distance = haversine(lat1, lon1, lat2, lon1)
    lon_distance = haversine(lat1, lon1, lat1, lon2)
    return lat_distance + lon_distance

def process_directory(base_directory_path):
    # Process each subdirectory in the base directory
    for subdir in os.listdir(base_directory_path):
        subdir_path = os.path.join(base_directory_path, subdir)
        if os.path.isdir(subdir_path):
            # Process each CSV file in the subdirectory
            for filename in os.listdir(subdir_path):
                if filename.endswith('.csv'):
                    file_path = os.path.join(subdir_path, filename)
                    
                    # Load the CSV file into a DataFrame
                    df = pd.read_csv(file_path)

                    # Calculate the L1 distance for each row and create a new column 'l1distance'
                    df['l1_distance'] = df.apply(lambda row: l1_distance(row['latitude'], row['longitude'], 
                                                                        row['perturbed_latitude'], row['perturbed_longitude']), axis=1)

                    # Calculate the L2 (Haversine) distance for each row and create a new column 'l2distance'
                    df['l2_distance'] = df.apply(lambda row: haversine(row['latitude'], row['longitude'], 
                                                                      row['perturbed_latitude'], row['perturbed_longitude']), axis=1)

                    # Save the DataFrame back to the same CSV file
                    df.to_csv(file_path, index=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python utility_metric.py base_directory")
    else:
        base_directory = sys.argv[1]
        process_directory(base_directory)
        print("L1 and L2 distance calculation and saving done for all CSV files in all subdirectories.")


#python utility_metrics.py '/Users/shafizurrahmanseeam/Desktop/ARR/AR_GPS_Sensor_Data/Perturbed_10/test'
        