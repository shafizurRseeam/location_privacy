import os
import shutil
import sys

def move_files(source_directory, destination_directory_template, mechanism, file_suffix):
    # Epsilon values
    epsilon_values = ['0.1', '0.2', '0.5', '1', '2', '3', '4', '5']
    
    # Iterate through CSV files in the source directory
    for filename in os.listdir(source_directory):
        if filename.endswith('.csv'):
            for epsilon in epsilon_values:
                if filename.endswith(f'_{file_suffix}_{epsilon}.csv'):
                    source_file = os.path.join(source_directory, filename)
                    destination_directory = destination_directory_template.format(mechanism=mechanism, epsilon=epsilon)
                    os.makedirs(destination_directory, exist_ok=True)  # Ensure the destination directory exists
                    destination_file = os.path.join(destination_directory, filename)
                    shutil.copy(source_file, destination_file)
                    print(f"Moved {filename} to {destination_directory}")
                    break  # Exit the inner loop once a match is found

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python move_files.py <source_directory> <destination_directory_template> <mechanism> <file_suffix>")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    destination_directory_template = sys.argv[2]
    mechanism = sys.argv[3]
    file_suffix = sys.argv[4]
    move_files(source_directory, destination_directory_template, mechanism, file_suffix)

#execution 
#python move_files.py "C:\Path\To\Source" "C:\Path\To\Destination\{mechanism}\{epsilon}" Staircase staircase
    
