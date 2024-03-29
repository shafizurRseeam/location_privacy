import os
import json
import numpy as np
import random
import scipy.special
import argparse

# Set the random seed for numpy and random modules at the beginning of the script.
np.random.seed(42)
random.seed(42)

def pdf_values(epsilon, x_interval, L):
    b = (1 - np.exp(-epsilon)) / x_interval
    intervals = int(L / x_interval)
    positions = np.linspace(0, L - x_interval, intervals)
    unnormalized_pdf_samples = b * np.exp(-epsilon * positions)
    area = np.sum(unnormalized_pdf_samples) * x_interval
    normalized_pdf_samples = unnormalized_pdf_samples / area
    return positions, normalized_pdf_samples

def generate_staircase_noise_samples(epsilon, x_interval, L, number_samples, min_r_value):
    samples = []
    while len(samples) < number_samples:
        positions, normalized_pdf_samples = pdf_values(epsilon, x_interval, L)
        cdf = np.cumsum(normalized_pdf_samples)
        cdf /= cdf[-1]
        r = np.random.rand()
        index = np.searchsorted(cdf, r)
        theta = np.random.uniform(0, 2 * np.pi)
        start_of_interval = positions[index]
        end_of_interval = start_of_interval + x_interval
        random_r_value = np.random.uniform(start_of_interval, end_of_interval)
        if abs(random_r_value) < min_r_value:
            x, y = random_r_value * np.cos(theta), random_r_value * np.sin(theta)
            samples.append((x, y))
    return samples

def save_noise_samples(samples, epsilon, min_r_value, output_dir):
    file_name = f"staircase_noise_epsilon_{epsilon}_bl_{min_r_value}.json"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        json.dump(samples, file)
    print(f"Saved noise samples to {file_path}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate and save Staircase noise samples.")
    parser.add_argument('output_dir', type=str, help='Directory to save output noise samples.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    output_dir = args.output_dir
    # Hardcoded values for epsilon and min_r_value
    epsilon_values = [0.1, 0.2, 0.5, 1, 2, 3, 4, 5]
    min_r_values = [20, 50, 100, 200, 10000]
    x_interval = 0.1
    L = 10000
    number_samples = 20000

    for epsilon in epsilon_values:
        for min_r_value in min_r_values:
            samples = generate_staircase_noise_samples(epsilon, x_interval, L, number_samples, min_r_value)
            save_noise_samples(samples, epsilon, min_r_value, output_dir)
