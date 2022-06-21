---
title: Setup
---

## Software required:
- Git
    - [MacOS](https://git-scm.com/download/mac)
    - [Linux](https://git-scm.com/download/linux)
    - [Windows](https://git-scm.com/download/win)
- A terminal
  - MocOS/Linux, a bash terminal is available by default
  - Windows, use either [WSL](https://docs.microsoft.com/en-us/windows/wsl/) if you have it installed, or gitbash (above)
- A python environment
  - python3 (ideally 3.8+)
  - Install packages using a package manager such as conda or pip (only one, not both, see below)
    - matplotlib, basemap, numpy, pandas
- A python pacakge manager (just one)
  - Conda (large but complete)
    - [AnyOs](https://www.anaconda.com/products/distribution)
  - Miniconda (minimal, sufficient for our needs)
    - [MacOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
    - [Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
    - [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
  - See [this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda) if you are having trouble deciding between conda and miniconda
  - pip (barebones, also sufficient)
    - Almost always bundled with python, but see [here](https://pip.pypa.io/en/stable/installation/) if `pip` does nothing for you.
- Online tools
  - An account on [trello](https://trello.com/en) (free)
  - [sqliteonline](https://sqliteonline.com/) (no account needed)


## Conda environment
If you are using Conda to manage your python modules we have set up a Conda python environment that will install all dependencies for you.
After installing Conda, run the following commands:

Download:
```
wget https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/environment.yaml
# or
curl -O https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/environment.yaml
```
{: .language-bash}

Then install and activate
```
conda env create --name hwsa2022 --file environment.yaml
conda activate hwsa2022
```
{: .language-bash}

## Pip environment
If you are using pip to manage your python modules we have an environment set up for you.
Create an activate a new python environment (optional, but recommended)
~~~
python3 -m venv hwsa2022
source hwsa2022/bin/activate
~~~
{: .language-bash}

Download:
```
wget https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/requirements.txt
# or
curl -O https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/requirements.txt
```
{: .language-bash}

Install required libraries
~~~
pip install -r requirements.txt
~~~
{: .language-bash}

## Help
Please ensure that you have access to the above tools prior to starting this workshop.
If you need help to install or access any of these tools, please email one of the facilitators, or chat to us on the Thursday before the workshop and we can sit down with you to get your system setup.

{% include links.md %}
