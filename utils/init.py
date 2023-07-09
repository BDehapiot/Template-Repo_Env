#%% Imports -------------------------------------------------------------------

import yaml
from pathlib import Path
from jinja2 import Template

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path('.').resolve()
REPO_NAME = ROOT_PATH.name

#%%

# # Read congig.yml
# with open(ROOT_PATH / "config.yml", 'r') as stream:
#     try:
#         config = yaml.safe_load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)

# if config['repo_type'] == 'lite':
#     Path(ROOT_PATH / "data").mkdir(parents=True, exist_ok=True)
#     Path(ROOT_PATH / "data" / ".gitkeep").touch()
#     pass

# if config['repo_type'] == 'full':
#     pass
# if config['repo_type'] == 'full-build':
#     pass

# 

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
