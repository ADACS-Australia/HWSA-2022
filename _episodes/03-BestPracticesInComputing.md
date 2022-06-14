---
title: "Best Practices In Scientific Computing"
teaching: 30
exercises: 30
questions:
- "What does best practice mean?"
- "What are the top N things to do?"
- "What are the top N things to avoid?"
---
# Best Practices In Scientific Computing
Borrowed and adapted from computer science and software engineering.

- Good code etiquette
  - Efficiency vs clarity
  - Readability
  - Naming things
  - Rule of three
  - KISS
  - 90-90 rule
  - Documentation
  - Testing
  - Optimization
  - Version control

In this lesson we will focus on repetition, version control, testing, documentation, and repetition.

To demonstrate the utility of these topics we'll be working on a common task - analyzing meteorite falls around the world.

# Reading in data
You can download the data with the command:

```
wget https://raw.githubusercontent.com/ADACS-Australia/HWSA-2022/gh-pages/data/Australian_Metorite_Landings.csv
```
{: .language-bash}

You can have a peak inside the csv file with the command:

```
head Australian_Metorite_Landings.csv
```
{: .language-bash}

```
id,mass (g),reclat,reclong
5051,488.1,-33.15639,115.67639
48653,324.0,-31.35,129.19
7743,30.0,-31.66667,152.83333
10033,127.0,-29.46667,151.61667
10120,26000.0,-33.35,146.85833
12264,41730.0,-35.08333,139.91667
16643,330000.0,-26.45,120.36667
16738,8887.5,-40.975,145.6
16766,11300.0,-29.8,141.7
```
{: .output}

From this you can see that we have given you a simple csv that for each metortie has an ID, a mass, and a recorded position in latitude and logitude.
We shall use this csv as an example of how to investigate data, confirm that they are valid and see if we can get any results.

There are few ways that we can read in the this csv in Python. A fairly manual way is using the csv module like so

```
import csv

csv_list = []
# opening the CSV file
with open('Australian_Metorite_Landings.csv', mode ='r') as file:
  # read the CSV file
  csv_reader = csv.reader(file)

  # loop over each line and record it
  for line in csv_reader:
        csv_list.append(line)

# print the first 10 lines
print(csv_list[:10])
```
{: .language-python}

```
[['id', 'mass (g)', 'reclat', 'reclong'], ['5051', '488.1', '-33.15639', '115.67639'], ['48653', '324.0', '-31.35', '129.19'], ['7743', '30.0', '-31.66667', '152.83333'], ['10033', '127.0', '-29.46667', '151.61667'], ['10120', '26000.0', '-33.35', '146.85833'], ['12264', '41730.0', '-35.08333', '139.91667'], ['16643', '330000.0', '-26.45', '120.36667'], ['16738', '8887.5', '-40.975', '145.6'], ['16766', '11300.0', '-29.8', '141.7']]
```
{: .output}

Then if you wanted to get the mean mass you could do this:

```
import numpy as np

all_mass = []
# csv_list[1:] will skip header
for id, mass, lat, long in csv_list[1:]:
    # make sure there is no missing data
    if mass != "":
        # Convert from string to float
        all_mass.append(float(mass))
# Output mean
print(np.mean(all_mass))
```
{: .language-python}

```
80919.38811616955
```
{: .output}

Which is fine but that was a bit of work. Instead we recomend that you learn how to use [pandas](https://pandas.pydata.org/docs/). Pandas makes reading in and inspecting data even easier.

```
import pandas as pd

df = pd.read_csv('Australian_Metorite_Landings.csv')

# Have a look at the data
print("csv data\n--------------------------")
print(df)

# Use pandas to do some quick analysis
print("\npanda describe\n--------------------------")
print(df.describe())
```
{: .language-python}

```
csv data
--------------------------
        id   mass (g)    reclat    reclong
0     5051      488.1 -33.15639  115.67639
1    48653      324.0 -31.35000  129.19000
2     7743       30.0 -31.66667  152.83333
3    10033      127.0 -29.46667  151.61667
4    10120    26000.0 -33.35000  146.85833
..     ...        ...       ...        ...
638  30359      262.5 -32.03333  126.17500
639  30361   132000.0 -14.25000  132.01667
640  30362    40000.0 -31.19167  121.53333
641  30373   118400.0 -29.50000  118.75000
642  30374  3800000.0 -32.10000  117.71667

[643 rows x 4 columns]

panda describe
--------------------------
                 id      mass (g)      reclat     reclong
count    643.000000  6.370000e+02  643.000000  643.000000
mean   19219.513219  8.091939e+04  -30.275400  130.594478
std    14869.941958  1.029442e+06    2.940091    7.655877
min      471.000000  0.000000e+00  -41.500000  114.216670
25%    10136.500000  3.280000e+01  -30.841665  126.587915
50%    15481.000000  1.291000e+02  -30.383330  128.916670
75%    23537.500000  2.426000e+03  -30.086415  132.008335
max    56644.000000  2.400000e+07  -12.263330  152.833330
```
{: .output}

With only a few lines we can load the data and have a quick look. You can see that the count of mass is only 637 out of 643 so pandas has recognised that there is missing mass data and has even calculated a mean mass for us.

## Validating data

One of the best ways to test or validate the data is to plot it in a few different ways to visually inspect it. Let's make a scatter graph of these positions using [matplotlib](https://matplotlib.org/stable/tutorials/index)

```
import matplotlib.pyplot as plt

plt.scatter(df['reclong'], df['reclat'], edgecolors='0')
plt.show()
```
{: .language-python}

That looks vaguely Australia shaped but to be sure lets plot this against a map of Australia to make sure we believe the locations.
Doing this manually would be difficult so, after some Googling, we have found a python module that can do it for you called [Basemap](https://basemaptutorial.readthedocs.io/en/latest/first_map.html)

```
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
# setup map projection.
min_long = 110
max_long = 155
min_lat  = -45
max_lat  = -10
m = Basemap(
    # Lower left corner longitude
    llcrnrlon=min_long,
    # Upper right corner longitude
    urcrnrlon=max_long,
    # Lower left corner latitude
    llcrnrlat=min_lat,
    # Upper right corner latitude
    urcrnrlat=max_lat,
    projection='mill',
)
# Draw in Austrlia and map lines
m.drawcoastlines()
m.fillcontinents()
m.drawparallels(np.arange(-90,90,10),labels=[1,1,0,1])
m.drawmeridians(np.arange(-180,180,10),labels=[1,1,0,1])

# Convert your data to the Basemap coordinates and add it to the plot
x, y = m(df['reclong'], df['reclat'])
plt.scatter(x, y, edgecolors='0')
plt.show()
```
{: .language-python}


We could also have a look at the distribution of masses using the [seaborn](https://seaborn.pydata.org/) module like so:

```
import seaborn as sns

#create density plot of data
sns.kdeplot(df['mass (g)'])
plt.show()

# O that looked a bit silly lets make it a log plot
sns.kdeplot(np.log(df['mass (g)']))
plt.show()
```
{: .language-python}

## Creating a resuable script

This is looking great but before we go any further we should make this into a function as part of a script so it's easier to rerun.
Functions makes it easier to reuse parts of your code which prevents you from repeating yourself and making mistakes.
Lets combine all of our analysis into a single script (and lets make the scatter plot different sizes based on the mass) like so


```
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_metorite_analysis(
    df,
    # optional arguments
    min_long=110,
    max_long=155,
    min_lat=-45,
    max_lat=-10,
):
    log_mass = np.log(df['mass (g)'])

    fig = plt.figure()
    # setup map projection.
    m = Basemap(
        # Lower left corner longitude
        llcrnrlon=min_long,
        # Upper right corner longitude
        urcrnrlon=max_long,
        # Lower left corner latitude
        llcrnrlat=min_lat,
        # Upper right corner latitude
        urcrnrlat=max_lat,
        projection='mill',
    )
    # Draw in Austrlia and map lines
    m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90,90,10),labels=[1,1,0,1])
    m.drawmeridians(np.arange(-180,180,10),labels=[1,1,0,1])

    # Convert your data to the Basemap coordinates and add it to the plot
    x, y = m(df['reclong'], df['reclat'])
    # Make the scatter dots size propotional to the mass
    plt.scatter(x, y, edgecolors='0', s=log_mass)
    plt.show()

    sns.kdeplot(np.log(df['mass (g)']))
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('Australian_Metorite_Landings.csv')
    plot_metorite_analysis(df)
```
{: .language-python}

Now you have a script that is easy to rerun if you want to recreate the plot and if anyone asks you how you generated the results you can show them your script so you can go through the steps one by one to confirm their validity.

It's a good thing you made your script repeatable because someone points out that your mass distribution looks wrong. After some investigation you notice that [np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html) is a natural log not base 10! Luckily you can fix that quickly. You function can also easily be used for future data sets.
Ooops np.log is a natural log!

lets vesion control this

make it git

document it so it's clear

readme describing the input data

make sure you have a final script so you can recreate these plots easily

Make a script for both processing and plotting

This prevents you being unsure how you got your results


## Version control
Don't loose track of your working versions.
Online backup is a bonus but not essential.
Collaborative work is nice but not essential.
merge/rebase/branch are nice but not essential.

## Testing
Testing is not hard, and we already do it so let's just embrace that.

Anything that you do to validate your work is testing.
- making plots
- writing to STDOUT
- checking known cases

Automation is nice, but not essential for testing.

Think about how you will validate your work as you develop your data collection and methodology.

## Documentation
Many levels:
- README.md
- `--help` or docstrings (Python)
- userguid.pdf
- myproject.readthedocs.io

Consider the audience:
- users
- developers
- you in 6 months time

## Avoiding repetition
Repeated code means repeated opportunity for mistakes and inconsistencies.
