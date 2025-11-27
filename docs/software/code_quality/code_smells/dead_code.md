---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-04

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
title: Dead code

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

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
  - Refactoring
  - Dead Code

---

Dead code refers to unused or unreachable code that remains in the codebase but serves no functional purpose. Commented-out code consists of inactive code blocks that developers have disabled rather than deleting. Both contribute to clutter and reduce maintainability.

## Symptoms

- Unused variables or functions.
- Conditional blocks that never execute.
- Large blocks of commented-out code.
- Using comments to disable code to change the behavior of the code.

:::{.callout-tip}
Do not use comments to change the behavior of the code. Instead, make use of input parameters or configuration settings to control the behavior of the code.
:::

## Solution
- If code is not needed, delete it. Use version control (e.g., Git) to restore it if necessary. Commit the removal of the commented-out code with a meaningful commit message explaining why it was removed. This allows you to track the change and easily revert it if necessary.
- To change the executation of your code, use [input parameters or configuration settings](./hardcoded_values.md) to control the behavior of the code. This makes the code more readable and maintainable.
