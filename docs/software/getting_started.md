---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-29

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-08-29

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Getting started

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
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
#categories: 
# - 
# - 

---

## What is research software?
Research software can be thought of as evolving through stages, reflecting how code evolves alongside the research process:

- **Exploratory stage:** Code is written to test ideas, prototype methods, or quickly generate results. The focus is flexibility and speed rather than maintainability.
- **Sharable stage:** When research outputs need to be communicated, validated, or reproduced, the software must reach a “good enough” state. It should be documented, versioned, and structured so that others can rerun or inspect the work.
- **Sustainable stage:** Some research software grows beyond its original project to become a (critical) dependency for others. At this point, higher standards are needed, approaching the quality expectations of production software.

Alongside these levels of maturity, researchers also rely on "software in research" (e.g., operating systems, libraries, dependencies) that may not have been created with research in mind but are essential for computation. For reproducibility, all of these components (exploratory scripts, research software, external dependencies, and documentation) must be identified, described, and made accessible following the [FAIR principles for research software](./fair_software/fair.md).

## Why does research software matter?
Code is now as central to research as data or publications. Sharing and reusing it ensures that scientific work doesn’t stop at a single experiment but can be built upon, adapted, and tested by others. Even quick, exploratory scripts have value when preserved and explained. And when research software matures into tools used across a field, the benefits multiply by providing a foundation for whole communities. 

Journals and funders are also raising expectations. They increasingly expect code to be documented, reproducible, and accessible, both to validate findings and to support new discoveries. By treating research software as something that can grow from rough sketches into sustainable tools, researchers can improve the reliability of their own work while contributing lasting resources for others.

## What can you find?
This series of guides looks at research software through that lens of growth and maturity. You’ll find:

- Practical advice on version control, environment management, and modular design.
- Common pitfalls, including missing documentation, tricky dependencies, and reproducibility issues.
- Guidance on what “good enough” looks like at different stages, and how to raise the quality of your code when it becomes important to do so.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
The DCC guides don't provide a full learning path (see [About the guides](../about.md)), but the following resources can help you get started with research software development:

- [The Turing Way](https://book.the-turing-way.org/) - A handbook to reproducible, ethical and collaborative data science.
- [Research Software Quality Toolkit for Sciences (RSQKit)](https://everse.software/RSQKit/) - Best practices, tools, and resources for improving research software quality.

For hands-on training in essential skills:

- [Software Carpentry](https://software-carpentry.org/) - Entry-level workshops on Python, version control, and the UNIX shell.
- [Building Better Research Software](https://carpentries-incubator.github.io/better-research-software/) - Follow-up to Software Carpentry, focusing on research software best practices.
- [Intermediate Research Software Development with Python](https://carpentries-incubator.github.io/python-intermediate-development/) - Covers more advanced Python topics for research software.

For additional workshops, see [Courses & Workshops](../resources/courses.md).
:::