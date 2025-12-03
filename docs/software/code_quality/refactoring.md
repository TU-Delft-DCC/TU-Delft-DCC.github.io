---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-06

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-12-03

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
author_1: Maurits Kok
author_2: Manuel Garcia

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
  - Code Quality
  - Refactoring
---


>"Always leave the code you're editing a little better than you found it."
>
> **Robert C. Martin** (Uncle Bob)

## What is refactoring?

Refactoring is the process of **restructuring existing code without changing its external behaviour**. It improves maintainability and readability, making future developments smoother and reducing the likelihood of bugs. Key benefits include:

- **Improving readability** - Writing code that's easier to understand, benefits both yourself and future developers.
- **Reducing complexity** - Simplifying complex structures by breaking down large functions or removing unnecessary dependencies.
- **Optimizing design** - Creating a more robust and adaptable codebase for long-term growth. 
- **Eliminating redundancies** - Removing duplicate or unnecessary code.
- **Ensuring consistency** - Following a consistent coding style for a cleaner, more maintanable codebase.

### When should you refactor?
![CC-BY-4.0 © 2021 Balaban et al.](/docs/img/refactoring.PNG){width=50%}

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

{{< fa shoe-prints >}} **Always work in small steps** - So that you can easily identify if a change to the code changes the its behaviour. 

{{< fa ban >}} **Avoid adding new features** - Focus on improving structure, not functionality. 

{{< fa check-double >}} **Ensure tests pass** - Verify that all existing tests succeed before starting with refactoring. If there are no tests, consider writing some basic tests first to cover the existing functionality. 

{{< fa vial-circle-check >}} **Test often** - So that you can be sure the behaviour remains unchanged.

{{< fa code-commit >}} **Commit often** - Use a version control system and commit often, so that you can easily revert changes if something goes wrong. 

{{< fa bullseye >}} **Remember, you can stop at any point** - Refactoring can be an endless taks if you aim for perfection. Instead aim to leave the code in a better state than you found it.

## Farley's refactoring method

Refactoring can be approached in various ways. Here, is a simple four-step method proposed by Dave Farley in his book *"Continuous Delivery"*. This method emphasizes safety and gradual improvement.

### 1. Write approval tests

Create software tests for the code that will be refactored. *Approval tests* are software tests that check the outputs of a program or part of a program. Approval tests are important in refactoring because we need to know if changes in the code affect its behaviour.

### 2. Reduce clutter

Remove unnecessary code, such as [unused (dead) code](./code_smells/dead_code.md), and [repeated code](./code_smells/duplication.md). 
While doing so, be cautious when removing code, but take some chances when reducing clutter. To safely reduce clutter, rely on version control to undo changes, and on approval tests to check that code changes do not affect its behaviour.

### 3. Reduce cyclomatic complexity

Cyclomatic complexity refers to the number of logical branches or pathways used in the code to implement functionality and behaviour. The overuse of **if statements** and **loops** is an indication of code with high levels of cyclomatic complexity. 

To reduce cyclomatic complexity:

- Reduce branching or pathways in the code.
- Bring related code together, and keep unrelated code apart.
- Look for blocks of code that can be separated in methods or functions; this is known as *method extraction*.

### 4. Composing methods

At the last step, focus on improving the structure and readability of the code by extracting methods or functions from existing code blocks. This involves breaking down large methods into smaller, more manageable pieces that each perform a single task or function. 

When composing methods, consider the following guidelines:

- Make each extracted method (or function) tell its own story. This requires understanding the context of the code within a program and how it is expected to be read and interpreted by other developers. 
- Ideally, each method tells a single, well structured and easy-to-understand story. If that is not the case, the code is poorly written and should be refactored. 
- Rename things (functions, classes, variables) so that their behaviour is clear in the code.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Refactoring techniques from Refactoring.Guru](https://refactoring.guru/refactoring/techniques)
- [eScience Center - Lesson on refactoring](https://carpentries-incubator.github.io/python-intermediate-development/34-code-refactoring.html)
- [The Alan Turing Institute - Refactoring](https://alan-turing-institute.github.io/rse-course/html/module07_construction_and_design/07_04_refactoring.html)
- [Dave Farley's Refactoring Course - Free ](https://courses.cd.training/courses/refactoring-tutorial)
:::