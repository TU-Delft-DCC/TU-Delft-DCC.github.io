---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2024-11-14

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

Although the specific content of a `README` can vary from project to project, several sections are recommended because they address fundamental aspects that are relevant to most projects.

You should ensure that your README addresses the following:

1. The purpose of the project is explained.
2. You have described how to install, use, and develop the code.
3. You have explained the licensing terms for the project.
4. Information is provided on how to reach out to you, ask questions, or contribute.

## Description
Although explaining the purpose might sound self-explanatory, it is important to clearly explain the motivations and objectives of your project. This section should serve as an introductory overview that informs potential users and contributors about the essence of your project. 

Provide background information and include links to any references that someone might not be familiar with. If there are alternatives to your project, this is the place to outline what sets your project apart.

## Installation and usage
This section should detail the steps needed to set up the software in their environment.

Before installation, users must be aware of any prerequisites or dependencies required. This can include specific versions of programming languages, libraries, operating systems, and hardware. It is recommended to make use of a dependency manager such as pip or conda for easy and reproducible installation.

After listing the dependencies, describe the installation process step-by-step. This might involve downloading the software from a repository, compiling code, or using a package manager.

**Example:** The [`scikit-learn` GitHub repository](https://github.com/scikit-learn/scikit-learn?tab=readme-ov-file#installation) provides a good example of the *Installation* section of a README.

You can include the simplest possible usage example directly in the README and provide more complex examples in additional files or links.

**Example:** The [`TensorFlow` GitHub repository](https://github.com/tensorflow/tensorflow?tab=readme-ov-file#install) gives a small usage sample after installation instructions and provides a link with additional examples and tutorials. 

It is recommended to write READMEs in markdown formatting and they should be placed in the top-level directory of your project. It is better that your README is on the side of too much information than too little. If you find your README is becoming too extensive, think about incorporating [additional forms of documentation](https://www.makeareadme.com/#more-documentation) instead of omitting important details.

::: {.callout-note} 
## **Further reading**

- [Make a README - README 101](https://www.makeareadme.com)
- [Making READMEs readable](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md)
:::