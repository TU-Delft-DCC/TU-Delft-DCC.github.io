---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-12

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Testing in Python

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
- Python

---

## Testing in Python

In Python, two popular frameworks are used: `pytest` and `unittest`. In this guide, we demonstrate the use of `pytest`. When starting out with testing in Python, it is [**recommended to use `pytest`**](https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful).

::: {.callout-note collapse="true"}
## What is the difference between pytest and unittest?
The main difference between the two frameworks is that `pytest` offers a more user-friendly and less verbose syntax, allowing for simpler test writing and better readability. `unittest` is part of the Python standard library and follows a more traditional object-oriented style of writing tests.
:::

#### Step 1. Setup a testing framework

Install pytest using pip

```bash
pip install pytest
```
Setup your test framework with the following structure in your repository:

```markdown
src/
    mypkg/
        __init__.py
        add.py
        draw_random_number.py
tests/
    test_add.py
    test_draw_random_number.py
    ...
```
  
#### Step 2. Identify testable units
Identify functions, methods, or classes that need to be tested within the Python codebase.

#### Step 3. Write test cases
Write test functions using the pytest framework to test the identified units. For example:

```python
# src/mypkg/add.py
def add(x,y):
    return x + y
```

```python
# tests/test_add.py
from mypkg import add

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
```

::: {.callout-tip}
Limit the number of assert statements in a single test function. Otherwise, when an assert fails, pytest will not test the remaining assertions in the test function.
:::

#### Step 4. Run tests locally
Run the test suite locally using the pytest command to ensure it executes correctly. 

```bash
pytest test_add.py
```

Pytest will automatically discover all files that are prepended with `test_`. To run all tests, execute `pytest` without any arguments.

#### Step 5. Interpret and fix tests
Interpret the test results displayed in the console to identify any failures or errors. If errors occur, debug the failing tests by examining failure messages and stack traces.

#### Step 6. Run coverage report locally
Generate a coverage report to gain insights into which parts of the codebase have been executed during testing (see [Code Coverage](#code-coverage)). 

#### Step 7. Run tests remotely
Integrate the test suite with a Continuous Integration service (e.g., GitHub Actions) to automate testing. 

::: {.callout-note}
## Learning materials for automated testing
- [Intermediate Research Software Development - CI for Automated Testing](https://carpentries-incubator.github.io/python-intermediate-development/23-continuous-integration-automated-testing/index.html)
- [Code Refinery - Automated testing](https://coderefinery.github.io/testing/continuous-integration/)
:::

#### Examples of repositories with tests

- eScience Center - [Project `matchms`](https://github.com/matchms/matchms)
- Pandas library - [Repository tests](https://github.com/pandas-dev/pandas/tree/main/pandas/tests)

::: {.callout-note}
## Further reading
- Pytest - [Getting Started](https://docs.pytest.org/en/8.0.x/getting-started.html#get-started)
- Code Refinery - [Pytest exercise](https://coderefinery.github.io/testing/locally/)
- RealPython - [Effective testing with pytest](https://realpython.com/pytest-python-testing/)
:::