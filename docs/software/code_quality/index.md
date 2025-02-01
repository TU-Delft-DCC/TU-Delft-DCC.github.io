---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
date: 2025/01/31

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Code quality

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of code quality tools and services
hide-description: true

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
#categories: 
# - 
# - 

---

>"Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?"
>
> **Brian W. Kernighan**

The quality of your research software plays a crucial role in its reliability, maintainability, and scalability. Writing **clean code** means developing code that is easy to read, understand, and with - not just you, but for others as well. Well-structured code simplifies debudding, fosters collaboration, and allows for future modifications and extensions, ensuring your software remains useful and adaptable over time.


::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa file-code >}} Code Style
Conventions and guidelines used to write and format code.

::: {.learn-more}
[Learn more »](./code_style.md)
:::
:::

::: {.feature}
### {{< fa poo >}} Code Smells
Symptoms of poor code quality that can indicate deeper problems in the code.

::: {.learn-more}
[Learn more »](./code_smells.md)
:::
:::

::: {.feature}
### {{< fa wrench >}} Refactoring
Restructuring existing code without changing its external behavior.

::: {.learn-more}
[Learn more »](./refactoring.md)
:::
:::

::: {.feature}
### {{< fa shield-alt >}} Online services
Services that provide code quality analysis.

::: {.learn-more}
[Learn more »](./online_services.md)
:::
:::

:::
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Other resources
- [The Turing Way - Writing Robust Code](https://the-turing-way.netlify.app/reproducible-research/code-quality/code-quality-robust.html?highlight=error)
- [Utrecht University - Workshop on Writing Reproducible Code](https://utrechtuniversity.github.io/workshop-computational-reproducibility/)
- [A set of Common Software Quality Assurance Baseline Criteria for Research Projects](https://indigo-dc.github.io/sqa-baseline/)
:::