import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [

   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack10 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_10\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_10\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_10\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_10\test"',

   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack20 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\test"',
   
   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack30 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\test"',
   
   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack40 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\test"',
   
   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack50 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\test"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack20 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_20\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack30 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_30\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack40 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_40\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack50 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau_50\train"',
  
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
