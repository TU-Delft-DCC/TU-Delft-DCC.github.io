---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-14

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

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
categories: 
  - Software
  - Environments
  - Dependencies
  - MATLAB

---

MATLAB does not use virtual environments like Python, where isolated environments manage dependencies. Instead, MATLAB handles project-specific dependencies using:

- **Toolboxes** - Pre-packaged libraries that must be licensed and available
- [**MATLAB projects**](https://mathworks.com/help/matlab/projects.html) - A feature that manages paths and environments for a project
- **Path management** - Manually adding paths to the MATLAB search path with `addpath` and `rmpath`

To check dependencies in a project:

- Use [**`requiredfilesandproducts`**](https://nl.mathworks.com/help/matlab/ref/matlab.codetools.requiredfilesandproducts.html) to identify required MathWorks toolboxes for a script of function.
- Use the the [**Dependency Analyzer**](https://nl.mathworks.com/help/matlab/matlab_prog/analyze-project-dependencies.html) to detect file dependencies.


### Custom MATLAB Dependency Manager

To offer a solution for managing dependencies in MATLAB through a dependency file, we have created a Dependency Manager: 

{{< fa up-right-from-square >}} [**DependencyManager**](https://github.com/TU-Delft-DCC/matlab_dependency_manager)
