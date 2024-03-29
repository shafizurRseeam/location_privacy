import os
import json
import numpy as np
import random
import scipy.special
import argparse  # Import the argparse module

def set_random_seed(seed=42):
    np.random.seed(seed)
    random.seed(seed)

def generate_laplace_noise_samples(number_samples, epsilon, min_r_value):
    """Generate and return samples where the radial distance r is less than min_r_value."""
    set_random_seed()
    samples = []
    while len(samples) < number_samples:
        theta = np.random.uniform(0, 2 * np.pi)
        p = random.random()
        r = -1 / epsilon * (scipy.special.lambertw((p - 1) / np.e, k=-1, tol=1e-8).real + 1)
        if abs(r) < min_r_value:
            x, y = r * np.cos(theta), r * np.sin(theta)
            samples.append((x, y))
    return samples

def save_noise_samples(epsilon_values, number_samples, min_r_value, output_dir):
    """Save noise samples for each epsilon to separate files."""
    os.makedirs(output_dir, exist_ok=True)
    for epsilon in epsilon_values:
        samples = generate_laplace_noise_samples(number_samples, epsilon, min_r_value)
        file_path = os.path.join(output_dir, f"laplace_noise_epsilon_{epsilon}.json")
        with open(file_path, 'w') as file:
            json.dump(samples, file)
        print(f"Saved noise samples for epsilon={epsilon} to {file_path}")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate and save Laplace noise samples.")
    parser.add_argument('output_dir', type=str, help='Directory to save output noise samples.')
    # Ensure this line is exactly as shown, to correctly define the --min_r_value argument
    parser.add_argument('--min_r_value', type=float, default=10000.0, help='Minimum r value to include in samples.')
    args = parser.parse_args()
    return args.output_dir, args.min_r_value

if __name__ == '__main__':
    output_dir, min_r_value = parse_arguments()
    epsilon_values = [0.1, 0.2, 0.5, 1, 2, 3, 4, 5]
    number_samples = 20000  # Adjust as needed
    save_noise_samples(epsilon_values, number_samples, min_r_value, output_dir)



#  python noise_generation_files_laplace.py 'C:\Users\ss6365\Desktop\VisualCodeImplementation\noise'