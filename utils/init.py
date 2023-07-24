#%% Imports -------------------------------------------------------------------

import re
import platform
import subprocess
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path(__file__).resolve().parents[1]
REPO_NAME = ROOT_PATH.name
ENV_NAME = REPO_NAME.split("_", 1)[1] if "_" in REPO_NAME else REPO_NAME

#%% Setup conda environment ---------------------------------------------------

def setup_conda_env():

    # Get python version from config.yml
with open(ROOT_PATH / "utils" / "config.yml", "r") as file:
    txt = file.read()
    match = re.search(r'python_version: "([^"]*)"', txt)
    if match: python_version = match.group(1)

    # Create a new conda environement
    subprocess.run([
        'conda', 'create', '-n', ENV_NAME, 
        f'python={python_version}', 'pip', '-y'
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

#%% Setup repository ----------------------------------------------------------

def setup_repo():

    if platform.system() == "Windows":
        init_repo_path = ROOT_PATH / "utils" / "init_repo.py"
    else:
        init_repo_path = ROOT_PATH.parent / "utils" / "init_repo.py"

    subprocess.run([
    'conda', 'run', '-n', ENV_NAME, 
    'python', str(init_repo_path)
    ], shell=True)

setup_repo()
