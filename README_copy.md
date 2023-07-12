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
cd Desktop/Template-Repo_Env-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) PS C:\Users\YourUsername>\Desktop\Template-Repo_Env-main
```
- Create a new environment: 
 ```bash
conda create -n Env python=3.11 pip
```
- Activate your newly created environment:
 ```bash
conda activate Env
```
- Your prompt should now start with `(Env)`
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
cd Desktop/Template-Repo_Env-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) YourUsername@MacBook-Pro Template-Repo_Env-main %
```
- Create a new environment: 
 ```bash
conda create -n Env python=3.11 pip
```
- Activate your newly created environment:
 ```bash
conda activate Env
```
- Your prompt should now start with `(Env)`
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
cd Desktop/Template-Repo_Env-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) YourUsername@YourMachine:~/Desktop/Template-Repo_Env-main$
```
- Create a new environment: 
 ```bash
conda create -n Env python=3.11 pip
```
- Activate your newly created environment:
 ```bash
conda activate Env
```
- Your prompt should now start with `(Env)`
- Finally, install all project dependencies using `pip`: 
 ```bash
pip install -r requirements.txt
```

<hr style=\"border-top: 1px\">
</details>

## Dependencies

* numpy <span style='font-size: 0.75em;'>[home](https://numpy.org/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/numpy/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/numpy/numpy)</span>
* scipy <span style='font-size: 0.75em;'>[home](https://scipy.org/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/scipy/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/scipy/scipy)</span>
* pandas <span style='font-size: 0.75em;'>[home](https://pandas.pydata.org/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/pandas/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/pandas-dev/pandas)</span>
* scikit-image <span style='font-size: 0.75em;'>[home](https://scikit-image.org/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/scikit-image/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/scikit-image/scikit-image)</span>
* matplotlib <span style='font-size: 0.75em;'>[home](https://matplotlib.org/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/matplotlib/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/matplotlib/matplotlib)</span>
* joblib <span style='font-size: 0.75em;'>[home](https://joblib.readthedocs.io/en/stable/)</span> <span style='font-size: 0.75em;'>[PyPI](https://pypi.org/project/joblib/)</span> <span style='font-size: 0.75em;'>[GitHub](https://github.com/joblib/joblib)</span>