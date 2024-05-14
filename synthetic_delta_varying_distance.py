import subprocess

# Define the commands to run, corrected for apparent path errors


commands = [
  


# #####################################################


    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_2" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\our_bl_50_delta_2"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_5" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\our_bl_50_delta_2"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\our_bl_50_delta_2"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\our_bl_50_delta_2"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 2',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\{mechanism}\{epsilon}" our_bl_50_delta_2 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\our_bl_50_delta_2"',

# #####################################################

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_2" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\our_bl_50_delta_5"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_5" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\our_bl_50_delta_5"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\our_bl_50_delta_5"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\our_bl_50_delta_5"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\our_bl_50_delta_5"',



    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_2" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_5" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 10',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\{mechanism}\{epsilon}" our_bl_50_delta_10 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\our_bl_50_delta_10"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_2" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\our_bl_50_delta_20"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_5" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\our_bl_50_delta_20"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\our_bl_50_delta_20"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\our_bl_50_delta_20"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 20',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\{mechanism}\{epsilon}" our_bl_50_delta_20 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\our_bl_50_delta_20"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_2" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 30',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\{mechanism}\{epsilon}" our_bl_50_delta_30 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_2\our_bl_50_delta_30"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_5" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 30',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\{mechanism}\{epsilon}" our_bl_50_delta_30 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_5\our_bl_50_delta_30"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_10" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 30',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\{mechanism}\{epsilon}" our_bl_50_delta_30 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_10\our_bl_50_delta_30"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_20" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 30',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\{mechanism}\{epsilon}" our_bl_50_delta_30 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_20\our_bl_50_delta_30"',

    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_30" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 30',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\{mechanism}\{epsilon}" our_bl_50_delta_30 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_30\our_bl_50_delta_30"',





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
