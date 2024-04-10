import argparse
import os
import json
import logging
from data_processor import process_file_staircase_intermediate

def load_staircase_noise_samples(epsilon, bound_value, noise_dir):
    """Load staircase noise samples for given epsilon and bound_value from a file."""
    file_name = f"staircase_noise_epsilon_{epsilon}_bl_{bound_value}.json"
    file_path = os.path.join(noise_dir, file_name)
    with open(file_path, 'r') as file:
        samples = json.load(file)
    return samples

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data files with Staircase Intermediate Mechanism.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input CSV files.')
    parser.add_argument('--output_dir', required=True, help='Directory to save output CSV files.')
    parser.add_argument('--min_r_value', type=int, required=True, help='Bounding parameter (bl) for the staircase noise as minimum r value.')
    parser.add_argument('--delta', type=int, required=True, help='Delta parameter for differential privacy.')
    return parser.parse_args()

def main_staircase_intermediate():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_arguments()

    base_directory_input = args.input_dir
    base_directory_output = args.output_dir
    noise_directory = r"C:\Users\ss6365\Desktop\VisualCodeImplementation\noise_staircase" # Update this path to where your noise files are stored
    predefined_min_r_values = [20, 50, 100, 200, 10000]
    max_min_r_value = max(predefined_min_r_values)

    for epsilon in [0.1, 1]:
        noise_staircase_bounded = load_staircase_noise_samples(epsilon, args.min_r_value, noise_directory)
        noise_staircase = load_staircase_noise_samples(epsilon, max_min_r_value, noise_directory)

        for file_name in os.listdir(base_directory_input):
            if file_name.endswith('.csv'):
                file_path = os.path.join(base_directory_input, file_name)
                process_file_staircase_intermediate(file_path, epsilon, base_directory_output, 
                                                    noise_staircase, noise_staircase_bounded,
                                                    args.delta)

if __name__ == '__main__':
    main_staircase_intermediate()
