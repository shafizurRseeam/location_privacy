import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
  
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 1',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_1 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_1"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_2"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 3',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_3 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_3"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 4',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_4 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_4"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_5"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 6',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_6 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_6"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 7',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_7 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_7"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 8',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_8 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_8"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 9',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_9 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_9"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 11',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_11 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_11"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 12',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_12 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_12"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 13',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_13 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_13"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 14',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_14 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_14"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 15',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_15 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_15"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 16',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_16 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_16"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 17',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_17 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_17"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 18',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_18 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_18"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 19',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_19 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_19"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\20_len_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed\our_bl_50_delta_20"',
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
