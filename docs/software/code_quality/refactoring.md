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

Refactoring is the process of **restructuring existing code without changing its external behavior**. Refactoring helps make the code more maintainable and understandable, which in turn makes it easier to build on and less likely to develop bugs. This can include:

- Improving readability - making code easier to understand, which helps future maintainers and external partners.
- Reducing complexity - simplifying complex code structures, which can involve breaking down large functions into smaller, more manageable pieces or removing unnecessary dependencies.
- Optimizing software design - making it more robust and adaptable for future needs. 
- Identifying and eliminating redundancies - removing duplicated or unnecessary code.
- Ensuring consistency - adhere to a consistent coding style accross the codebase to ensure the code is uniform.


### Refactoring workflow

![CC-BY-4.0 © 2021 Balaban et al.](https://journals.plos.org/ploscompbiol/article/figure/image?size=large&id=10.1371/journal.pcbi.1008549.g009&type=medium)

#### When to refactor code?

1. **Rule of three:** Begin refactoring when the same or very similar code is being written for the third time.
2. **When adding a feature:** Refactoring existing code before adding new features can help simplify the integration of new functionality.
3. **When fixing a bug:** Cleaning up code in the areas around a bug can make it easier to identify and fix the issue.
4. **During a code review:** Refactoring during code reviews can prevent issues from becoming part of the public codebase and streamline the development process.
5. **Finding a code smell** (see below)

👉 [Refactoring.Guru - When to refactor?](https://refactoring.guru/refactoring/when)

#### How to refactor code?

Refactoring should be done through minor changes without breaking the underlying code. Each iteration should make your code slightly better, and could be done according to this checklist:

1. **Maintain clean code:** Refactor with the aim to make the code cleaner and more efficient.
2. **Avoid adding new features:** Refactor without introducing new functionalities.
3. **Keep tests passing:** All existing tests should still be passing after refactoring, ensuring no new bugs are introduced.

👉 [Refactoring.Guru - How to refactor?](https://refactoring.guru/refactoring/how-to)

:::{.callout-note}
## Further reading

- [Refactoring techniques from Refactoring.Guru](https://refactoring.guru/refactoring/techniques)
- [The Alan Turing Institute - Refactoring](https://alan-turing-institute.github.io/rse-course/html/module07_construction_and_design/07_04_refactoring.html)
:::