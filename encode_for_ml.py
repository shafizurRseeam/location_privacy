import os
import glob
import pandas as pd
import numpy as np
import sys  # Import the sys module

def encode_locations(df, num_lat_bins, num_lon_bins):
    """
    Encode latitude and longitude into a fixed-size grid and calculate the average
    latitude and longitude for each grid cell.
    """
    lat_min, lat_max = df['latitude'].min(), df['latitude'].max()
    lon_min, lon_max = df['longitude'].min(), df['longitude'].max()

    lat_bins = np.linspace(lat_min, lat_max, num_lat_bins + 1)
    lon_bins = np.linspace(lon_min, lon_max, num_lon_bins + 1)

    df['lat_bin'] = pd.cut(df['latitude'], bins=lat_bins, labels=False, include_lowest=True)
    df['lon_bin'] = pd.cut(df['longitude'], bins=lon_bins, labels=False, include_lowest=True)
    
    df['location_id'] = df['lat_bin'] * num_lon_bins + df['lon_bin'] + 1

    return df

def process_directory(input_directory, output_directory, bin_sizes):
    """
    Process all CSV files in a given directory for all specified bin sizes.
    """
    subdirectories = [ 'laplace', 'staircase', 'our_bl_50_delta_5', 'our_bl_50_delta_10', 'our_bl_50_delta_15', 'our_bl_50_delta_20','our_bl_20_delta_5', 'our_bl_200_delta_5', 'our_bl_500_delta_5']
#
    for subdirectory in subdirectories:
        full_path = os.path.join(input_directory, subdirectory)
        
        for bins in bin_sizes:
            specific_output_path = os.path.join(output_directory, subdirectory, str(bins))
            if not os.path.exists(specific_output_path):
                os.makedirs(specific_output_path)
            
            for csv_file in glob.glob(os.path.join(full_path, '*.csv')):
                df = pd.read_csv(csv_file)
                encoded_df = encode_locations(df.copy(), bins, bins)

                base_filename = os.path.splitext(os.path.basename(csv_file))[0]
                new_filename = f"{base_filename}_encoded_{str(bins)}.csv"
                output_path = os.path.join(specific_output_path, new_filename)
                
                encoded_df.to_csv(output_path, index=False)
            
            print(f"Encoding complete for {subdirectory} at bin size {bins}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encode.py <input_directory> <output_directory>")
    else:
        input_directory = sys.argv[1]
        output_directory = sys.argv[2]

        # List of bin sizes
        bin_sizes = [200]

        process_directory(input_directory, output_directory, bin_sizes)


#python encode_for_ml.py 'C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged' 'C:\Users\ss6365\Desktop\location_privacy_final\uci\machine_learning\attack1'