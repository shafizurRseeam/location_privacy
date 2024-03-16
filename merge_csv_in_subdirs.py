import os
import sys
import pandas as pd

def merge_csv_in_subdirectory(base_directory):
    # List of important columns to keep
    important_columns = ['Latitude', 'Longitude', 'Perturbed_Latitude', 'Perturbed_Longitude']

    # Check if the base directory exists
    if not os.path.isdir(base_directory):
        print(f"The directory {base_directory} does not exist.")
        sys.exit(1)

    # Extract the mechanism's name from the base directory path
    mechanism_name = os.path.basename(base_directory)

    # Process each subdirectory in the base directory
    for subdir in os.listdir(base_directory):
        subdir_path = os.path.join(base_directory, subdir)
        if os.path.isdir(subdir_path):
            # Initialize a list to store dataframes
            dataframes = []
            
            # Iterate through each CSV file in the subdirectory
            for filename in os.listdir(subdir_path):
                if filename.endswith('.csv'):
                    file_path = os.path.join(subdir_path, filename)
                    # Read the CSV file with only the important columns
                    df = pd.read_csv(file_path, usecols=important_columns)
                    dataframes.append(df)
            
            # Concatenate all dataframes if any were added
            if dataframes:
                merged_df = pd.concat(dataframes, ignore_index=True)
                # Define the output file path, including the mechanism's name in the file name
                output_file_path = os.path.join(base_directory, f"merged_{mechanism_name}_{subdir}.csv")
                # Save the merged dataframe to a new CSV file
                merged_df.to_csv(output_file_path, index=False)
                print(f"Merged CSV file for {subdir} saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_csv_in_subdirs.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    merge_csv_in_subdirectory(base_directory)

# python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy\geolife\test\Laplace"