import os
import pandas as pd
import sys
from sklearn.model_selection import train_test_split

def split_and_save_csv(input_csv_path, train_output_dir, test_output_dir, test_size=0.2, random_state=42):
    file_name = os.path.splitext(os.path.basename(input_csv_path))[0]
    eps = file_name.split('_')[-3]  # Extract the eps value, assuming it's in a consistent position

    df = pd.read_csv(input_csv_path)
    df = df[['location_id', 'perturbed_latitude', 'perturbed_longitude']]
    
    train_data, test_data = train_test_split(df, test_size=test_size, random_state=random_state)

    if not os.path.exists(train_output_dir):
        os.makedirs(train_output_dir)
    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)

    train_csv_path = os.path.join(train_output_dir, f'{eps}.csv')
    test_csv_path = os.path.join(test_output_dir, f'{eps}.csv')

    train_data.to_csv(train_csv_path, index=False, header=False)
    test_data.to_csv(test_csv_path, index=False, header=False)

    print(f"Train data saved to {train_csv_path}")
    print(f"Test data saved to {test_csv_path}")

def main(base_input_directory, base_train_output_directory, base_test_output_directory):
    # Mechanisms to process
    mechanisms = ['staircase', 'our_bl_50_delta_5', 'laplace']

    # List of directory names as numeric values
    dir_names = [60, 100, 120, 200, 300, 400]

    for mechanism in mechanisms:
        print(f"Processing mechanism: {mechanism}")
        for dir_name in dir_names:
            input_directory = os.path.join(base_input_directory, mechanism, str(dir_name))
            train_output_directory = os.path.join(base_train_output_directory, mechanism, str(dir_name))
            test_output_directory = os.path.join(base_test_output_directory, mechanism, str(dir_name))

            if not os.path.exists(input_directory):
                print(f"Directory does not exist: {input_directory}")
                continue  # Skip to the next directory if the current one does not exist

            csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

            for csv_file in csv_files:
                input_csv_path = os.path.join(input_directory, csv_file)
                split_and_save_csv(input_csv_path, train_output_directory, test_output_directory)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <base_dir> <train_dir> <test_dir>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])

# python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\machine_learning\attack1 C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\fbleau\train C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\fbleau\test
