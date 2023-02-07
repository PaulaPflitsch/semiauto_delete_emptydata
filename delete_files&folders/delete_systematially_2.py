## code to delete fish tracking videos and empty folders from data for sleep paper
import glob
import os
from pathlib import Path

## goes into directory in which this python script is located
#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

# input directory
dname = r"E:\OMR_sleep_deprivation\d8_08_24_2021_recovery"  #or just put in file name here
print(dname)

days = '2021_08_24' # replace date in days-variable
fish = [64]  # replace number of folders in dname as fish

# iterate through folders in dname
for day_idx, day in enumerate(days):
    for f in range(fish[day_idx]):
        folder = dname + "/" + f'{days}_fish{f +1:03d}'
        print(folder)

        for e in folder:
            sub_1 = folder + "/mode_movie.avi"     # replace for every item you want to remove (so far only workes with files, not folders)
            print(sub_1)
            try:
                os.remove(sub_1)
            except: continue

            sub_2 = folder + "/fish_roi.avi"  # replace for every item you want to remove (so far only workes with files, not folders)
            print(sub_2)
            try:
                os.remove(sub_2)
            except:
                continue

            sub_3 = folder + "/current_mode.png"  # replace for every item you want to remove (so far only workes with files, not folders)
            print(sub_3)
            try:
                os.remove(sub_3)
            except:
                continue

            sub_4 = folder + "/scene_error.txt"  # replace for every item you want to remove (so far only workes with files, not folders)
            print(sub_4)
            try:
                os.remove(sub_4)
            except:
                continue


