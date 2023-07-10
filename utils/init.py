#%% Imports -------------------------------------------------------------------

import yaml
import json
import requests
from pathlib import Path
from jinja2 import Template

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path('.').resolve()
REPO_OWNER = "BDehapiot"
REPO_NAME = ROOT_PATH.name
REPO_METADATA = requests.get(
    f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'
    ).json()
ENV_NAME = REPO_NAME.split('_', 1)[1] if '_' in REPO_NAME else REPO_NAME

#%%

# Read config.yml
with open(ROOT_PATH / "utils" / "config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Format repository
if config['repo_type'] == 'lite':
    pass
if config['repo_type'] == 'full':
    pass
if config['repo_type'] == 'full-build':
    pass

# Replace placeholders
with open(ROOT_PATH / 'README_copy.md', 'r') as file:
    template_text = file.read()
template = Template(template_text)
rendered_text = template.render(
    repo_name=REPO_NAME,
    env_name=ENV_NAME,
    python_version=config['python_version'],
    )


# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# install("numpy")  # for example, to install numpy

# def update_readme():

#     # Read the template
#     with open(ROOT_PATH / 'README_copy.md', 'r') as file:
#         template_text = file.read()

#     template = Template(template_text)

#     rendered_text = template.render(repo_name=repo_name, env_name=env_name, python_version=python_version)

#     # Write the result to README.md
#     with open(ROOT_PATH / 'README_copy.md', 'w') as file:
#         file.write(rendered_text)
# %%
