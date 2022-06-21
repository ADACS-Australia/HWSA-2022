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
- A python environment
  - python3 (ideally 3.8+)
  - matplotlib, basemap, numpy, pandas
  - Install via conda or pip (see below)
- Online tools
  - An account on [trello](https://trello.com/en) (free)


## Pip environment
Create an activate a new python environment (optional, but recommended)
~~~
python3 -m venv hwsa2022
source hwsa2022/bin/activate
~~~
{: .language-bash}

Install required libraries
~~~
pip install -r requirements.txt
~~~
{: .language-bash}


Please ensure that you have access to the above tools prior to starting this workshop.
If you need help to install or access any of these tools, please email one of the facilitators, or chat to us on the Thursday before the workshop and we can sit down with you to get your system setup.

{% include links.md %}
