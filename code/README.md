# Meteortie Analysis Software
This git repository contains python scripts to analyse meteorite data for my research, which is bound to win me the noble prize.

## Installation
This software isn't installable (yet), but it's always good to describe how to install your software. Some common ways to install python scripts include

`python setup install`

or

`pip install .`

## Data
It is always best to note where your data came from and describe how to use it.

### Australian_Meteorite_Landings.csv
Data downloaded from https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/data/Australian_Metorite_Landings.csv. A truncated version of the data from https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9.

id: NASA meteorite

mass (g): Mass of the meteorite in grams

reclat: Recorded latitude in degrees

reclong: Recorded longitude in degrees

## Running Software
Create analysis plots using:

`python plot_meteorites.py`