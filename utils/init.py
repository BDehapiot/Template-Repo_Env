#%% Imports -------------------------------------------------------------------

import re
import requests
import platform
import subprocess
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path(".").resolve()
REPO_OWNER = "BDehapiot"
REPO_NAME = ROOT_PATH.name
ENV_NAME = REPO_NAME.split("_", 1)[1] if "_" in REPO_NAME else REPO_NAME

#%% Parse config.yml ----------------------------------------------------------

def parse_config():

    config = {}

    # Read config.yml as txt
    with open(ROOT_PATH / "utils" / "config.yml", "r") as file:
        txt = file.read()

    # Extract "General" variables
    match = re.search(r'repo_type: "([^"]*)"', txt)
    if match: config['repo_type'] = match.group(1)
    match = re.search(r'python_version: "([^"]*)"', txt)
    if match: config['python_version'] = match.group(1)

    # Extract "Readme" variables
    match = re.search(r'instructions: "([^"]*)"', txt)
    if match: config['instructions'] = match.group(1)

    # Extract "Tests" variables
    match = re.search(r'tested_python: "([^"]*)"', txt)
    if match: config['tested_python'] = match.group(1)
    match = re.search(r'tested_os: "([^"]*)"', txt)
    if match: config['tested_os'] = match.group(1)
                                                
    return config

config = parse_config()

#%% Setup conda environment ---------------------------------------------------

def setup_conda_env():

    # Create a new conda environement
    subprocess.run([
        'conda', 'create', '-n', ENV_NAME, 
        f'python={config["python_version"]}', 'pip', '-y'
        ], shell=True)

    # Install dependencies
    if platform.system() == "Windows":
        requirements_path = ROOT_PATH / "requirements.txt"
    else:
        requirements_path = ROOT_PATH.parent / "requirements.txt"
    subprocess.run([
        'conda', 'run', '-n', ENV_NAME, 
        'pip', 'install', '-r', str(requirements_path)
        ], shell=True)
    
setup_conda_env()

#%% Update Repository files ---------------------------------------------------

# Issue: request is not in conda base environement!
 
repo_metadata = requests.get(
    f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    ).json()


#%% Replace placeholders ------------------------------------------------------

# def replace_placeholders(file_path):
    
#     # Read file
#     with open(file_path, "r") as file:
#         txt = file.read()
    
#     # Replace placeholders
#     txt = txt.replace("{{ repo_name }}", REPO_NAME)
#     txt = txt.replace("{{ repo_description }}", REPO_METADATA.get("description"))
#     txt = txt.replace("{{ env_name }}", ENV_NAME)
#     txt = txt.replace("{{ python_version }}", CONFIG["python_version"])
#     txt = txt.replace("{{ os_versions }}", CONFIG["os_versions"])
#     txt = txt.replace("{{ python_versions }}", CONFIG["python_versions"])

#     # Update file
#     with open(file_path.with_stem(file_path.stem + "_copy"), "w") as file:
#         file.write(txt)

# replace_placeholders(ROOT_PATH / "README.md")
# replace_placeholders(ROOT_PATH / "setup.cfg")
# replace_placeholders(ROOT_PATH / ".github" / "workflows" / "test.yml")

#%% Setup requirements --------------------------------------------------------

# def setup_requirements(dependencies):

#     with open(ROOT_PATH / 'requirements.txt', 'r') as file:
#         txt = file.read()

#     with open(ROOT_PATH / 'requirements.txt', 'a') as file:
#         for item in dependencies:
#             if item not in txt:
#                 file.write("\n%s" % item)

# setup_requirements(CONFIG["dependencies"])

#%% Install conda env ---------------------------------------------------------

# def setup_conda_env():
#     subprocess.run(['conda', 'create', '-n', ENV_NAME, f'python={CONFIG["python_version"]}', 'pip', '-y'])
#     subprocess.run(['pip', 'install', '-r', str(ROOT_PATH / 'requirements.txt')])
