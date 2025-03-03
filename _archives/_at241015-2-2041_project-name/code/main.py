#BEGIN#

#help: https://www.w3schools.com/python/default.asp

import os

# Program creation timestamp
prg_ver = "@"

# Program description
prg_dsc = ""

# Program template version
prg_template_ver = "@241015-2-2041"

# Program run command in Android:Termux:Python
run_cmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__base_projects/_base_at241015-2-2041/code/main.py"

# Change working directory to project's root directory
prj_root = "storage/shared/"+run_cmd[27:]
prj_root = os.path.dirname(prj_root)
#print("Prj root: "+prj_root)
os.chdir(prj_root)

print()
print("==******************==")
print("    PROGRAM BEGIN    ")
print(f"Version: {prg_ver}")
print(f"Description: {prg_dsc}")
print(f"Working dir/Project root dir: {os.getcwd()}")
print("----------------------\n\n")

#----------------------------------------#





#----------------------------------------#

print("\n\n----------------------")
print("     PROGRAM END")
print("==******************==")
print()

#END#