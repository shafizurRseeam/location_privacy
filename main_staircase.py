import argparse
import os
import logging
from data_processor import process_file_staircase
from noise_generation import generate_staircase_noise_samples

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data files with Staircase Laplace Mechanism.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input CSV files.')
    parser.add_argument('--output_dir', required=True, help='Directory to save output CSV files.')
    return parser.parse_args()

def main_staircase():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_arguments()

    base_directory_input = args.input_dir
    base_directory_output = args.output_dir
    
    # Check if the input directory exists and is a directory
    if not os.path.isdir(base_directory_input):
        logging.error("Input directory does not exist or is not a directory.")
        raise ValueError("Input directory does not exist or is not a directory.")
    
    # Check if the input directory contains at least one CSV file
    if not any(file.endswith('.csv') for file in os.listdir(base_directory_input)):
        logging.error("Input directory does not contain any CSV files.")
        raise ValueError("Input directory does not contain any CSV files.")
    
    # Ensure output directory exists
    os.makedirs(base_directory_output, exist_ok=True)
    
    epsilon_values = [0.1, 0.2, 0.5, 1, 2, 3, 4, 5]
    number_samples = 20000

    L = 10000
    x_interval= 0.1
    
    for epsilon in epsilon_values:
        noise_staircase = generate_staircase_noise_samples(epsilon, x_interval,
                                                          L, number_samples)
        for file_name in os.listdir(base_directory_input):
            if file_name.endswith('.csv'):
                file_path = os.path.join(base_directory_input, file_name)
                process_file_staircase(file_path, epsilon, base_directory_output, noise_staircase)

if __name__ == '__main__':
    main_staircase()


# python main_staircase.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary"    