import subprocess

# Define the commands to run, corrected for apparent path errors


commands = [

     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\laplace"',
     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\laplace"',
     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\laplace"',
     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\laplace"',

     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\staircase"',
     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\staircase"',
     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\staircase"',
     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\staircase"', 


     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_20\perturbed_averaged\our_bl_50_delta_5"',
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_50\perturbed_averaged\our_bl_50_delta_5"',
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_100\perturbed_averaged\our_bl_50_delta_5"',
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\trace\collected_200\perturbed_averaged\our_bl_50_delta_5"',




]

# Execute each command sequentially
for command in commands:
    print(f"Executing: {command}")
    # Using shell=True can be a security hazard with untrusted input. Since you control the strings here, it should be okay.
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed.")
        break  # If a command fails, break the loop to avoid proceeding with dependent commands

print("All commands executed.")
