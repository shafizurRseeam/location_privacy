import pandas as pd
import os
from mechanism_laplace import planar_laplace_mechanism
from mechanism_staircase import planar_staircase_mechanism
from mechanism_staircase_intermediate import intermediate, only_reported_locations
from mechanism_laplace_delta import planar_laplace_mechanism_delta





def process_file_laplace_ml(file_path, epsilon, 
                         base_directory_output, noise_laplace, num_iterations):


    df = pd.read_csv(file_path)

    perturbed_results = []

    for _ in range(num_iterations):

        perturbed_locations = planar_laplace_mechanism(df.copy(), noise_laplace)
        perturbed_results.append(perturbed_locations)


    averaged_perturbed_df = pd.concat(perturbed_results).groupby(level = 0).mean(numeric_only=True)


    
    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_laplace_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    averaged_perturbed_df.to_csv(csv_file_path_out, index=False)

    print(f"Processed and saved: {output_csv_file_name}")


def process_file_laplace_delta_ml(file_path, epsilon, 
                               base_directory_output, delta, 
                               noise_laplace, num_iterations):


    df = pd.read_csv(file_path)

    perturbed_results = []

    for _ in range(num_iterations):

        perturbed_locations = planar_laplace_mechanism_delta(df.copy(), noise_laplace, delta)
        perturbed_results.append(perturbed_locations)

    averaged_perturbed_df = pd.concat(perturbed_results).groupby(level = 0).mean(numeric_only=True)

    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_laplaceDelta_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    averaged_perturbed_df.to_csv(csv_file_path_out, index=False)

    print(f"Processed and saved: {output_csv_file_name}")


def process_file_staircase_ml(file_path, epsilon, base_directory_output, 
                           noise_staircase, num_iterations):


    df = pd.read_csv(file_path)

    perturbed_results = []


    for _ in range(num_iterations):

        perturbed_locations = planar_staircase_mechanism(df.copy(), noise_staircase)
        perturbed_results.append(perturbed_locations)

    averaged_perturbed_df = pd.concat(perturbed_results).groupby(level = 0).mean(numeric_only=True)
    
    
    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_staircase_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    averaged_perturbed_df.to_csv(csv_file_path_out, index=False)

    print(f"Processed and saved: {output_csv_file_name}")



def process_file_staircase_intermediate_ml(file_path, epsilon, base_directory_output,  
                                        noise_staircase, noise_staircase_bounded,
                                        delta, num_iterations):
    


 
    df = pd.read_csv(file_path)
    perturbed_results = []

    
    intermediate_dataset = intermediate(df.copy(), noise_staircase_bounded)

    for _ in range(num_iterations):
        
        Perturbed_our = only_reported_locations(intermediate_dataset.copy(), noise_staircase, delta)
        #print(Perturbed_our)

        perturbed_results.append(Perturbed_our)

    average_perturbed_df = pd.concat(perturbed_results).groupby(level=0).mean(numeric_only=True)
   
    original_file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_csv_file_name = f"{original_file_name}_our_{epsilon}.csv"
    csv_file_path_out = os.path.join(base_directory_output, output_csv_file_name)

    average_perturbed_df.to_csv(csv_file_path_out, index=False)
    print(f"Processed and saved: {output_csv_file_name}")


