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
- "Clean your data"
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
- cleaned data
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
![DataProcessing]({{ page.root }}{% link fig/DataProcessing.svg %}){: width='400'}

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

![StructredUnstructredData](http://intellspot.com/wp-content/uploads/2020/04/Structured-vs-unstructured-data-an-infographic-1024x724.png){: width='400'}

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
> 
{: .exercise}

## Data cleaning

Pandas example here

## Data storage and access

Pandas <-> csv, Pandas <-> sqlite examples here
