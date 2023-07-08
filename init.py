#%% Imports -------------------------------------------------------------------

import yaml
from pathlib import Path
from jinja2 import Template

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path('.').resolve()
REPO_NAME = ROOT_PATH.name

#%%

with open(ROOT_PATH / "config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
    

# def update_placeholder_readme():

#     # Read the template
#     with open(ROOT_PATH / 'README_copy.md', 'r') as file:
#         template_text = file.read()

#     template = Template(template_text)

#     rendered_text = template.render(repo_name=repo_name, env_name=env_name, python_version=python_version)

#     # Write the result to README.md
#     with open(ROOT_PATH / 'README_copy.md', 'w') as file:
#         file.write(rendered_text)
# %%
