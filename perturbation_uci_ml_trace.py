import subprocess

# Define the commands to run, corrected for apparent path errors


commands = [

#Laplace
     #r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\laplace"',

     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\laplace"',

     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\laplace"',

     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_40" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\laplace"',

     r'python main_laplace_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_50" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\{mechanism}\{epsilon}" laplace laplace',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\laplace"',


#Staircase
     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\staircase"',

     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\staircase"',

     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\staircase"',

     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_40" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\staircase"',

     r'python main_staircase_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_50" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\{mechanism}\{epsilon}" staircase staircase',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\staircase"',

#Our

     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_10\our_bl_50_delta_5"',

     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_20\our_bl_50_delta_5"',

     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_30\our_bl_50_delta_5"',

     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_40" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_40\our_bl_50_delta_5"',

     r'python main_staircase_intermediate_ml.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\data\security_50" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" --min_r_value 50 --delta 5 --iteration 20',
     r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
     r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged_50\our_bl_50_delta_5"',


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
