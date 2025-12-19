---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-26

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Code documentation

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Elviss Dvinskis
author_2: Maurits Kok


# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
  - Software
  - Documentation
  - Python
  - MATLAB
  - R

---

Good code documentation acts as the bridge between developers and users by clearly explaining the functionality and rationale behind your code. Whether you’re writing inline comments or structured documentation, the key is to make your code readable, maintainable, and accessible to both current and future contributors.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa hashtag >}} Python projects
Code comments, docstrings, API reference.

::: {.learn-more}
[Learn more »](./python_documentation.md)
:::
:::

::: {.feature}
### {{< fa percent >}} MATLAB projects
Documenting MATLAB projects.

::: {.learn-more}
[Learn more »](./matlab_documentation.md)
:::
:::

::: {.feature}
### {{< fa hashtag >}} R projects
Documenting R projects with `roxygen2`.

::: {.learn-more}
[Learn more »](./r_documentation.md)
:::
:::

:::
:::

### Types of source code documentation

1. **Code comments** are inline annotations meant for developers who read or maintain the source code. They are useful for clarifying complex parts of code, noting why certain decisions were made in specific blocks or lines.

:::{.callout-tip appearance="simple" icon="false"}
## Good code comments should:
- explain parts that are not intuitive from the code itself
- explain the purpose of a piece of code (why over how)
- need to be kept up-to-date as wrong comments are not caught through testing
- **not** replace readable and structured code
- **not** turn old code into commented zombie code (see [code smells](../../code_quality/code_smells/dead_code.md))
- **not** repeat in natural language what is written in your code
:::

2. **Docstrings** provide a description of the function, class, or module that follows immediately after it is defined. It should contain all the relevant information needed for using them, rather than explaining how the code works. Docstrings are available to users without looking at the source code (as opposed to comments) and can be used to generate user documentation. 
