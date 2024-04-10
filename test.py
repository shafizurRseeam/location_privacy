commands = [
  
    r'python main_staircase_intermediate.py --input_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\data\traj_20_distance_1" --output_dir "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" --min_r_value 50 --delta 5',
    r'python move_files.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\temporary" "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_1\{mechanism}\{epsilon}" our_bl_50_delta_5 our',
    r'python merge_csv_in_subdirs.py "C:\Users\ss6365\Desktop\location_privacy_final\synthetic\perturbed_20_distance_1\our_bl_50_delta_5"',

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





]