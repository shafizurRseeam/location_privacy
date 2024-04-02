import argparse
import os
import logging
from data_processor_ml import process_file_staircase_ml
from noise_generation import generate_staircase_noise_samples
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data files with Staircase Laplace Mechanism.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input CSV files.')
    parser.add_argument('--output_dir', required=True, help='Directory to save output CSV files.')
    parser.add_argument('--min_r_value', type=int, default=None, help='Optional minimum r value to include in samples.')
    parser.add_argument('--iteration', required=True, help='Directory to save output CSV files.')

    return parser.parse_args()

def load_staircase_noise_samples(epsilon, min_r_value, noise_dir):
    """Load staircase noise samples for given epsilon and min_r_value from a file."""
    file_name = f"staircase_noise_epsilon_{epsilon}_bl_{min_r_value}.json"
    file_path = os.path.join(noise_dir, file_name)
    with open(file_path, 'r') as file:
        samples = json.load(file)
    return samples

def main_staircase_ml():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_arguments()

    base_directory_input = args.input_dir
    base_directory_output = args.output_dir
    num_iterations_ml = int(args.iteration)

    # Update the path to your actual directory where noise files are stored
    noise_directory = r"C:\Users\ss6365\Desktop\VisualCodeImplementation\noise_staircase"
    
    predefined_min_r_values = [20, 50, 100, 200, 10000]  # Predefined list of min_r_values
    min_r_value = args.min_r_value if args.min_r_value is not None else max(predefined_min_r_values)

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


 
    
    for epsilon in epsilon_values:
        noise_staircase = load_staircase_noise_samples(epsilon, min_r_value, noise_directory)

        for file_name in os.listdir(base_directory_input):
            if file_name.endswith('.csv'):
                file_path = os.path.join(base_directory_input, file_name)
                process_file_staircase_ml(file_path, epsilon, base_directory_output, noise_staircase, num_iterations_ml)

if __name__ == '__main__':
    main_staircase_ml()