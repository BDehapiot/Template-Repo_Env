#%% Imports -------------------------------------------------------------------

import yaml
import shutil
import urllib
import requests
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path(__file__).resolve().parents[1]
REPO_OWNER = "BDehapiot"
REPO_NAME = ROOT_PATH.name
ENV_NAME = REPO_NAME.split("_", 1)[1] if "_" in REPO_NAME else REPO_NAME

#%% Extract info --------------------------------------------------------------

def extract_info():

    # Parse config.yml
    with open(ROOT_PATH / "utils" / "config.yml", "r") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)

    # Get repository metadata (GitHub API)
    github = requests.get(
        f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
        ).json()
    
    return config, github

config, github = extract_info()

#%% Setup repository ----------------------------------------------------------

def setup_repo():

    # Define paths
    ressources_path = Path(ROOT_PATH / "utils" / "ressources")
    backup_path = Path(ROOT_PATH / "utils" / "backup")
    workflows_path = Path(ROOT_PATH / ".github" / "workflows")
    tests_path = Path(ROOT_PATH / "tests")

    if config["repo_type"] in ["python_lite"]:
        
        try: (ROOT_PATH / "pyproject.toml").unlink()
        except FileNotFoundError: pass
        try: (ROOT_PATH / "setup.cfg").unlink()
        except FileNotFoundError: pass

    if config["repo_type"] in ["python_lite", "python_build"]:

        try: shutil.rmtree(ROOT_PATH / ".github")
        except FileNotFoundError: pass
        try: shutil.move(ROOT_PATH / "tests", backup_path / "tests")
        except FileNotFoundError: pass

    if config["repo_type"] in ["python_build", "python_test"]:

        try: 
            shutil.move(backup_path / "pyproject.toml", ROOT_PATH / "pyproject.toml")
        except FileNotFoundError:
            shutil.copy(ressources_path / "pyproject.toml", ROOT_PATH / "pyproject.toml")
        try: 
            shutil.move(backup_path / "setup.cfg", ROOT_PATH / "setup.cfg")
        except FileNotFoundError:
            shutil.copy(ressources_path / "setup.cfg", ROOT_PATH / "setup.cfg")

    if config["repo_type"] in ["python_test"]:

        try: 
            shutil.move(backup_path / ".github", ROOT_PATH / ".github")
        except FileNotFoundError:
            workflows_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(ressources_path / "test.yml", workflows_path / "test.yml")
        try: 
            shutil.move(backup_path / "tests", ROOT_PATH / "tests")
        except FileNotFoundError:
            tests_path.mkdir(parents=True, exist_ok=True)
            (tests_path / ".gitkeep").touch()

setup_repo()

#%% Create badges -------------------------------------------------------------

def create_badges():

    badges = {}

    # Author
    author_str = "Benoit Dehapiot"
    author_url = urllib.parse.quote(author_str)
    badges["author"] = (
        f"![Author Badge](https://img.shields.io/badge/Author-"
        f"{author_url}-green?"
        f"color=rgb(149%2C157%2C165)&"
        f"labelColor=rgb(50%2C60%2C65)) "
    )

    # License 
    license_info = github.get("license", {})
    license_str = license_info.get(
        "name", "No license information found")
    license_url = urllib.parse.quote(license_str)
    badges["license"] = (
        f"![License Badge](https://img.shields.io/badge/License-"
        f"{license_url}-green?&"
        f"color=rgb(149%2C157%2C165)&"
        f"labelColor=rgb(50%2C60%2C65)) "
    )

    # Fiji
    if config["repo_type"] in ["fiji"]:
        badges["fiji"] = (
            f"![IJM Badge](https://img.shields.io/badge/-"
            f"ImageJ%20Macro-blue?logo=ImageJ&"
            f"logoColor=rgb(149%2C157%2C165)&"
            f"labelColor=rgb(50%2C60%2C65)) "
        )

    # ![Static Badge](https://img.shields.io/badge/Code-ImageJMacro-blue?logo=ImageJ&logoColor=rgb(149%2C157%2C165))


    # Test (GitHub actions)
    if config["repo_type"] in ["python_build", "python_test"]:
        badges["test"] = (
            f"[![Test](https://github.com/{REPO_OWNER}/{REPO_NAME}"
            f"/actions/workflows/test.yml/badge.svg)]"
            f"(https://github.com/{REPO_OWNER}/{REPO_NAME}"
            f"/actions/workflows/test.yml)"
        )

    # Python version(s)
    if "python" in config["repo_type"]:
    
        if config["repo_type"] in ["python_lite", "python_build"]:
            
            python_str = config["python_version"]

        elif config["repo_type"] in ["python_test"]:
            
            python_str = config["tested_python"]
            python_str = python_str.replace("[", "")
            python_str = python_str.replace("]", "")
            python_str = python_str.replace("'", "")
            python_str = python_str.replace(",", " |")

        python_url = urllib.parse.quote(python_str)
        badges["python"] = (
            f"![Python Badge](https://img.shields.io/badge/Python-"
            f"{python_url}-blue?logo=python&"
            f"logoColor=rgb(149%2C157%2C165)&"
            f"labelColor=rgb(50%2C60%2C65)) "
        )
        
    # OS version(s)
    badges["os"] = []
    if config["repo_type"] in ["python_lite", "python_build"]:

        badges["os"].append(
            f"![Windows Badge](https://img.shields.io/badge/Windows-"
            f"latest-blue?logo=windows11&"
            f"logoColor=rgb(149%2C157%2C165)&"
            f"labelColor=rgb(50%2C60%2C65)) "
        )

    if config["repo_type"] in ["python_test"]:
        
        os_name, os_version = [], []
        os_str = config["tested_os"]
        os_str = os_str.replace("[", "")
        os_str = os_str.replace("]", "")
        os_str = os_str.split(", ")
        for item in os_str:
            name, version = item.split("-")
            os_name.append(name)
            os_version.append(version)

        if "ubuntu" in os_name:
            idx = os_name.index("ubuntu")
            badges["os"].append(
                f"![Ubuntu Badge](https://img.shields.io/badge/Ubuntu-"
                f"{os_version[idx]}-blue?logo=ubuntu&"
                f"logoColor=rgb(149%2C157%2C165)&"
                f"labelColor=rgb(50%2C60%2C65)) "
            )
        if "windows" in os_name:
            idx = os_name.index("windows")
            badges["os"].append(
                f"![Windows Badge](https://img.shields.io/badge/Windows-"
                f"{os_version[idx]}-blue?logo=windows11&"
                f"logoColor=rgb(149%2C157%2C165)&"
                f"labelColor=rgb(50%2C60%2C65)) "
            )
        if "macos" in os_name:
            idx = os_name.index("macos")
            badges["os"].append(
                f"![MacOS Badge](https://img.shields.io/badge/MacOS-"
                f"{os_version[idx]}-blue?logo=apple&"
                f"logoColor=rgb(149%2C157%2C165)&"
                f"labelColor=rgb(50%2C60%2C65)) "
            )

    return badges

badges = create_badges()

#%% Get dependencies ----------------------------------------------------------

def get_dependencies():

    dependencies = []
    dependency_list = []
    start_append = False

    # Extract dependencies
    with open(ROOT_PATH / "requirements.txt", "r") as file:
        for line in file:
            line = line.strip()                  
            if start_append and line and not line.startswith("#"):
                dependency_list.append(line)
            if line == "# Project":
                start_append = True            

    # Parse links.yml
    with open(ROOT_PATH / "utils" / "ressources" / "links.yml", "r") as file:
        try:
            links = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)

    for dependency in dependency_list:
        for key, value in links.items():
            if dependency in key:
                dependencies.append(
                    f"* [{dependency}]({links[key]['PyPI']})"
                    )
                
    return dependencies

dependencies = get_dependencies()

#%% Assemble readme -----------------------------------------------------------

def assemble_readme():

    # Get overview
    with open(ROOT_PATH / "utils" / "ressources" / "overview.md", "r") as file:
            overview = file.read()

    # Get instructions
    if "python" in config["repo_type"]:
        with open(ROOT_PATH / "utils" / "ressources" / "instructions_python.md", "r") as file:
            instructions = file.read()
    if "fiji" in config["repo_type"]:
        with open(ROOT_PATH / "utils" / "ressources" / "instructions_fiji.md", "r") as file:
            instructions = file.read()

    with open(ROOT_PATH / "README.md", "w") as file:

        # Badges
        file.write(badges["author"] + "\n")
        file.write(badges["license"] + "\n")
        if "fiji" in config["repo_type"]:
            file.write("\n" + badges["fiji"] + "\n")
        if "python" in config["repo_type"]:
            file.write("\n" + badges["python"] + "\n")
        for badge in badges["os"]:
            file.write(badge + "\n")
        if config["repo_type"] in ["python_test"]:
            file.write("\n" + badges["test"] + "\n")

        # Repo info
        file.write("\n" + f"# {REPO_NAME}" + "\n") 
        file.write("\n" + f"{github['description']}" + "\n")
        file.write("\n" + f"## Overview" + "\n") 
        file.write("\n" + overview + "\n") 

        # Installation
        file.write("\n" + f"## Installation" + "\n") 
        file.write("\n" + instructions + "\n") 

        # Dependencies
        file.write("\n" + f"## Dependencies" + "\n") 
        for dependency in dependencies:
            file.write("\n" + dependency)

assemble_readme()

#%% Replace placeholders ------------------------------------------------------

def replace_placeholders(file_path):
    
    # Read file
    with open(file_path, "r") as file:
        txt = file.read()
    
    # Replace placeholders
    txt = txt.replace("{{ repo_name }}", REPO_NAME)
    txt = txt.replace("{{ env_name }}", ENV_NAME)
    txt = txt.replace("{{ python_version }}", config["python_version"])
    txt = txt.replace("{{ tested_os }}", config["tested_os"])
    txt = txt.replace("{{ tested_python }}", config["tested_python"])
    txt = txt.replace("{{ repo_description }}", github["description"])

    # Update file
    with open(file_path, "w") as file:
        file.write(txt)

replace_placeholders(ROOT_PATH / "README.md")
if config["repo_type"] in ["python_build", "python_test"]:
    replace_placeholders(ROOT_PATH / "setup.cfg")
if config["repo_type"] in ["python_test"]:
    replace_placeholders(ROOT_PATH / ".github" / "workflows" / "test.yml")
