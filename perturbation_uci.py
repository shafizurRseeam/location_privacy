import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
    r'python main_laplace.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary"',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" laplace laplace',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\laplace"',
    r'python main_laplace_delta.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary"',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" laplace_delta_5 laplaceDelta',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\laplace_delta_5"',
    r'python main_staircase.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary"',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" staircase staircase',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\staircase"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_50_delta_5"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_50_delta_10"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_50_delta_20"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 200 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_200_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_200_delta_5"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 500 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_500_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_500_delta_5"',
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\utility" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --bl 1000 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\{mechanism}\{epsilon}" our_bl_1000_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed\our_bl_1000_delta_5"',
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
