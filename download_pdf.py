# Downloads all workouts on the log as PDFs
# Usage: python3 download_workouts.py <log_folder>
# Example: python3 download_workouts.py "log"

import os
import sys

# Check if the folder is valid
if len(sys.argv) != 2:
    print("Usage: python3 download_workouts.py <log_folder>")
    sys.exit(1)

log_folder = sys.argv[1]
if not os.path.isdir(log_folder):
    print("Invalid folder")
    sys.exit(1)

valid_folders = ["upper", "lower", "abs", "full"]
for folder in valid_folders:
    if not os.path.isdir(os.path.join(log_folder, folder)):
        print("Invalid folder structure")
        sys.exit(1)

    # Loop through each workout csv file
    for file in os.listdir(os.path.join(log_folder, folder)):
        if file.endswith(".csv"):
            workout_name = file.split(".csv")[0]
            url = "https://www.darebee.com/pdf/workouts/" + workout_name + ".pdf"
            # Create /tmp/darebee
            os.system("mkdir -p /tmp/darebee")
            # Download url to /tmp/darebee
            os.system("wget " + url + " -P " + "/tmp/darebee")

print("Done")
