---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-24

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Workflow management

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Aysun Urhan

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Aysun Urhan
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Aysun Urhan

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - project management
# - github
# - issues
# - project board

---

Workflow management for research software is the practice of organizing series of tasks related to research, such as how scientific code, data and experiments are developed, executed and shared to ensure reproducible, collaborative and efficient research. An example research workflow might include data processing, model training or running simulations, as well as recording and publishing the results. The main objective is not only about making the code run successfully, but about making it **reproducible**, **trackable** and **adaptable**.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa solid circle-question >}} Why workflow management is important in research
Research software development differs from traditional software development. Workflow management is crucial to: 

- Keep **track** of the development progress
- Ensure **reproducible** results
- Allow **experiments** with variable inputs or settings with minimal overhead
- **Reduce errors** when running large or complex pipelines
- Facilitate **collaborative research** as others can easily join the project and understand its structure
:::

## Workflow management tools
A workflow management tool (or simply a workflow manager) is a tool to help researchers build and manage computational workflows in a structured and reproducible way. 

- These tools assist in defining, organizing, executing and tracking sequences of computational steps which are typically represented as a series of commands or scripts. 
- By explicitly recording how data is processed, including the parameters and software environments used, workflow managers make it easier to replicate analyses, debug issues, and share work with collaborators. 
- This level of structure helps avoid the all-too-common situation where a result is produced but the exact steps to generate it are lost or unclear.

The **bioinformatics** field is a prominent example where workflow management has become essential since research relies heavily on pipelines to analyze genomic data; usually you perform a sequence of analyses on several files. Hence, there are many workflow managers niche to the field. 

- But workflow management is a general need in many other applications involving data to support reproducible analysis. 
- **Any research field** involving data analysis, simulations, or modeling can benefit from adopting workflow managers. 
- Fields like **climate science**, **neuroscience**, **physics**, and even **digital humanities** face similar challenges of organizing code, managing data dependencies, and ensuring that computational results are reproducible. 
- As scientific computing becomes more complex and collaborative, workflow management is emerging as a foundational practice to support open science, reproducibility, and long-term maintainability of research software.

### Some examples of workflow managers
Workflow managers come in many forms, from simple scripting approaches to full-featured platforms with graphical user interfaces (GUIs) or domain-specific languages (DSLs). Here are some examples, categorized by interface and complexity:

- **Script-based or Classic Tools** <br>
  - Shell scripts / Python scripts (*"good old scripts"*)
  - [Make](https://en.wikipedia.org/wiki/Make_(software)) – a traditional build automation tool still used in research for its simplicity
- **Code-Based Workflow Managers** <br>
  These systems are primarily driven by writing code in general-purpose languages (like Python), often using functions, decorators, or object-oriented patterns:
  - [Snakemake](https://snakemake.readthedocs.io/en/stable/) (Python-based)
  - [Nextflow](https://www.nextflow.io) (DSL based on Groovy)
  - [Airflow](https://airflow.apache.org) (Python-based)
  - [Ruffus](http://www.ruffus.org.uk), [SciPipe](https://scipipe.org), and many others

  Snakemake, Nextflow, and Airflow are examples of DSL-based workflow managers that allow users to define workflows in a concise and human-readable syntax.

- **GUI-Based Workflow Managers** <br>
  These tools provide a visual interface for building and executing workflows, making them ideal for users with little or no programming background:
  - [Galaxy](https://galaxyproject.org)
  - [KNIME](https://www.knime.com)

::: {.callout-tip appearance="simple" icon="true"}
## Choose the right workflow manager for you

- **DSLs** can make workflows easier to read, document, and debug - especially for complex pipelines.
- **GUI-based workflow systems**, with drag-and-drop interfaces and visual feedback, are often the most accessible option for beginners or interdisciplinary teams.
:::

## Snakemake: a Python-esque make 
Snakemake essentially builds on the implicit wildcard rule approach of Make, and it extends its capabilities by allowing the use of Python in a pipeline. Just like Make, its goal is to produce a set of requested output files based on predefined rules and steps. 

Although it was originally developed to create scalable bioinformatics and genomics pipelines, it can be generalized to other applications as well. It has become a standard tool in reproducible research; being cited more than [12 times per week in 2023](https://indico.cern.ch/event/1441041/), and has been used extensively in scientific publications in several different fields. Currently, it has [over one million downloads on Conda](https://anaconda.org/bioconda/snakemake).

### Noteworthy features of Snakemake
- If Python and Make were to have a baby.
- You can describe workflows using a **human readable**, **Python based language**.
- It has **built-in caching**: if some steps of your workflow have already been run, Snakemake can recognize that and avoid rerunning the same analyses.
- It can accommodate both **serial and parallel jobs** since each "work units" in a workflow can be run independently of one another.
- It makes **debugging** easier since it keeps track of all files generated, you can identify which steps in your workflow have failed.
- **Integration with conda** allows you to define conda environments for both the whole workflow and individual steps. 
- You can incorporate tools or methods written in different scripting languages.
- Workflows can be scaled to **server, cluster, grid and cloud environments**, without modifying the workflow itself.
- It has an **active user and developer base** in mainly bioinformatics, and other scientific research community. It's development is driven by the needs of scientists and their needs of reproducible research.

## What about Airflow?
Airflow has become the go-to tool for building data pipelines, it started at Airbnb and was later adopted by the Apache project. Being backed by the Apache project, and a growing community of contributors, it's the most popular workflow manager in software engineering.

- {{< fa thumbs-up >}} **Pros:**
  - It is the most popular choice of workflow management system in software engineering.
  - It has a bigger community support and hence more detailed tutorials and documentation.
  - It offers more features, especially enterprise integrations used in industry.
  - It integrates well with databases, APIs, cloud services and data warehouse like Google BigQuery, AWS S3 and Snowflake.
  - It is more production friendly with built-in scheduling and monitoring features.

- {{< fa thumbs-down >}} **Cons:**
  - It has a complex infrastructure and a steeper learning curve.
  - It is more difficult to share pipelines between different environments.
  - It lacks native support for conda.
  - It has a more convoluted approach to parallel computation.
  - It has limited support for HPC.

### A summary of workflow management tools discussed

| **Feature**                  | **Snakemake**                 | **Nextflow**                  | **Airflow**                    |
|------------------------------|-------------------------------|-------------------------------|--------------------------------|
| **Target Audience**          | Scientists, researchers       | Bioinformaticians, scientists | Data engineers, DevOps         |
| **Ease of Use**              | High                          | Medium                        | Low                            |
| **Reproducibility Focus**    | Strong                        | Medium                        | Low                            |
| **HPC Support**              | Excellent                     | Good                          | Minimal                        |
| **Cloud-Native Support**     | Moderate                      | Strong                        | Excellent                      |
| **Community**                | Scientific community          | Bioinformatics                | Data engineering, cloud-native |

::: {.callout-important appearance="simple" icon="true"}
## Snakemake vs Airflow

Snakemake is a gentle introduction to workflow management for most researchers. Airflow produces well defined production level workflows that are meant to be run continually, and hence Snakemake is much better suited for the needs of researchers who want to run reproducible analyses for a particular project or an application. 
:::

::: {.callout-note collapse="true"}
## Sidenote: What is special about bioinformatics workflows?

In bioinformatics, a workflow is a collection of steps run in series to transform raw data input to processed results (figures, insights, decisions etc.). Each step can be made up of different tools, programs, parameters, databases and dependencies/requirements. 

There are 3 main reasons why bioinformatics workflows are different than those data engineering workflows in the industry:

**1. Differences in data type, shape and scale**

- Bioinformatics datasets are typically very large and come from various sources (DNA sequences, RNA sequencing, proteomics data, imaging data)
- Different data types have different structures and different preprocessing/analysis needs

**2. Differences in programs and tooling**

- Bioinformatics pipelines often involve numerous steps with intricate dependencies
- Different steps use different, specialized tools 
- Open source, highly specialized tools that are not meant to be integrated natively, there are no software packages or standalone platforms to run analyses from start to finish 
- New algorithms, tools and reference databases are updated frequently, researchers need flexible pipelines that can be adapted easily
- Many bioinformatics tasks and tools are computationally expensive (genome assembly, alignment, sequence search) and require HPC

**3. Community support behind bioinformatics workflow managers and open source software**

- Field of bioinformatics has a strong emphasis on open science, reproducible and transparent research. All of which are achieved using workflow managers 

:::

### Other fields that already use or can benefit from Snakemake
- [Large, parallel deep learning experiments using Snakemake](https://waterdata.usgs.gov/blog/snakemake-for-ml-experiments): The USGS demonstrates how Snakemake can be used to perform deep learning experiments on environmental data.
- [Workflow managers in high-energy physics - Enhancing analyses with Snakemake: Physics and high-energy particle research:](https://archive.fosdem.org/2024/events/attachments/fosdem-2024-3415-workflow-managers-in-high-energy-physics-enhancing-analyses-with-snakemake/slides/22450/FOSDEM-HEP-workflow-managers_hcQO9j3.pdf) Large scale HEP experiments with complex dependencies on cloud.
- [Neuroscience:](https://www.nature.com/articles/s41598-024-77615-z) Using Snakemake to process and analyze MRI data.
- [Ecology and evolutionary research:](https://doi.org/10.1111/2041-210X.14113) Article outlining the specific benefits of using Snakemake to manage data analysis workflows in ecology and evolutionary research, and demonstrating its use through case studies.
- Earth and Climate Science: Preprocessing large datasets from climate models (NetCDF format) for regional climate projections.
- Automating preprocessing EEG/MEG data, MRI and fMRI data analysis and predictive modeling for thousands of neuroimaging files.
- Chemistry: Running large-scale molecular dynamics simulations with different parameter combinations and collecting results in a reproducible framework.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Further reading
- [Awesome pipeline repository](https://github.com/pditommaso/awesome-pipeline): a curated list of tools for creating pipelines.
- [Snakemake documentation](https://snakemake.readthedocs.io/en/stable/): an extensive documentation that includes in depth tutorials and edge cases.
- [An Introduction to Snakemake with R for Economics](https://lachlandeer.github.io/snakemake-econ-r-tutorial/index.html)
- [Sustainable data analysis with Snakemake](https://doi.org/10.12688/f1000research.29032.2): A general overview article about Snakemake published in *F1000Research*.
- [A review of bioinformatic pipeline frameworks.](https://doi.org/10.1093/bib/bbw020): A review article published in *Briefings in Bioinformatics*, focused on Bioinformatics pipelines.
- [Airflow vs Snakemake](https://learn.flowdeploy.com/blog/airflow-vs-snakemake): A direct comparison between Airflow and Snakemake for data pipelines, while promoting FlowDeploy.
- [Why are bioinformatics workflows different?](https://www.deeporigin.com/blog/why-are-bioinformatics-workflows-different)
:::