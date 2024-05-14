import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
   #r'python encode_for_ml.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\perturbed_averaged" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack1"',
   #r'python encode_for_ml.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\perturbed_averaged" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack1"',
   #r'python encode_for_ml.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\perturbed_averaged" "C:\Users\ss6365\Desktop\location_privacy_final\uci\machine_learning\attack1"',
   #r'python encode_for_ml.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\perturbed_averaged" "C:\Users\ss6365\Desktop\location_privacy_final\collected\machine_learning\attack1"',
   r'python encode_for_ml.py "C:\Users\ss6365\Desktop\location_privacy_final\tracebased\perturbed_averaged_10" "C:\Users\ss6365\Desktop\location_privacy_final\tracebased\machine_learning\attack1"',

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
