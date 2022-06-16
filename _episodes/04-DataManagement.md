---
title: "Managing Data"
teaching: 30
exercises: 30
questions:
- "Why do I need to manage data?"
- "How do I manage different types of data?"
- "How do I store and access structured data?"
- "How do I store and access unstructured data?"
keypoints:
- "Invest time in cleaning and transforming your data"
- "Meta data gives context and makes your data easier to understand"
- "How and where you store your data is important"
---

# Managing Data
All of our research is fundamentally reliant on data so it's important to understand the different types of data, how to store them, and how to work with them.
In this lesson we'll learn all the above!

## Types of data
Fundamentally computers store data as 0s and 1s, representing floats, integers, boolean, or character data types.
However this is *not* what we are going to talk about here.
Here we are more concerned with a higher level of abstraction, which includes the following data types:
- raw data 
  - as it comes directly from a sensor or data source
  - contains signal + noise
  - format and quality is highly dependent on the data source
- clean data
  - has bad/invalid records removed or flagged
  - has been converted to a format which is usable by your analysis or processing tools
- transformed data
  - useful features have been identified
  - low level aggregation has been applied
  - instrument/sensor/model dependent effects have been removed
- reduced data
  - has been modeled
  - has been processed into a different form such as images or a time series
- published data
  - the highest level of abstraction/aggregation of your data
  - often represented as tables or figures

The following describes a generic data processing workflow
![DataProcessing]({{ page.root }}{% link fig/DataProcessing.svg %}){: width='800'}

> ## Discussion
> In your groups have a look at the different types of data and stages of the data processing workflow.
> Think about:
> - Where do you get your data from?
>   - Are there more than one source of data?
> - How do you keep track of which data is in which stage of processing?
> - When you publish your work, which data products do you want to keep and which can be deleted?
> 
> Record some notes in the shared document.
{: .discussion}

We can classify data by the processing stage as was done above, but also in an orthogonal dimension of how the data is organized.
The two most general considerations here are either structured or unstructured data.

![StructredUnstructredData](http://intellspot.com/wp-content/uploads/2020/04/Structured-vs-unstructured-data-an-infographic-1024x724.png){: width='800'}

The way that we can store and access data depends on how it's structured.

### Structured data
One of the easiest ways to store structured data are in one or more tables.
The tables themselves can be stored as `.csv`, `.fits`, or `.vot` tables which can be read by many astronomy software tools such as [topcat](http://www.star.bris.ac.uk/~mbt/topcat/).
[Google sheets](https://www.google.com.au/sheets/about/), [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel), or [LibreOffice Calc](https://www.libreoffice.org/discover/calc/) can also be beneficial for storing structured data, particularly because they allow you to do some data exploration, cleaning, filtering, and analysis within the file itself.

When your data volumes become large, or you find yourself needing to have multiple related tables, then you probably want to start exploring databases as a storage option.
See the [Bonus Content]({{page.root}}{% link _episodes/06-BonusContent.md %}#structured-data-storage)

### Unstructured data
Unstructured data cannot be aggregated or combined into a single data format due to their lack of common structure.
In such cases it is often best to make use of a regular directory/file structure to store the individual files in a way that can be navigated easily.
A well planned directory/file structure it is very useful to store meta-data about each of the files that you are storing.
For example you could have:
- A `README.md` file in the root directory that describes the directory/file structure
- A `metadata.csv` file that maps the location of a file to some high level information such as the file format, the date the file was collected, the processing stage of the data, or the version of the file.

> ## Exercise
> - Download example data form [TODO](link)
> - For each of the files decide what stage of processing they are in, wether they are structured or unstructured data
> - Make a plan for how you would store and manage this data
> - Note in the shared document what you have decided for at least one of the files
{: .challenge}

## Data cleaning
In the previous lesson we worked with a file `Australian_Meteorite_Landings.csv`.
For your benefit this had already been cleaned to remove invalid entries, attributes that we didn't need, and entries that were not relevant.

Let's now start with the original data set and go through the cleaning process.

~~~
wget -O Meteorite_Landings.csv https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD
# or
curl -o Meteorite_Landings_curl.csv -O https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD
~~~
{: .language bash}

Now we'll explore the data set using pandas.

> ## View the raw data
> Using your viewer of choice, have a look at the csv file that we just downloaded.
> Think about and discuss:
> - Are there any missing data?
> - What can be done about the missing data?
> - Are there any columns that are not useful?
>
> Note in our shared document which tool you used to inspect the data, and one that you would take to clean this data.
> 
{: .challenge}

> ## Solution with pandas
> ~~~
> import pandas as pd
> df = pd.read_csv('Meteorite_Landings.csv')
> print("Quick look of data")
> print(df)
> print("Summary of data")
> print(df.describe())
> ~~~
> {: .language-python}
> ~~~
> Quick look of data
>              name     id nametype              recclass  mass (g)   fall    year    > reclat    reclong             GeoLocation
> 0          Aachen      1    Valid                    L5      21.0   Fell  1880.0  50.> 77500    6.08333       (50.775, 6.08333)
> 1          Aarhus      2    Valid                    H6     720.0   Fell  1951.0  56.> 18333   10.23333    (56.18333, 10.23333)
> 2            Abee      6    Valid                   EH4  107000.0   Fell  1952.0  54.> 21667 -113.00000      (54.21667, -113.0)
> 3        Acapulco     10    Valid           Acapulcoite    1914.0   Fell  1976.0  16.> 88333  -99.90000       (16.88333, -99.9)
> 4         Achiras    370    Valid                    L6     780.0   Fell  1902.0 -33.> 16667  -64.95000     (-33.16667, -64.95)
> ...           ...    ...      ...                   ...       ...    ...     ...       ..> .        ...                     ...
> 45711  Zillah 002  31356    Valid               Eucrite     172.0  Found  1990.0  29.> 03700   17.01850       (29.037, 17.0185)
> 45712      Zinder  30409    Valid  Pallasite, ungrouped      46.0  Found  1999.0  13.> 78333    8.96667     (13.78333, 8.96667)
> 45713        Zlin  30410    Valid                    H4       3.3  Found  1939.0  49.> 25000   17.66667       (49.25, 17.66667)
> 45714   Zubkovsky  31357    Valid                    L6    2167.0  Found  2003.0  49.> 78917   41.50460     (49.78917, 41.5046)
> 45715  Zulu Queen  30414    Valid                  L3.7     200.0  Found  1976.0  33.> 98333 -115.68333  (33.98333, -115.68333)
> 
> [45716 rows x 10 columns]
> Summary of data
>                  id      mass (g)          year        reclat       reclong
> count  45716.000000  4.558500e+04  45425.000000  38401.000000  38401.000000
> mean   26889.735104  1.327808e+04   1991.828817    -39.122580     61.074319
> std    16860.683030  5.749889e+05     25.052766     46.378511     80.647298
> min        1.000000  0.000000e+00    860.000000    -87.366670   -165.433330
> 25%    12688.750000  7.200000e+00   1987.000000    -76.714240      0.000000
> 50%    24261.500000  3.260000e+01   1998.000000    -71.500000     35.666670
> 75%    40656.750000  2.026000e+02   2003.000000      0.000000    157.166670
> max    57458.000000  6.000000e+07   2101.000000     81.166670    354.473330
> ~~~
> {: .output}
{: .solution}

> ## solution with bash
> ~~~
> head Meteorite_Landings.csv
> ~~~
> {: .language-bash}
> ~~~
> name,id,nametype,recclass,mass (g),fall,year,reclat,reclong,GeoLocation
> Aachen,1,Valid,L5,21,Fell,1880,50.775000,6.083330,"(50.775, 6.08333)"
> Aarhus,2,Valid,H6,720,Fell,1951,56.183330,10.233330,"(56.18333, 10.23333)"
> Abee,6,Valid,EH4,107000,Fell,1952,54.216670,-113.000000,"(54.21667, -113.0)"
> Acapulco,10,Valid,Acapulcoite,1914,Fell,1976,16.883330,-99.900000,"(16.88333, -99.9)"
> Achiras,370,Valid,L6,780,Fell,1902,-33.166670,-64.950000,"(-33.16667, -64.95)"
> Adhi Kot,379,Valid,EH4,4239,Fell,1919,32.100000,71.800000,"(32.1, 71.8)"
> Adzhi-Bogdo (stone),390,Valid,LL3-6,910,Fell,1949,44.833330,95.166670,"(44.83333, 95.> 16667)"
> Agen,392,Valid,H5,30000,Fell,1814,44.216670,0.616670,"(44.21667, 0.61667)"
> Aguada,398,Valid,L6,1620,Fell,1930,-31.600000,-65.233330,"(-31.6, -65.23333)"
> ~~~
> {: .output}
> ~~~
> wc Meteorite_Landings.csv
> ~~~
> {: .language-bash}
> ~~~
>   45717  166894 3952161 Meteorite_Landings.csv
> ~~~
> {: .output}
{: .solution}

You may have noticed when inspecting the file above, that the header names are occasionally useful, but don't do a good job of explaining what the data represent.
For example:
- what does the "rec" in reclat/reclong represent?
- Why do some meteors have blank reclat/reclon, while others have (0,0)?
  - Did someone found a meteorite at the Greenwich observatory?
- There are many meteorites with the same reclat/reclong, why is this?
- What does recclass represent?

Here is where we need to think about the meta-data attached to this table.
We need context (how/why the table was created), and also a description of what the data represent.
If we go to the NASA website they have a description of the column data, but it's not so helpful:

![MeteoriteColumnDescriptions]({{page.root}}{% link fig/MeteoriteColumnDescriptions.png %}){: .width=400}

Wuh-wah!
The only column with a description is the one that was most obvious.
Not only that, but the data type listed for the columns is incorrect in many cases.
For example, id, reclat, and reclat are listed as being "plain text" but they are clearly numeric (int, and floats), while "year" is listed as being "date and time".

Enough complaining, lets start fixing.

> ## Challenge
>  We want to plot all the Australian meteorites, with a measured mass value, and a nametype of "Valid"
> - Using pandas, load the meteorite dataset
> - Delete the geolocation column as it's a duplicate of the reclat/reclong columns
> - Select all rows with a non-zero and non-null mass value
>   - Count the rows and record this number
>   - Delete these rows
> - Repeat the above for:
>   - rows with a `reclat`/`reclong` that are identically 0,0
>   - rows with a blank `reclat`/`reclong`
>   - rows with `nametype` that is not "Valid"
> - Delete the `nametype` column as it's now just has a single value for all rows
> - Choose a bounding box in lat/long for Australia (don't forget Tassie!)
> - Select, count, and delete all rows that are outside of this bounding box
> - Save our new dataframe as a `.csv` file
> - Run our previously created script on this file and view the results
{: .challenge}

## Data storage and access

Pandas <-> csv, Pandas <-> sqlite examples here
