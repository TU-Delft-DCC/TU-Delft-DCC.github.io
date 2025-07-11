---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-06

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Side effects and external state

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

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

---

Side effects occur when a function modifies external state or interacts with the outside world beyond simply returning a value. This makes code less predictable, harder to test, and more difficult to debug.

## Symptoms

- Unexpected changes to the global state
- Non-deterministic behavior
- Hidden dependencies

:::{.callout-tip}
**Pure functions** are **deterministic** (always return the same output for the same input) and have **no side-effects**.

Instead, non-pure functions often:

- Modify global variables or shared state, leading to unintended behavior.
- Change input parameters (mutating function arguments).
- Perform I/O operations like reading from or writing to files, databases, or APIs.
- Generate random numbers, making them non-deterministic.
- Depend on external state, meaning results may change due to external factors.
:::

## Example - Function with side effects
```python
# Modifies global state (side effect)
data = []

def add_item(item):
    data.append(item)  # Changes an external variable

add_item("A")
print(data)  # ['A'] - Output depends on previous calls

```

### Solutions

#### 1. Separate pure and non-pure functions
Keep your computational logic (pure) separate from side-effect operations (non-pure).

```python
def process_data(data):  # Pure function: no external state modification
    return [x**2 for x in data]

def save_to_file(filename, data):  # Non-pure: writes to a file
    with open(filename, "w") as f:
        f.write("\n".join(map(str, data)))

# Usage
numbers = [1, 2, 3]
processed = process_data(numbers)
save_to_file("output.txt", processed)
```

#### 2. Avoid mutating global variables
Use function parameters and return values instead of modifying external variables.

```python
def add_item(data, item):
    return data + [item]  # Returns a new list instead of modifying global state

data = []
data = add_item(data, "A")  # Safe: no side effects
```

## Key takeaways

- Ensure that each function or module has a single responsibility. 
- Break down complex functions into smaller, focused functions that perform specific tasks. 
- Isolate non-pure functions with side effects from pure functions.

![*CC-BY-4.0 CodeRefinery*](/docs/img/good-vs-bad.svg)