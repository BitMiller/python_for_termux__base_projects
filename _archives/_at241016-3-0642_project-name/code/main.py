#BEGIN#

#help: https://www.w3schools.com/python/default.asp

import os

# Program creation timestamp:
prgVer = "@"

# Program description:
prgDsc = ""

# Program template version:
prgTemplateVer = "@241016-3-0642"

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__base_projects/_base_at241016-3-0642/code/main.py"

# Change working directory to project's root directory
prjRoot = "storage/shared/"+runCmd[27:]
prjRoot = os.path.dirname(prjRoot)
prjRoot = os.path.dirname(prjRoot)
os.chdir(prjRoot)

print()
print("==******************==")
print("    PROGRAM BEGIN    ")
print(f"Version: {prgVer}")
print(f"Description: {prgDsc}")
print(f"Working dir/Project root dir: {os.getcwd()}")
print("----------------------\n\n")

#----------------------------------------#





#----------------------------------------#

print("\n\n----------------------")
print("     PROGRAM END")
print("==******************==")
print()

#END#