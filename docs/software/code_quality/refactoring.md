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
title: Refactoring

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of refactoring code practices
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


>"Always leave the code you're editing a little better than you found it."
>
> **Robert C. Martin** (Uncle Bob)

### What is refactoring?

Refactoring is the process of **restructuring existing code without changing its external behavior**. It improved maintainability, readability, and efficiency, making future developments smoother and reducing the likelihood of bugs. Key benefits include:

- **Improving readability** - Writing code that's easier to understand, benefits both yourself and future developers.
- **Reducing complexity** - Simplifying complex structures by breaking down large functions or removing unnecessary dependencies.
- **Optimizing design** - Creating a more robust and adaptable codebase for long-term growth. 
- **Eliminating redundancies** - Removing duplicate or unnecessary code.
- **Ensuring consistency** - Following a consistent coding style for a cleaner, more maintanable codebase.

### When should you refactor?
![CC-BY-4.0 © 2021 Balaban et al.](https://journals.plos.org/ploscompbiol/article/figure/image?size=large&id=10.1371/journal.pcbi.1008549.g009&type=medium){width=50%}

1. **Rule of three:** If you find yourself writing the same or similiar code for the third time, it's time to refactor.
2. **Before adding a feature:** Cleaning up existing code makes it easier to integrate a new functionality.
3. **When fixing a bug:** Cleaning up surrounding code can help uncover and fix the issue faster.
4. **During code reviews:** Refactoring during code reviews can prevent issues from becoming part of the public codebase and streamline the development process.
5. **When you spot a code smell:** Addressing [code smells](./code_smells.md) early prevents them from evolving into more serious bugs.

::: {.learn-more}
{{< fa arrow-right >}} [Learn more: When to refactor?](https://refactoring.guru/refactoring/when)
:::

### How to refactor code effectively?

Refactoring should be done gradually, improving code in small controlled 
steps without introducing new functionalities. Keep these principles in mind:

{{< fa broom >}} **Maintain clean code** - Aim for clarity, simplicity, and readability.  
{{< fa ban >}} **Avoid adding new features** - Focus on improving structure, not functionality.  
{{< fa check-double>}} **Ensure tests pass** - Verify that all existing tests still succeed to prevent new bugs.

::: {.lean-more}
{{< fa arrow-right >}} [Learn more: How to refactor?](https://refactoring.guru/refactoring/how-to)
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Refactoring techniques from Refactoring.Guru](https://refactoring.guru/refactoring/techniques)
- [eScience Center - Lesson on refactoring](https://carpentries-incubator.github.io/python-intermediate-development/34-code-refactoring.html)
- [The Alan Turing Institute - Refactoring](https://alan-turing-institute.github.io/rse-course/html/module07_construction_and_design/07_04_refactoring.html)
:::