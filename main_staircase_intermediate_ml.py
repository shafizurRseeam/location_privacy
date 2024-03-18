import argparse
import os
import logging
from data_processor_ml import process_file_staircase_intermediate_ml
from noise_generation import generate_staircase_noise_samples

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data files with Staircase Intermediate Mechanism.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input CSV files.')
    parser.add_argument('--output_dir', required=True, help='Directory to save output CSV files.')
    return parser.parse_args()

def main_staircase_intermediate_ml():

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
    
    epsilon_values = [0.1]
    number_samples = 10
    L = 10000
    x_interval= 0.1
    bl = 50
    delta = 5
    num_iterations = 10
    for epsilon in epsilon_values:

        noise_staircase_bounded = generate_staircase_noise_samples(epsilon, x_interval, bl, number_samples)
        noise_staircase         = generate_staircase_noise_samples(epsilon, x_interval,  L, number_samples)

        for file_name in os.listdir(base_directory_input):
            if file_name.endswith('.csv'):

                file_path = os.path.join(base_directory_input, file_name)
                process_file_staircase_intermediate_ml(file_path, epsilon, base_directory_output, 
                                                    noise_staircase, noise_staircase_bounded,
                                                    delta, num_iterations)

if __name__ == '__main__':
    main_staircase_intermediate_ml()