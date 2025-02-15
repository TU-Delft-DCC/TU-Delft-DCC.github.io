---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-14

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Environment and dependency management in MATLAB

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
author_2: Elviss Dvinskis

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
# - matlab
# - environments
# - dependencies

---

MATLAB does not use virtual environments in the same sense as Python, but it allows for setting up paths and toolboxes that act similarly by organizing and encapsulating project-specific functions and scripts. Dependency management in MATLAB often involves ensuring the correct toolboxes are licensed and available, and using MATLAB's Project feature to manage and share paths and environments with others.

MATLAB toolbox requirements can be found with the function [**`requiredfilesandproducts`**](https://nl.mathworks.com/help/matlab/ref/matlab.codetools.requiredfilesandproducts.html) or with the [**Dependency Analyzer**](https://nl.mathworks.com/help/matlab/matlab_prog/analyze-project-dependencies.html).