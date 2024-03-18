import os
import sys
import pandas as pd

def remove_unseen_labels_and_overwrite_test_file(train_csv_path, test_csv_path):
    # Load the datasets without headers and use the first column as labels
    train_df = pd.read_csv(train_csv_path, header=None, usecols=[0])
    test_df = pd.read_csv(test_csv_path, header=None)

    # Extract unique labels
    train_labels = set(train_df.iloc[:, 0].unique())
    test_labels = set(test_df.iloc[:, 0].unique())

    # Find labels in test set not present in training set
    missing_labels = test_labels - train_labels

    # Remove rows with labels not present in training set
    cleaned_test_df = test_df[~test_df[0].isin(missing_labels)]

    # Overwrite the original test file with the cleaned data
    cleaned_test_df.to_csv(test_csv_path, index=False, header=False)

def process_all_files(train_directory, test_directory):
    # Get list of all CSV files in the training directory
    train_files = [f for f in os.listdir(train_directory) if f.endswith('.csv')]

    # Process each file
    for train_file in train_files:
        train_csv_path = os.path.join(train_directory, train_file)
        test_csv_path = os.path.join(test_directory, train_file)

        if os.path.exists(test_csv_path):  # Check if the corresponding test file exists
            remove_unseen_labels_and_overwrite_test_file(train_csv_path, test_csv_path)
            print(f"Processed {train_file}")
        else:
            print(f"No corresponding test file for {train_file}")


if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("Usage: python test_train_check_br.py <train_directory> <test_directory>")
        sys.exit(1)

    train_directory = sys.argv[1]
    test_directory  = sys.argv[2]

    process_all_files(train_directory, test_directory)    