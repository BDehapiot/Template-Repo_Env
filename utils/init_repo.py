#%% Imports -------------------------------------------------------------------

import re
import yaml
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

    # Last commit (seems wrong!)
    try:
        last_commit_str = github[0]['commit']['committer']['date']
    except (KeyError, IndexError):
        last_commit_str = "none"
    last_commit_url = urllib.parse.quote(last_commit_str)
    badges["last_commit"] = (
        f"![Last_commit Badge](https://img.shields.io/badge/Last_commit-"
        f"{last_commit_url}-green?&"
        f"color=rgb(149%2C157%2C165)&"
        f"labelColor=rgb(50%2C60%2C65)) "
    )

    # Python version(s)
    if config["repo_type"] in ["python_lite"]:
        
        python_str = config["python_version"]

    elif config["repo_type"] in ["python_full", "python_build"]:
        
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
    if config["repo_type"] in ["python_full", "python_build"]:
        
        os_name, os_version = [], []
        os_str = config["tested_os"]
        os_str = os_str.replace("[", "")
        os_str = os_str.replace("]", "")
        os_str = os_str.split(", ")
        for item in os_str:
            name, version = item.split("-")
            os_name.append(name)
            os_version.append(version)

        badges["os"] = []
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

#%% Assemble readme -----------------------------------------------------------

def assemble_readme():

    with open(ROOT_PATH / "README.md", "w") as file:
        file.write(badges["python"])
        for badge in badges["os"]:
            file.write(badge)
        file.write(badges["author"])
        file.write(badges["license"])
        file.write(badges["last_commit"])
        

assemble_readme()

# def assemble_readme():
      
#     # 
#     title = f"# {REPO_NAME}"
#     description = f"{github["description"]}"

#     #
#     if config["repo_type"] in ["python_lite", "python_full", "python_build"]:
#         with open(ROOT_PATH / "utils" / "markdown" / "instructions_python.md", "r") as file:
#             instructions = file.read()
#     elif config["repo_type"] == "Fiji":
#         with open(ROOT_PATH / "utils" / "markdown" / "instructions_fiji.md", "r") as file:
#             instructions = file.read()

#     #
#     dependencies = []
#     start_append = False
#     with open(ROOT_PATH / "requirements.txt", "r") as file:
#         for line in file:
#             line = line.strip()
#             if start_append and line and not line.startswith("#"):
#                 dependencies.append("* " + line + "\n")
#             if line == "# Project":
#                 start_append = True
#     dependencies = "".join(dependencies)
    
#     #   
#     with open(ROOT_PATH / "README.md", "w") as file:
#         file.write(python_badge)
#         file.write(license_badge)
#         if config["repo_type"] in ["python_full", "python_build"]:
#             for os_badge in os_badges:
#                 file.write(" " + os_badge)
#         file.write("\n" + title + "\n" + description)
#         file.write("\n\n" + "## Installation" + "\n" + instructions)
#         file.write("\n\n" + "## Dependencies" + "\n" + dependencies)

#     return license

# license = assemble_readme()
# print(license)

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
    with open(file_path.with_stem(file_path.stem + "_copy"), "w") as file:
        file.write(txt)

replace_placeholders(ROOT_PATH / "README.md")
replace_placeholders(ROOT_PATH / "setup.cfg")
replace_placeholders(ROOT_PATH / ".github" / "workflows" / "test.yml")
