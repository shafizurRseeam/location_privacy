import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

def split_and_save_csv(input_csv_path, train_output_dir, test_output_dir, test_size=0.2, random_state=42):
    # Extract the eps value from the input CSV file name
    file_name = os.path.splitext(os.path.basename(input_csv_path))[0]
    eps = file_name.split('_')[3]  # Adjust based on where eps is in your file name

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    df = df[['location_id', 'perturbed_latitude', 'perturbed_longitude']]

    # Perform the train-test split
    train_data, test_data = train_test_split(df, test_size=test_size, random_state=random_state)

    # Construct the output file paths
    train_csv_path = os.path.join(train_output_dir, f'{eps}.csv')
    test_csv_path = os.path.join(test_output_dir, f'{eps}.csv')

    # Save the DataFrames to CSV files
    train_data.to_csv(train_csv_path, index=False, header=False)
    test_data.to_csv(test_csv_path, index=False, header=False)

    print(f"Train data saved to {train_csv_path}")
    print(f"Test data saved to {test_csv_path}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python split_train_test_fbleau.py <input_directory> <train_output_directory> <test_output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    train_output_directory = sys.argv[2]
    test_output_directory = sys.argv[3]

    # List all CSV files in the input directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

    # Process each file
    for csv_file in csv_files:
        input_csv_path = os.path.join(input_directory, csv_file)
        split_and_save_csv(input_csv_path, train_output_directory, test_output_directory)

if __name__ == "__main__":
    main()

#input_directory = 'C:\\Users\\ss6365\\Desktop\\11111\\Geolife\\Machine_Learning\\Staircase\\encoded\\2km\\200'
#train_output_directory = 'C:\\Users\\ss6365\\Desktop\\11111\\Geolife\\Fbleau\\train\\Staircase\\200'
#test_output_directory = 'C:\\Users\\ss6365\\Desktop\\11111\\Geolife\\Fbleau\\test\\Staircase\\200'


#python split_train_test_fbleau.py <input_directory> <train_output_directory> <test_output_directory>
