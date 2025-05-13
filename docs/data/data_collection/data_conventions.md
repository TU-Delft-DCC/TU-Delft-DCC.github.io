---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-07

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Data conventions

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
author_2: Raul Ortiz Merino

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - data
 - conventions

---

By adhering to domain-aligned data conventions, you can enhance the quality and reproducibility of your work, promote collaboration, data sharing and reuse. While flexibility exists to accommodate the specific needs of your research project, it is important to establish a consistent framework for data collection and management. This section outlines some key considerations for data conventions, including naming conventions, folder structure, and file standards.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Learn more
Again, we would like to refer you to modules from the RDM 101 course. Please explore:

- [RDM 101 - Module 2 - Data within the research workflow](https://tu-delft-library.github.io/rdm101-book/modules/module2.html#data-within-the-research-workflow)
- [RDM 101 - Module 3 - FAIR data principles and their main elements](https://tu-delft-library.github.io/rdm101-book/modules/module3.html) 

for more information on this topic.
:::


## Data conventions

Establishing consistent naming conventions and metadata practices for your data files is essential for long-term project maintainability. Similarly, as mentioned in the [Project structure](../../software/development_workflow/project_structure.md) guide in the *Research Software* section, some essential principles apply, like:

- use descriptive, concise and consistent names
- avoid special characters and spaces (instead use underscores `_` or hyphens `-`)
- follow [`ISO 8601`](https://www.iso.org/iso-8601-date-and-time-format.html) date formatting (`YYYY-MM-DD`)
- the order matters - order elements in the name from least to most specific
- include versioning in the name (where applicable)

However, the specific conventions you choose should align with the needs of your research project, collaborators, and established practices within your field.

## Folder structure

Maintaining a consistent folder structure across your research group and project phases prevents confusion, reduces errors in data analysis, and significantly improves research reproducibility. Remember that folder structure should complement your file naming (data) conventions to create a cohesive data organization system. Some practices to consider include:

- Use a consistent and descriptive naming convention for folders, similar to file naming conventions
- Avoid using spaces or special characters in folder names
- Create a hierarchical structure that moves from general to specific, making navigation intuitive
- Establish consistent naming patterns across all levels of your folder hierarchy
- Separate raw and processed data into distinct folders to preserve original data integrity
- Limit folder nesting to 3-5 levels to prevent excessive complexity
- Group related files into logical categories rather than creating folders for individual files
- Document your folder structure in your data management plan for reference
- For time-series or versioned data, consider incorporating date-based folder organization
- Consider adding a README file in your `data/` folder to provide an overview of the folder structure and its contents

## File standards

Files commonly use standardised formats depending on their knowledge domain, and/or the platfrom through which they are made available. For example, [FASTA](https://www.bioinformatics.nl/tools/crab_fasta.html) format files are widely used in bioinformatics workflows for sequence alignment, database searches, genome assembly and more. Several major biological databases and tooling use and support the FASTA format, like [NCBI](https://www.ncbi.nlm.nih.gov), [EMBL-EBI](https://www.ebi.ac.uk), and [UniProt](https://www.uniprot.org/).

In the field of geosciences, the [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) format is widely used for array-oriented scientific data. It is particularly useful for storing multidimensional data such as temperature, pressure, and humidity in a single file. NetCDF files are self-describing and can be compressed to save space, making them ideal for large datasets.

In the field of engineering, data is often stored in formats such as [HDF5](https://www.hdfgroup.org/solutions/hdf5/). It is widely used for storing large amounts of numerical data and are supported by many programming languages and software tools.

In addition, 4TU.ResearchData has a list of [preferred file formats](https://data.4tu.nl/s/documents/Preferred_File_Formats_2019.pdf), and they have a [data collection policy](https://data.4tu.nl/s/docs/data-collection-policy.pdf) that outlines the preferred file formats for data submission.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Further reading
- [The FAIR Guiding Principles for scientific data management and stewardship](https://doi.org/10.1038/sdata.2016.18)
:::