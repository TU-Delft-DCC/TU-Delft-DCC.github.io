---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-03-07

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: README

# Short description of the document, will be used in the listing
description: Writing a good README
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
author_2: Elviss Dvinskis

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
    - documentation
    - README
---

A **README** file is essential for your software project as it helps users understand the purpose of your project, how to install and use it, and how to contribute. While the specific content of a README can vary from project to project, a good README should always include the following sections:

1. The purpose of the project.
2. How to cite the project.
3. Installation and usage instructions.
4. The terms under which the software is distributed (license).

## 1. Project purpose
Clearly explain the purpose of your project, including its motivation and objectives. This section should serve as an introductory overview, helping users and contributors understand the essence of your project. 

Consider adding:

- Background information
- Comparison with alternatives, highlighting what sets your project apart
- Links to related references or documentation

## 2. How to cite
If you want users to cite your project when they use it, provide a citation in this section, referring to a publication or DOI of the software.

For more information about citing the project, see the [Citation guide](./citation.md).

## 3. Installation and usage
This section should explain the steps needed to set up and use the software. Before installation, users must be aware of any prerequisites or dependencies that are required. This can include specific versions of programming languages, libraries, operating systems, data, and hardware. 


#### **Installation steps**
Provide a step-by-step guide for installation. This can involve downloading the software from a repository, compiling code, or using a package manager. Consider using package managers, such as `pip` or `conda`, to simplify the installation.

**Example:** The [`scikit-learn` GitHub repository](https://github.com/scikit-learn/scikit-learn?tab=readme-ov-file#installation) provides a good example of the *Installation* section of a README.

#### **Usage**
You can include the simplest possible usage example directly in the README and provide more complex examples in additional files or links.

**Example:** The [`TensorFlow` GitHub repository](https://github.com/tensorflow/tensorflow?tab=readme-ov-file#install) gives a small usage sample after installation instructions and provides a link with additional examples and tutorials. 

## 4. License
Your README should specify the licensing terms. For more information, see the [License guide](./license.md).


::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip

It is recommended to write README's in markdown (`README.md`) formatting and placed in the project's top-level directory. If you find your README is becoming too long, consider incorporating [additional documentation files](https://www.makeareadme.com/#more-documentation) instead of omitting important details.
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Make a README - README 101](https://www.makeareadme.com)
- [Making READMEs readable](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md)
:::