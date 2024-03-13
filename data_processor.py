import pandas as pd
import os
from mechanism_laplace import planar_laplace_mechanism
from mechanism_staircase import planar_staircase_mechanism

def process_file_laplace(file_path, epsilon, base_directory_output, noise_laplace):


    df = pd.read_csv(file_path)

    perturbed_locations = planar_laplace_mechanism(df.copy(), noise_laplace)


    
    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_laplace_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    perturbed_locations.to_csv(csv_file_path_out, index=False)

    print(f"Processed and saved: {output_csv_file_name}")



def process_file_staircase(file_path, epsilon, base_directory_output, noise_staircase):


    df = pd.read_csv(file_path)

    perturbed_locations = planar_staircase_mechanism(df.copy(), noise_staircase)


    
    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_staircase_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    perturbed_locations.to_csv(csv_file_path_out, index=False)

    print(f"Processed and saved: {output_csv_file_name}")