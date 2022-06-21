---
title: Setup
---

Software required:
- Git
    - [OSX](https://git-scm.com/download/mac)
    - [Linux](https://git-scm.com/download/linux)
    - [Windows](https://git-scm.com/download/win)
- A terminal
  - OSX/Linux, a bash terminal is available by default
  - Windows, use either [WSL](https://docs.microsoft.com/en-us/windows/wsl/) if you have it installed, or gitbash (above)
- Conda
    - [OSX](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
    - [Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
    - [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- Online tools
  - An account on [trello](https://trello.com/en) (free)

We have set up a conda python environment that will install all dependencies for you. After installing Conda, run the following commands

Download:
```
wget https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/environment.yaml
# or
curl -O https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/files/environment.yaml
```
Then install and activate
```
conda env create --name hwsa2022 --file environment.yaml
conda activate hwsa2022
```


Please ensure that you have access to the above tools prior to starting this workshop.
If you need help to install or access any of these tools, please email one of the facilitators, or chat to us on the Thursday before the workshop and we can sit down with you to get your system setup.

{% include links.md %}
