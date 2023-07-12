![Author Badge](https://img.shields.io/badge/Author-Benoit%20Dehapiot-green?color=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65)) 
![License Badge](https://img.shields.io/badge/License-GNU%20General%20Public%20License%20v3.0-green?&color=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65)) 

![Python Badge](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65)) 
![Windows Badge](https://img.shields.io/badge/Windows-latest-blue?logo=windows11&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65)) 

# Template-Repo_Env

Template repository for Python-based projects

## Overview

## Installation

<details> <summary>Windows</summary>

### 1 - Download the GitHub repository: 
![Static Badge](https://img.shields.io/badge/%20Code%20-%20blue?color=rgb(30%2C%20135%2C%2060))
- Download the GitHub repository by clicking the green `Code` button and select `Download ZIP`
- Unzip the file to a known location (e.g. `C:\Users\YourUsername\Desktop`)

### 2 - Install miniconda: 
https://docs.conda.io/en/latest/miniconda.html
- Download the latest installer from the official website (link above) and run the `.exe` file
- Accept default options (it can be modified later)

### 3 - Setup conda environment: 
- Navigate to your Anaconda3 folder using the start menu and run `Anaconda Powershell Prompt`  
- Your prompt should look like this:
 ```bash
(base) PS C:\Users\YourUsername>
```
- `(base)` at the beginning of the prompt means that you are in your base conda environment
- Navigate to the GitHub repository using the `cd` command: 
 ```bash
cd Desktop/{{ repo_name }}-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) PS C:\Users\YourUsername>\Desktop\{{ repo_name }}-main
```
- Create a new environment: 
 ```bash
conda create -n {{ env_name }} python={{ python_version }} pip
```
- Activate your newly created environment:
 ```bash
conda activate {{ env_name }}
```
- Your prompt should now start with `({{ env_name }})`
- Finally, install all project dependencies using `pip`: 
 ```bash
pip install -r requirements.txt
```
<hr style=\"border-top: 1px\">
</details>

<details> <summary>MacOS</summary>

### 1 - Download the GitHub repository: 
![Static Badge](https://img.shields.io/badge/%20Code%20-%20blue?color=rgb(30%2C%20135%2C%2060))
- Download the GitHub repository by clicking the green `Code` button and select `Download ZIP`
- Unzip the file to a known location (e.g. `~/Desktop`)

### 2 - Install miniconda:
https://docs.conda.io/en/latest/miniconda.html
- Download the latest installer (bash) from the official website (link above) 
- Open your terminal (typing 'terminal' in `Launchpad` or `Spotlight search`)
- Your prompt should look like this:
 ```bash
YourUsername@MacBook-Pro ~ %
```
- Navigate to the directory where the downloaded Miniconda script is located (most likely your `Downloads` folder).
 ```bash
cd ~/Downloads
```
- Run the script using the following `bash` command followed by the name of the `.sh` you downloaded (change file name accordingly):
 ```bash
bash Miniconda3-latest-MacOSX-x86_64.sh
```
- Follow the Terminal prompts to complete the installation and accept default options (it can be modified later)

### 3 - Setup conda environment: 
- You should now read the following prompt on your terminal (close and open if needed):
 ```bash
(base) YourUsername@MacBook-Pro ~ %
```
- `(base)` at the beginning of the prompt means that you are in your base conda environment
- Navigate to the GitHub repository using the `cd` command: 
 ```bash
cd Desktop/{{ repo_name }}-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) YourUsername@MacBook-Pro {{ repo_name }}-main %
```
- Create a new environment: 
 ```bash
conda create -n {{ env_name }} python={{ python_version }} pip
```
- Activate your newly created environment:
 ```bash
conda activate {{ env_name }}
```
- Your prompt should now start with `({{ env_name }})`
- Finally, install all project dependencies using `pip`: 
 ```bash
pip install -r requirements.txt
```
<hr style=\"border-top: 1px\">
</details>

<details> <summary>Linux</summary>

### 1 - Download the GitHub repository: 
![Static Badge](https://img.shields.io/badge/%20Code%20-%20blue?color=rgb(30%2C%20135%2C%2060))
- Download the GitHub repository by clicking the green `Code` button and select `Download ZIP`
- Unzip the file to a known location (e.g. `~/Desktop`)
  
### 2 - Install miniconda:
https://docs.conda.io/en/latest/miniconda.html
- Download the latest installer (bash) from the official website (link above) 
- Open your terminal (Ctrl+Alt+T)
- Your prompt should look like this:
 ```bash
YourUsername@YourMachine:~$
```
- Navigate to the directory where the downloaded Miniconda script is located (most likely your `Downloads` folder).
 ```bash
cd ~/Downloads
```
- Run the script using the following `bash` command followed by the name of the `.sh` you downloaded (change file name accordingly):
 ```bash
bash Miniconda3-latest-Linux-x86_64.sh
```
- Follow the Terminal prompts to complete the installation and accept default options (it can be modified later)

### 3 - Setup conda environment: 
- You should now read the following prompt on your terminal (close and open if needed):
 ```bash
(base) YourUsername@YourMachine:~$
```
- `(base)` at the beginning of the prompt means that you are in your base conda environment
- Navigate to the GitHub repository using the `cd` command: 
 ```bash
cd Desktop/{{ repo_name }}-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) YourUsername@YourMachine:~/Desktop/{{ repo_name }}-main$
```
- Create a new environment: 
 ```bash
conda create -n {{ env_name }} python={{ python_version }} pip
```
- Activate your newly created environment:
 ```bash
conda activate {{ env_name }}
```
- Your prompt should now start with `({{ env_name }})`
- Finally, install all project dependencies using `pip`: 
 ```bash
pip install -r requirements.txt
```

<hr style=\"border-top: 1px\">
</details>

## Dependencies

* numpy
* scipy
* pandas
* scikit-image
* matplotlib
* joblib

* numpy [![PyPI logo](https://github.com/BDehapiot/Template-Repo_Env/utils/img/pypi.svg)](https://pypi.org/project/numpy/)