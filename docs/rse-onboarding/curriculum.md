---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2026-04-22

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2026-04-22

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
#title: Title of the document

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Raul Ortiz Merino
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Raul Ortiz Merino
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Raul Ortiz Merino

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - 
# - 

---

# DCC curriculum

## Skill matrix
RSE-like positions are still relatively new and are therefore lacking a standardized profile across the Dutch universities. As a starting point for ourselves, we are in the process of compiling a curriculum for RSEs. In conjunction, we are composing a set of digital competency levels for a TU Delft researcher in a [Skill Matrix](https://docs.google.com/document/d/1STgSYulUI57BQEvDi4lXxaxfCmG3MrXIA49M5Nisq-4/edit?usp=sharing). 

## UFO profiles
The UFO (University Job Classification) profiles are the official profiles for positions in higher education in the Netherlands. The profiles are used to determine the salary scale of a position as well as the accompanying competences. 

For example, the position of the Research Data Engineer (RDE) is not yet included in the UFO profiles. Instead, the position is officially a combination of the profiles of a Researcher and of a Data Steward. Ongoing discussions are taking place to define the role of the RDE. The position of RSE is currently defined by the UFO profile "ICT developer". A national taskforce, led by the TU Delft DCC coordinator, is currently working on a new UFO profile for RSE-like positions.

- [UFO Profile ICT developer](../images/ufo_ict_developer.pdf)
- [UFO Profile Data Steward](../images/ufo_data_steward.pdf)
- [UFO Profile Researcher](../images/ufo_researcher.pdf)

## General competences for all DCC team members
- Version control with git
- GitHub/GitLab/BitBucket/Azure
- Unix shell (bash)
- Proficiency in a programming language (Python, R, Matlab, C++)
- Dependency management (conda, pip, maven, npm, ...)
- SSH and remote computing
- TU Delft storage solutions
- Data and software archiving (Zenodo and 4TU.ResearchData)
- FAIR principles for data and software

### Soft skills
- Project management
- Teaching (Carpentries instructor certification)
- Mentoring / coaching
- Consultancy
- Community engagement (presentations)

## RSE specific competences
### Need to know
- Good proficiency in a programming language
- Proficiency in a second programming language
- Software development workflows (agile, gitflow, trunk based development, test driven development, ...)
- Continuous integration (GitHub Actions / Gitlab runners)
- Containerization (Docker, Singularity)
- Documentation (sphinx, jupyterbook, GitHub pages, readthedocs)
- Research software quality (modular coding, security, reuseability, reproducibility, ...)
- Software architecture design principles and patterns
- [Software Management Plan](https://zenodo.org/records/7589725)
- [TU Delft Software (open) Licenses ](https://filelist.tudelft.nl/TUDelft/Over_TU_Delft/Strategie/TU%20Delft%20Research%20Software%20Guidelines.pdf)


### Useful to know
- Basics of Machine Learning (pytorch, tensorflow, scikit-learn)
- GUI development (PyQt, Tkinter, Matlab)
- Webdevelopment (Django, flask)
- Cloud (AWS, Azure)
- HPC (SLURM, MPL)
- Data processing and analysis (images, netcdf, hdf5, ndarrays, ...)
- Performance optimization (CPU, GPU)

## Data Manager specific competences

### Need to know 
- [Data Management Plan (DMP)](https://dmponline.tudelft.nl/?perform_check=false)
- [TUD Research Data Management Framework Policy](https://zenodo.org/record/4088123) 
- [TUD Guidelines on Research Software](https://zenodo.org/record/4629635)
- [RDM good rules and practices](https://tu-delft-library.github.io/rdm101-book/intro.html)
- Building reproducible data workflows 
- Storing, managing, archiving, and sharing data ([Essentials 4 Data Support](https://danstraining.moodlecloud.com/course/view.php?id=11))
- Definition of personal data and GDPR rules ([TU Delft Human Research Ethics](https://www.tudelft.nl/en/about-tu-delft/strategy/integrity-policy/human-research-ethics))
- Documentation (sphinx, jupyterbook, GitHub pages, readthedocs, Quarto)
- Data(type) processing and analysis (images, netcdf, hdf5, ndarrays, ...)
- [FAIR principles](https://www.nature.com/articles/sdata201618)


### Good to know
- LAMP servers (Linux Apache MySQL Python)
- Database initialisation and management (SQLite, MySQL, PostgreSQL) 
- DVA (Data Version Control)
- GUI/ Web/ Dashboard development (Django, flask, Shiny)
- Setting up servers (FTP, REST API)
- Workflow management (Snakemake/ Apache Airflow/ targets)
- [Electronic Lab Notebooks](https://www.tudelft.nl/library/research-data-management/r/beheer/electronic-lab-notebooks)
- [Open Science and open publishing](https://online-learning.tudelft.nl/courses/open-science-sharing-your-research-with-the-world/)
- [Data Protection](https://www.tudelft.nl/en/privacy-security)