import os
import sys
import glob
import pandas as pd
import numpy as np

def encode_locations(df, num_lat_bins, num_lon_bins):
    lat_min, lat_max = df['latitude'].min(), df['latitude'].max()
    lon_min, lon_max = df['longitude'].min(), df['longitude'].max()

    lat_bins = np.linspace(lat_min, lat_max, num_lat_bins + 1)
    lon_bins = np.linspace(lon_min, lon_max, num_lon_bins + 1)

    df['lat_bin'] = pd.cut(df['latitude'], bins=lat_bins, labels=False, include_lowest=True)
    df['lon_bin'] = pd.cut(df['longitude'], bins=lon_bins, labels=False, include_lowest=True)
    
    lat_midpoints = (lat_bins[:-1] + lat_bins[1:]) / 2
    lon_midpoints = (lon_bins[:-1] + lon_bins[1:]) / 2

    df['mid_latitude'] = df['lat_bin'].map(lambda x: lat_midpoints[x])
    df['mid_longitude'] = df['lon_bin'].map(lambda x: lon_midpoints[x])
    
    df['location_id'] = df['lat_bin'] * num_lon_bins + df['lon_bin'] + 1

    avg_coordinates = df.groupby('location_id').agg({'latitude': 'mean', 'longitude': 'mean'}).rename(columns={'latitude': 'avg_latitude', 'longitude': 'avg_longitude'})
    df = df.merge(avg_coordinates, on='location_id', how='left')

    return df

def process_files(input_directory, base_output_directory, bin_sizes):
    for bins in bin_sizes:
        num_lat_bins = bins
        num_lon_bins = bins
        output_directory = os.path.join(base_output_directory, str(bins))

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for csv_file in glob.glob(os.path.join(input_directory, '*.csv')):
            df = pd.read_csv(csv_file)
            encoded_df = encode_locations(df.copy(), num_lat_bins, num_lon_bins)
            base_filename = os.path.splitext(os.path.basename(csv_file))[0]
            new_filename = f"{base_filename}_encoded.csv"
            output_path = os.path.join(output_directory, new_filename)
            encoded_df.to_csv(output_path, index=False)

        print(f"Encoding complete for bin size {bins}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encode_locations_grid.py <input_directory> <base_output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    base_output_directory = sys.argv[2]
    bin_sizes = [100, 200, 400, 800, 1000]

    process_files(input_directory, base_output_directory, bin_sizes)

    
#python encode_locations_grid.py "C:\Users\ss6365\Desktop\11111\Geolife\Machine_Learning\Laplace\2km" "C:\Users\ss6365\Desktop\11111\Geolife\Machine_Learning\Laplace\encoded\2km"
