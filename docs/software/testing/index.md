---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
#date: YYYY-MM-DD

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Software testing

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: Name Surname
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
categories: 
- testing 

---

Testing plays an important role in guaranteeing the ongoing reliability and stability of software systems. Beyond merely detecting bugs, it represents a strategic investment in the quality and long-term maintainability of your codebase. By testing your software, you safeguard against unforeseen complications arising from code modifications. For research software, systematic testing can ensure the reliability, accuracy, and scientific validity of the software, thereby enhancing the quality  and reproducibility of research findings.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa file-code >}} Getting started
Conventions and guidelines used to write and format code.

::: {.learn-more}
[Learn more »](./code_style.md)
:::
:::

::: {.feature}
### {{< fa file-code >}} Intermediate concepts
Conventions and guidelines used to write and format code.

::: {.learn-more}
[Learn more »](./intermediate.md)
:::
:::

::: {.feature}
### {{< fa wrench >}} Python testing
Restructuring existing code without changing its external behavior.

::: {.learn-more}
[Learn more »](./python.md)
:::
:::

::: {.feature}
### {{< fa wrench >}} MATLAB testing
Restructuring existing code without changing its external behavior.

::: {.learn-more}
[Learn more »](./matlab.md)
:::
:::

:::
:::



::: {.callout-tip title="Recommended resources"}
- [The Turing Way - Testing](https://book.the-turing-way.org/reproducible-research/testing)
- [CodeRefinery - Lesson on testing](https://coderefinery.github.io/testing/motivation/)
- [Software Carpentry - Testing and Continuous Integration with Python](https://carpentries-incubator.github.io/python-testing/)
- [R Packages - Testing](https://r-pkgs.org/tests.html)
:::
