
# Program creation timestamp:
PROJECT_CREATION = "@"

# Program description:
PROJECT_DESCRIPTION = ""

# Program template version:
PROJECT_TEMPLATE_VERSION = "@241118-1-1316"

# Program run command in Android:Termux:Python :
RUN_COMMAND = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__base_projects/_at241118-1-1316_dev_dont-copy_project-name/code/main.py"

#####

PRADHANA_ROOT = "/storage/emulated/0/BitMiller/Pradhana/"

DROPBOX_PATHCHUNK = "Dropbox/"

NS_DROPBOX_PATHCHUNK = "_no_sync_Dropbox/"

PY_PROGRAMS_ROOT_PATHCHUNK = "bitmiller_hu/progs/python_for_termux/"

PROJECT_ROOT_PATHCHUNK = "__base_projects/_at241118-1-1316_dev_dont-copy_project-name"

#####

PY_PROGRAMS_ROOT = "/storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux"

PROJECT_ROOT = PRADHANA_ROOT + DROPBOX_PATHCHUNK + PY_PROGRAMS_ROOT_PATHCHUNK + PROJECT_ROOT_PATHCHUNK

NS_PROJECT_ROOT = PRADHANA_ROOT + NS_DROPBOX_PATHCHUNK + PY_PROGRAMS_ROOT_PATHCHUNK + PROJECT_ROOT_PATHCHUNK

# Change working directory to project's root directory
prj_root = run_cmd[7:]
prj_root = os.path.dirname(prj_root)
prj_root = os.path.dirname(prj_root)
os.chdir(prj_root)

OUTPUT_LIGHT_PATH = PROJECT_ROOT + "/_no_sync/output_light"

OUTPUT_HEAVY_PATH = PROJECT_ROOT + "/_no_sync/output_light"

COMMON_MODULES_PATH = "/storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__common"


