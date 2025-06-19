import os
import re
import subprocess

root_dir = "/media/disk_k/WbLS-DATA/raw_root/phase8/muon"
calib_file = "bnl1t_spe_fit_results_250209.csv"
script_name = "decayMuon_v2.py"

match = re.search(r"(\d{6})", calib_file)
if not match:
    raise ValueError("Calibration file name must contain a date in the format DDMMYYT (e.g. 250217T)")
date_str = match.group(1)  

# Loop over all ROOT files that contain the matching date
for filename in os.listdir(root_dir):
    if filename.endswith(".root") and date_str in filename:
        print(f"Processing {filename}")
        try:
            subprocess.run(["python3", script_name, filename, calib_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to process {filename}: {e}")
