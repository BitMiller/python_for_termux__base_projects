
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

PY_PROGRAMS_ROOT = PRADHANA_ROOT + DROPBOX_PATHCHUNK + PY_PROGRAMS_ROOT_PATHCHUNK

PROJECT_ROOT = PY_PROGRAMS_ROOT + PROJECT_ROOT_PATHCHUNK

NS_PY_PROGRAMS_ROOT = PRADHANA_ROOT + NS_DROPBOX_PATHCHUNK + PY_PROGRAMS_ROOT_PATHCHUNK

NS_PROJECT_ROOT = NS_PY_PROGRAMS_ROOT + PROJECT_ROOT_PATHCHUNK

# Normal output for light data:
OUTPUT_PATH = PROJECT_ROOT + "output"

# Normal output for light, sensitive data:
NS_OUTPUT_PATH = PROJECT_ROOT + "_no_sync/output"

# No-Dropbox output for heavy data:
ND_OUTPUT_PATH = NS_PROJECT_ROOT + "output"

# No-Dropbox output for heavy, sensitive data:
ND_NS_OUTPUT_PATH = NS_PROJECT_ROOT + "_no_sync/output"

COMMON_MODULES_PATH = PY_PROGRAMS_ROOT + "__common/"


