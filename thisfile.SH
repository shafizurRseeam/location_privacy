#!/bin/bash

# Use the first command-line argument as the base path
basePath="$1"
if [ -z "$basePath" ]; then
    echo "Base directory is not provided."
    exit 1
fi

# Extract the last part of the base path for the file name
subscript="${basePath##*/}"

# Define the directories
directories=( "Laplace" "Staircase" "Our_bl_50_delta_5" "LaplaceDelta5")

# Define the suffixes to iterate over
suffixes=(0.1 0.2 0.5 1 2 3 4 5)

# Initialize CSV file and write the header row. Include the extracted part in the file name.
csvFile="${basePath}/bsm_ln_200_${subscript}.csv"
# Join directory names with commas for the header row
header="Suffix"
for dir in "${directories[@]}"; do
    header="$header,$dir"
done
echo "$header" > "$csvFile"

# Iterate over each suffix
for suffix in "${suffixes[@]}"; do
    # Initialize a line starting with the suffix
    line="$suffix"
    
    # Iterate over each directory
    for dir in "${directories[@]}"; do
        trainFile="$basePath/train/$dir/200/${suffix}.csv"
        testFile="$basePath/test/$dir/200/${suffix}.csv"

        # Check if both files exist
        if [[ -f "$trainFile" && -f "$testFile" ]]; then
            # Run fbleau and capture the output
            output=$(fbleau knn --knn-strategy ln "$trainFile" "$testFile")
            # Extract Bayes security measure from the output
            bayesMeasure=$(echo "$output" | grep -o 'Bayes security measure: [0-9.]*' | awk '{print $4}')
            # Append the measure to the line
            line+=",${bayesMeasure}"
        else
            # If files are missing, append a placeholder
            line+=",NA"
        fi
    done
    
    # Write the line to the CSV file
    echo "$line" >> "$csvFile"
done

echo "Process completed. Bayes security measures saved to $csvFile."
