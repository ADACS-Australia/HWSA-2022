---
title: "Bonus Content"
teaching: 0
exercises: 0
questions:
- "What else is there?"
---

## Automation
### Aliases
A basic form of automation is the use of aliases.
The goal here is to save you a bunch of keyboard or mouse clicks.
Some common examples:
~~~
# long list all files
alias ll='ls -al'

# open ds9 and press about 20 buttons to get the interface set up just the way I like
alias ds9='~/Software/ds9/ds9 -scalelims -0.2 1 -tile -cmap cubehelix0 -lock frame wcs -lock scale yes -lock colorbar yes -lock crosshair wcs'

# run stilts and topcat and not have to bother with the java invocation
alias stilts='java -jar ~/Software/topcat/topcat-full.jar -stilts'
alias topcat='java -jar ~/Software/topcat/topcat-full.jar'

# activate my favorite python3 environment
alias py3='source ~/.py3/bin/activate'
~~~
{: .language-bash}

## Structured data storage
CSV files are great but can be cumbersome to work with when they become large or when you have multiple files with related data.
An alternative is to store your data as tables in a database, where you can make explicit links between multiple tables, and make use of the SQL language to select, filter, order, and extract the data that you need.
Some commercial (but free) solutions include [PostgreSQL](https://www.postgresql.org/) and [MySQL](https://www.mysql.com/), but these require a fair bit of system admin to get setup and work with.
A great lightweight middle-ground is [SQLite](https://www.sqlite.org/index.html), which provides the core functionality of a relational database but without all the security, authentication, and sys admin requirements of a commercial solution.
See this [carpentries](https://swcarpentry.github.io/sql-novice-survey/) lesson for an introduction do databases using SQLite.