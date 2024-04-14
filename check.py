import os
import pandas as pd
import sys

def remove_unseen_labels_and_overwrite_test_file(train_csv_path, test_csv_path):
    train_df = pd.read_csv(train_csv_path, header=None, usecols=[0])
    test_df = pd.read_csv(test_csv_path, header=None)
    train_labels = set(train_df.iloc[:, 0].unique())
    test_labels = set(test_df.iloc[:, 0].unique())
    missing_labels = test_labels - train_labels
    cleaned_test_df = test_df[~test_df[0].isin(missing_labels)]
    cleaned_test_df.to_csv(test_csv_path, index=False, header=False)

def process_all_files(base_train_directory, base_test_directory, mechanisms, dir_names):
    for mechanism in mechanisms:
        for dir_name in dir_names:
            train_directory = os.path.join(base_train_directory, mechanism, str(dir_name))
            test_directory = os.path.join(base_test_directory, mechanism, str(dir_name))
            if os.path.exists(train_directory) and os.path.exists(test_directory):
                train_files = [f for f in os.listdir(train_directory) if f.endswith('.csv')]
                for train_file in train_files:
                    train_csv_path = os.path.join(train_directory, train_file)
                    test_csv_path = os.path.join(test_directory, train_file)
                    if os.path.exists(test_csv_path):
                        remove_unseen_labels_and_overwrite_test_file(train_csv_path, test_csv_path)
                        print(f"Processed {train_file} in {mechanism}/{dir_name}")
                    else:
                        print(f"No corresponding test file for {train_file} in {mechanism}/{dir_name}")
            else:
                print(f"Directory does not exist: {mechanism}/{dir_name}")

def main(base_train_directory, base_test_directory):
    # Mechanisms to process
    mechanisms = ['laplace', 'staircase', 'our_bl_50_delta_5', 'our_bl_50_delta_10', 'our_bl_50_delta_15', 'our_bl_50_delta_20']
    # List of directory names as numeric values
    dir_names = [60, 100, 120, 200, 300, 400]
    process_all_files(base_train_directory, base_test_directory, mechanisms, dir_names)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <base_train_directory> <base_test_directory>")
    else:
        main(sys.argv[1], sys.argv[2])


# python check.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau_10\train" "C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau_10\train"
