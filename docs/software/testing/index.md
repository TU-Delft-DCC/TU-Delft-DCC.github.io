---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-03-11

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
title: Software testing

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of software testing practices and strategies
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
  - Software
  - Testing

---

When you're writing software -- especially for research -- it's important to make sure your programs work as expected. Testing is like a safety net: it helps you catch mistakes early and keeps your code reliable as you add new features or make changes. In research software, tests are even more crucial because they help ensure that your results are accurate and that others can reproduce your work. Beyond detecting bugs early, it is an investment in the quality and long-term maintainability of your codebase. 


::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa route >}} Approach to testing
A guide to help you get started with testing your software.

::: {.learn-more}
[Learn more »](./strategies.md)
:::
:::

::: {.feature}
### {{< fa cubes >}} Test types
Different types of tests to ensure your software works as expected.

::: {.learn-more}
[Learn more »](./test_types.md)
:::
:::

::: {.feature}
### {{< fa magnifying-glass >}} Additional concepts
More concepts to help you write better tests.

::: {.learn-more}
[Learn more »](./intermediate.md)
:::
:::

::: {.feature}
### {{< fa flask >}} Python testing
Testing your Python code.

::: {.learn-more}
[Learn more »](./python.md)
:::
:::

::: {.feature}
### {{< fa flask >}} MATLAB testing
Testing your MATLAB code.

::: {.learn-more}
[Learn more »](./matlab.md)
:::
:::

::: {.feature}
### {{< fa flask >}} R testing
Testing your R code.

::: {.learn-more}
[Learn more »](./r_test.md)
:::
:::

:::
:::


::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb>}}Recommended courses
- [The Turing Way - Testing](https://book.the-turing-way.org/reproducible-research/testing)
- [CodeRefinery - Lesson on testing](https://coderefinery.github.io/testing/motivation/)
- [Software Carpentry - Testing and Continuous Integration with Python](https://carpentries-incubator.github.io/python-testing/)
- [R Packages - Testing](https://r-pkgs.org/tests.html)
:::