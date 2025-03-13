#BEGIN#

#help: https://www.w3schools.com/python/default.asp

import os
from datetime import datetime
from p_main.p_constants import *

# Calculate DTS for running instance :
run_start_time = datetime.now()
run_instance_date_time_stamp = "at" \
+ str(run_start_time.year)[2:].zfill(2) \
+ str(run_start_time.month).zfill(2) \
+ str(run_start_time.day).zfill(2) \
+ "-" + str(run_start_time.weekday()+1) + "-" \
+ str(run_start_time.hour).zfill(2) \
+ str(run_start_time.minute).zfill(2) \
+ str(run_start_time.second).zfill(2) \
+ "-" \
+ str(run_start_time.microsecond).zfill(6)

# Change working directory to project's root directory
os.chdir(PROJECT_ROOT)

print()
print("==*******************==")
print("     PROGRAM BEGIN    ")
print(f"> Version: {prg_ver}")
print(f"> Description: {prg_dsc}")
print(f"> Working dir/Project's root dir: {os.getcwd()}")
print(f"> Run start time: {run_start_time}")
print(f"> run_instance_date_time_stamp: {run_instance_date_time_stamp}")
print("----------------------\n\n")

#----------------------------------------#



#----------------------------------------#

print("\n\n----------------------")
print("      PROGRAM END")
print("==*******************==")
print()

#END#