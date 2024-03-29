import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
    # r'python main_laplace.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary"',
    # r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" laplace laplace',
    # r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\laplace"',
    # r'python main_laplace_delta.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary"',
    # r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" laplace_delta_5 laplaceDelta',
    # r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\laplace_delta_5"',
    # r'python main_staircase.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary"',
    # r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" staircase staircase',
    # r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\staircase"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 50 --delta 5',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_50_delta_5"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 50 --delta 10',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_50_delta_10"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 50 --delta 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_50_delta_20"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 200 --delta 5',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_200_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_200_delta_5"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 100 --delta 5',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_100_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_100_delta_5"',
     r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" --min_r_value 20 --delta 5',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\{mechanism}\{epsilon}" our_bl_20_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed\our_bl_20_delta_5"',
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
