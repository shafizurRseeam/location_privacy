import os
import sys
import pandas as pd

def add_identifier_to_csv(source_directory):
    # Counter for file identifier
    file_identifier = 1

    # Iterate over each file in the source directory
    for file in os.listdir(source_directory):
        # Check if the file is a CSV
        if file.endswith('.csv'):
            file_path = os.path.join(source_directory, file)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Add a new column with the identifier
            df['identifier'] = file_identifier

            # Save the modified DataFrame back to CSV
            df.to_csv(file_path, index=False)

            # Increment the file identifier for the next file
            file_identifier += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_identifier.py <source_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    add_identifier_to_csv(source_directory)
    print('Processing complete.')

#python add_identifier.py /path/to/source_directory