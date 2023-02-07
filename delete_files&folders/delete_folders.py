## code to delete fish tracking videos and empty folders from data for sleep paper

import glob
import os


# Delete file whose name contains "figures" or "recorded_full_frames"
pattern = r"E:\OMR_sleep_deprivation\d8_08_24_2021_recovery\*\*"   # make sure to keep the /*/* in place of the fish folders

for item in glob.iglob(pattern, recursive=True):
    if "recorded_full_frames" in item:  # replace "recorded full frame" for folder you want to delete
        print("this:", item)
        try:
            os.rmdir(item)  # Replace 'tmp{i]' with your folder name
        except:continue

    # same priciple for folder "figures"
    if "figures" in item:  # replace "recorded full frame" for folder you want to delete
        print("this:", item)
        try:
            os.rmdir(item)  # Replace 'tmp{i]' with your folder name
        except:continue


