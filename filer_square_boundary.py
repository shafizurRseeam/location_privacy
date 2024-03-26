import os
import sys
import glob
import pandas as pd
import numpy as np

def find_square_boundaries(lat, lon, distance_km):
    delta_lat = distance_km / 111  # 111 km per degree of latitude
    delta_lon = distance_km / (111 * np.cos(np.radians(lat)))  # Adjust for longitude
    return lat - delta_lat, lat + delta_lat, lon - delta_lon, lon + delta_lon

def process_directory(input_directory, output_directory, distance_km):
    for csv_file in glob.glob(os.path.join(input_directory, '*.csv')):
        df = pd.read_csv(csv_file)
        
        central_lat = df['latitude'].median()
        central_lon = df['longitude'].median()
        
        lat_min, lat_max, lon_min, lon_max = find_square_boundaries(central_lat, central_lon, distance_km)
        
        df_square = df[(df['latitude'] >= lat_min) & (df['latitude'] <= lat_max) &
                       (df['longitude'] >= lon_min) & (df['longitude'] <= lon_max)]
        
        base_filename = os.path.splitext(os.path.basename(csv_file))[0]
        new_filename = f"{base_filename}_{distance_km}km.csv"
        
        output_path = os.path.join(output_directory, new_filename)
        df_square.to_csv(output_path, index=False)

    print(f"Processing complete for directory: {input_directory}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python filter_square_boundaries.py <input_directory> <output_directory> <distance_km>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    distance_km = float(sys.argv[3])

    process_directory(input_directory, output_directory, distance_km)


#python filter_square_boundaries.py "C:/Users/ss6365/Desktop/11111/Geolife/Perturbed_Averaged/Laplace" "C:/Users/ss6365/Desktop/11111/Geolife/Machine_Learning/Laplace/2km" 2
