import subprocess
import csv
import re
import sys
import os

def run_fbleau_for_mechanism_and_size(base_directory, knn_strategy, versions, mechanisms, sizes):
    base_command = f"fbleau knn --knn-strategy {knn_strategy}"
    
    for size in sizes:
        for mechanism in mechanisms:
            results = []
            train_base_path = os.path.join(base_directory, "train", mechanism, size)
            test_base_path = os.path.join(base_directory, "test", mechanism, size)
            # Update file naming to include size
            if "udsdsi" in base_directory:
                dataset_identifier = "_uci"
            elif "colsdslectd" in base_directory:
                dataset_identifier = "_collected"
            else:
                dataset_identifier = ""  # Default to empty if neither is found
            output_csv = os.path.join(base_directory, f"fbleau_results_{mechanism}{dataset_identifier}_{knn_strategy}_{size}.csv")

            for version in versions:
                train_path = os.path.join(train_base_path, f"{version}.csv")
                test_path = os.path.join(test_base_path, f"{version}.csv")
                command = f"{base_command} {train_path} {test_path}"
                print(f"Running command for {mechanism}, size {size}, version {version}:")
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                
                # Parse the output
                metrics = parse_fbleau_output(result.stdout)
                results.append(metrics)

            # Save to CSV
            save_results_to_csv(output_csv, results)

def parse_fbleau_output(output):
    metrics = re.findall(r"Minimum estimate: (\S+)|Multiplicative Leakage: (\S+)|Additive Leakage: (\S+)|Bayes security measure: (\S+)|Min-entropy Leakage: (\S+)", output)
    metrics = [float(val) for sublist in metrics for val in sublist if val]
    return metrics

def save_results_to_csv(filename, data):
    headers = ["Minimum estimate", "Multiplicative Leakage", "Additive Leakage", "Bayes security measure", "Min-entropy Leakage"]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fbleau.py <base_directory> <knn-strategy>")
        sys.exit(1)

    base_directory = sys.argv[1]
    knn_strategy = sys.argv[2]
    versions = [0.1, 0.2, 0.5, 1, 2, 3, 4, 5]
    mechanisms = [ 'staircase', 'our_bl_50_delta_5','our_bl_50_delta_10', 'our_bl_50_delta_15', 'our_bl_50_delta_20', 'laplace','our_bl_20_delta_5', 'our_bl_200_delta_5', 'our_bl_500_delta_5'] 
    sizes = ['200']  # List of directory names
#'staircase', 'our_bl_50_delta_5','our_bl_50_delta_10', 'our_bl_50_delta_15', 'our_bl_50_delta_20', 'laplace',
    run_fbleau_for_mechanism_and_size(base_directory, knn_strategy, versions, mechanisms, sizes)
