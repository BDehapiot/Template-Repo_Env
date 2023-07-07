## Install

<!-- #### 1 - Download the GitHub repository: 
![Static Badge](https://img.shields.io/badge/%3C%3E%20Code%20-%20blue?color=rgb(30%2C%20135%2C%2060))
- Download the GitHub repository by clicking the green `<> Code` button and select `Download ZIP`
- Unzip the file to a known location
- Open your terminal and move to this location

#### 2 - Download & install miniconda:  
https://docs.conda.io/en/latest/miniconda.html

![Windows Badge](https://img.shields.io/badge/Windows-blue?logo=windows11&logoColor=rgb(149%2C%20157%2C%20165)&labelColor=rgb(50%2C%2060%2C%2065)&color=rgb(50%2C%2060%2C%2065))  
Download the last installer and run the .exe file  

![MacOS Badge](https://img.shields.io/badge/MacOS-blue?logo=apple&logoColor=rgb(149%2C%20157%2C%20165)&labelColor=rgb(50%2C%2060%2C%2065)&color=rgb(50%2C%2060%2C%2065))  
Download the last installer (bash) and run this command line in your terminal (type terminal in the Launchpad or Spotlight search)  
```bash
bash file.sh
```

![Static Badge](https://img.shields.io/badge/Ubuntu-blue?logo=ubuntu&logoColor=rgb(149%2C%20157%2C%20165)&labelColor=rgb(50%2C%2060%2C%2065)&color=rgb(50%2C%2060%2C%2065))  
Download the last installer (bash) and run the following command in the terminal (ctrl + alt + T)
```bash
chmod +x file.sh && ./file.sh
``` -->

<details>

<summary>Windows</summary>

#### 1 - Download the GitHub repository: 
![Static Badge](https://img.shields.io/badge/%3C%3E%20Code%20-%20blue?color=rgb(30%2C%20135%2C%2060))
- Download the GitHub repository by clicking the green `<> Code` button and select `Download ZIP`
- Unzip the file to a known location (e.g. `C:\Users\YourUsername\Desktop`)

#### 2 - Install miniconda: 
- Download the last installer and run the `.exe` file
- Use default options (it can be modified later anyway)

#### 3 - Setup conda environment: 
- Navigate to your Anaconda3 folder using the start menu and run `Anaconda Powershell Prompt`  
- Your prompt should look like this:
 ```bash
(base) PS C:\Users\YourUsername>
```
- `(base)` at the beginning of the prompt means that you are in your base conda environment
- You can move to the GitHub repository (change path if ) 
 ```bash
cd Desktop/{repo_name}-main
```
- Now your prompt should look like this:
 ```bash
(base) PS C:\Users\YourUsername>\Desktop\{repo_name}-main
```
- Now create a new environment: 
 ```bash
conda create -n {env_name} python={python_version} pip
```
- Activate the newly created environment: 
 ```bash
conda activate {env_name}
```
  
</details>

<details>

  <summary>MacOS</summary>
  
</details>

<details>

  <summary>Linux</summary>
  
</details>

