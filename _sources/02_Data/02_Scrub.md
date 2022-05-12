# Scrubing / Cleaning data
This phase of the process should require the most time and effort. 
> **As with Obtaining data, herein a little command line background and simple scripting can be of great utility.** 

**Skills required**
- Scripting language: Python, R, SAS
- Data Wrangling Tools: Python Pandas, R

**Advanced skills**
- Distributed Processing: Hadoop, Map Reduce / Spark

Scrubbing data is the least sexy part of the analysis process, but often one that yields the greatest benefits.Whether provided by an experimentalist with missing data and inconsistent labels, or via a website with an awkward choice of data formatting, there will almost always be some amount of data cleaning (or scrubbing) necessary before analysis of these data is possible. 

**Objective:**
- The most basic form of scrubbing data is just making sure that it’s read cleanly, stripped of extraneous characters, and parsed into a usable format. Unfortunately, many data sets are complex and messy.
- Examine the data: understand every feature you’re working with, identify errors, missing values, and corrupt records
- Clean the data: throw away, replace, and/or fill missing values/errors

**Sed**, **awk**, **grep** (linux command line programs) are enough for most small tasks, and using either Perl or Python should be good enough for the rest. Additional skills which may come to play are familiarity with databases, including their syntax for representing data (e.g., JSON, above) and for querying databases.
 A simple analysis of clean data can be more productive than a complex analysis of noisy and irregular data.

### An example
 Imagine that you decide to look at something as simple as the geographic distribution of twitter users by self-reported location in their profile. Easy, right? Even people living in the same place may use different text to represent it. Values for people who live in New York City contain “New York, NY”, “NYC”, “New York City”, “Manhattan, NY”, and even more fanciful things like “The Big Apple”. This could be an entire blog post (and will!), but how do you disambiguate it?. [Example](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.64.8557)

