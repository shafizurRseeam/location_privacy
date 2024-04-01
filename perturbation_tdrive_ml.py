import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\laplace"',
     r'python main_laplace_delta_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" laplace_delta_5 laplaceDelta',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\laplace_delta_5"',
     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\staircase"',
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\our_bl_50_delta_5"',
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --min_r_value 50 --delta 10 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\our_bl_50_delta_10"', 
     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --min_r_value 50 --delta 20 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\our_bl_50_delta_20"',
    #  r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --min_r_value 20 --delta 5 --iteration 20',
    #  r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" our_bl_20_delta_5 our',
    #  r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\our_bl_20_delta_5"',
    #  r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\data\security" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" --min_r_value 200 --delta 5 --iteration 20',
    #  r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\{mechanism}\{epsilon}" our_bl_200_delta_5 our',
    #  r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged\our_bl_200_delta_5"',
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
