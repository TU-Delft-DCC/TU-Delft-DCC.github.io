---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-04

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
title: Packaging

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
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
  - Software
  - Package
  - Python
  - R

---

Packaging allows developers to bundle their code into a format that is easily installable and manageable across different environments. By creating a package/library, you ensure that all necessary components, including dependencies and configuration files, are included in a single unit, simplifying the installation process for users. Here you can find how to package your Python or R projects for distribution.


::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa box-open >}} Create a Python package
Bundle your Python project.

::: {.learn-more}
[Learn more »](./packaging_python.md)
:::
:::

::: {.feature}
### {{< fa box-open >}} Create an R package
Bundle your R project.

::: {.learn-more}
[Learn more »](./packaging_r.md)
:::
:::

:::
:::