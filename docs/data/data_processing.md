---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-06

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Data processing

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: Name Surname
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - data processing
 - version control

--- 

Data processing is a broad term and is often conflated with related terms. It typically includes steps like data cleaning and data transformation. Some workflows may extend this to preliminary analysis, though visualizations are generally considered a separate stage. The term data wrangling is frequently used interchangeably with early processing stages. The specific steps involved can vary depending on the type of data and the goals of the analysis.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Learn more
We would like to refer you to the [Gather/Create & Analyse](https://phdsupervisors.tudl.tudelft.nl/phase/gather-create-analyse/) section of the *TU Delft Navigating Research Data and Software: A Practical Guide for PhD Supervisors* guide for more information.
:::

## Data versioning

Data versioning is the process of assigning unique version numbers to different iterations of a dataset. This practice is important when working with machine learning models, as it allows to track changes made to the data over time and ensure that the correct version of the data is used for training and testing. Data versioning can also help with reproducibility, because it allows to recreate previous versions of the data and compare results across different iterations. 

There are a couple of techniques and tools for data versioning. For example, Git is typically used to track source code and software versions, but is not well-suited for large datasets. However, Git LFS (Large File Storage) can be used to manage large files in a Git repository. Other tools like DVC (Data Version Control) are specifically designed for data versioning and can be used to track changes to datasets and models over time. DVC integrates with Git and allows to version control data files, models, and experiments in a way that is similar to how Git works for source code.

### DVC

DVC has very comprehensive documentation, tutorials and videos available, most of the resources are available on their [homepage](https://dvc.org/doc). It covers how to get started with data versioning, how to integrate it with Git, and how to use DVC with different cloud storage providers (e.g. AWS S3).