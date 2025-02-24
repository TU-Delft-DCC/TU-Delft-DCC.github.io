---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-20

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Software management plan

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
author_2: Aysun Urhan

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - 
# - 

---

Research software plays a crucial role in academic research and has become a key output of many research projects. A software management plan helps to implement best practices during software development and ensures that software is accessible and reusable in the short and longer term. It also contributes to the reproducibility of results and stimulates collaborative work on open-source software for research. 

The Netherlands eScience Center and NWO, the Dutch Research Council, have taken the initiative to form a [working group](https://www.esciencecenter.nl/national-guidelines-for-software-management-plans/) to develop (national) guidelines for software management plans. This working group – composed of five experts in research software, representing different research organizations in the Netherlands, and roles within those organizations – started their work in December 2021.

The initiative resulted in the publication of the [**Practical guide to Software Management Plans**](https://zenodo.org/record/7248877) in October 2022. You can read more about the process leading up to the guide in [this blog](https://blog.esciencecenter.nl/how-to-manage-your-software-327c8ac8a937). The DCC is currently evaluating the adoption of these guidelines for TU Delft research software.

As a introduction to Software Management Plans, TU Delft has created a video:

{{< video https://www.youtube.com/watch?v=5Zy3l4dTJd4 >}}

*"Navigating Research Data and Software: A Practical Guide for PhD Supervisors 2025", TU Delft Library. CC-BY-4.0*

:::{.callout-tip}
The [Intermediate Research Software Development](https://carpentries-incubator.github.io/python-intermediate-development/) course from The Carpentries is a good resource to learn the core principle of intermediate-level software development and best practices collaborating in a team.
:::

## Further reading

* [Software Development Plan](https://doit.software/blog/software-development-plan): A quick start on building software development plans.

* [How to Learn Software Design and Architecture](https://khalilstemmler.com/articles/software-design-architecture/full-stack-software-design): A step-by-step guide to learn software design and architecture, and best practices. 

* [Fundamentals of Software Architecture](https://tudelft.on.worldcat.org/oclc/1129469149): A comprehensive textbook to guide software developers on software architecture, available online.

* [Software Development Life Cycle](https://resources.github.com/software-development/what-is-sdlc/): A guide on how to follow the software development lifecycle (SDLC) systematically, and different SDLC methodologies.

* [Software Architecture - Design and Evaluation](https://www.diva-portal.org/smash/get/diva2:838171/FULLTEXT01.pdf): A detailed research report about software architecture design and evaluation.

### Software management
* [Software Management Overview](https://acqnotes.com/acqnote/careerfields/software-management-overview): An overview of software management and main tasks involved with managing a software.

* [Software Management Plans](https://forschungsdaten.info/praxis-kompakt/english-pages/software-management-plans/): A detailed documentation about software management plans, including up-to-date templates. 

* [Writing Software Management Plans](https://www.software.ac.uk/software-management-plans): A guide from the Software Sustainability Institute on how to write research software management plans.

### Research software sustainability
* [A Framework for Understanding Research Software](https://doi.org/10.5281/zenodo.4988277 ): A proposal for categorizing different types of research software, and a framework for sustaining research software.

### Developing open source software

* [Producing Open Source Software](https://producingoss.com/en/producingoss-letter.pdf): A comprehensive textbook for software managers and developers on how to start running open source projects and maintain them.

### Software Architecture diagrams

C4 model is a popular approach to draw good software architecture diagram that software development teams use to communicate efficiently. It is easy to learn and adopt into existing projects as well as design new projects from scratch. It provides a set of hierarchical abstractions and diagrams to visualize software architecture in a notation independent manner. 

While a marker and a whiteboard is more than enough to get started with the C4 model, the [C4-PlantUML library](https://github.com/plantuml-stdlib/C4-PlantUML) provides an easy-to-understand language to create C4 diagrams with PlantUML. The library is handy with macros, snippets and a VSCode extension.

* [C4 model](https://c4model.com/)

* [C4 model video explanation](https://www.youtube.com/watch?v=x2-rSnhpw0g)

* [C4 model in practice](https://lukemerrett.com/c4-diagrams-as-code-architectural-joy/)
