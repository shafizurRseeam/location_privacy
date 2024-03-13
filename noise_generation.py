import numpy as np
import random
import scipy.special



def pdf_values(epsilon, x_interval, L):
    """Compute normalized PDF values for a given range using the given epsilon."""
    b = (1 - np.exp(-epsilon)) / x_interval
    intervals = int(L / x_interval)
    positions = np.linspace(0, L - x_interval, intervals)  # directly create the positions array
    unnormalized_pdf_samples = b * np.exp(-epsilon * positions)
    
    # Normalize
    area = np.sum(unnormalized_pdf_samples) * x_interval
    normalized_pdf_samples = unnormalized_pdf_samples / area
    return positions, normalized_pdf_samples

def draw_from_pdf(epsilon, x_interval, L):
    positions, normalized_pdf_samples = pdf_values(epsilon, x_interval, L)
    
    # Compute the cumulative distribution
    cdf = np.cumsum(normalized_pdf_samples)
    cdf /= cdf[-1]
    
    # Draw a random number between 0 and 1
    r = np.random.rand()
    
    # Find the index where the random number fits into the CDF
    index = np.searchsorted(cdf, r)
    
    # Get radial distance from the selected interval
    start_of_interval = positions[index]
    end_of_interval = start_of_interval + x_interval
    random_r_value = np.random.uniform(start_of_interval, end_of_interval)
    
    # Generate the random theta value
    theta = np.random.uniform(0, 2 * np.pi)
    
    # Convert r and theta to x and y
    x = random_r_value * np.cos(theta)
    y = random_r_value * np.sin(theta)
    
    return x, y

def generate_laplace_noise_samples(number_samples, epsilon):
    samples = []
    for _ in range(number_samples):
        theta = np.random.uniform(0, 2 * np.pi)
        p = random.random()
        r = -1 / epsilon * (scipy.special.lambertw((p - 1) / np.e, k=-1, tol=1e-8).real + 1)
        x, y = r * np.cos(theta), r * np.sin(theta)
        samples.append((x, y))
    return samples

def generate_staircase_noise_samples(epsilon, x_interval, L, number_samples):
    samples = []
    for _ in range(number_samples):
        x, y = draw_from_pdf(epsilon, x_interval, L)
        samples.append((x, y))
    return samples


