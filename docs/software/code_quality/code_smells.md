---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY/MM/DD]
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
title: Code smells

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of common code smells and how to address them
hide-description: true

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
categories: 
- refactoring 

css: styles.css
---

![CC-BY-4.0 © 2021 Balaban et al.](/docs/img/bad_code_design.PNG){fig-alt="Drawing of a pyramid with various traps resembling code smells." width=600}

Code smells are software characteristics that suggest there might be an issue with the code's design or implementation. While code smells themselves might not always indicate a bug or malfunction, they can make the code harder to understand, maintain, and extend, which can lead to bugs and other issues down the line. Code smells are usually noticed and addressed during code reviews, when writing tests, adding new features, fixing bugs, and during automated code analysis. 

::: {.grid}

::: {.g-col-4}
::: {.code-smell-card}
##### Long Method
**Problem:** A function is very long and hard to understand or maintain.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor long methods](./code_smells/long_method.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Large Classes
**Problem:** A class contains too many responsibilities or functionalities.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor large classes](./code_smells/monolithic_design.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Code Duplication
**Problem:** The same or very similar code appears in multiple places.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor duplicate code](./code_smells/duplication.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Hard-Coding
**Problem:** Literal values (e.g., numeric values or strings) are directly embedded in the code.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor hard-coded values](./code_smells/hardcoded_values.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Deep Nesting
**Problem:** There are excessive levels of nested loops or conditionals.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor nested logic](./code_smells/deep_nesting.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Long Argument Lists
**Problem:** Functions require a long list of parameters.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor argument lists](./code_smells/many_arguments.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Inappropriate Intimacy
**Problem:** Two classes or methods depend too much on each other's internals.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor coupling](./code_smells/inappropriate_intimacy.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Side Effects
**Problem:** Changes in one part of the code cause unexpected behavior in another.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor side effects](./code_smells/side_effects.md)
:::
:::
:::

::: {.g-col-4}
::: {.code-smell-card}
##### Commented Code
**Problem:** There is a significant amount of outdated or commented-out code cluttering the source.  

::: {.refactor-link}
[{{< fa wrench >}} Refactor commented code](./code_smells/dead_code.md)
:::
:::
:::


:::


:::{.callout-note}
## Further reading
- [Ten simple rules for quick and dirty scientific programming](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008549)
- [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
:::