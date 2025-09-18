---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-12

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
    - Software
    - Testing
    - Python

---

In Python, two widely used testing frameworks are `pytest` and `unittest`. This guide focuses on `pytest`, which is recommended for its simplicity and readability. If you are new to testing in Python, [**`pytest` is a great starting point**](https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful).

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa info-circle >}} What is the difference between `pytest` and `unittest`?

- `pytest` is a third-party testing framework that is more user-friendly, requires less boilerplate, and offers better readability.
- `unittest` is part of the Python standard library and follows a more traditional object-oriented style of writing tests. 
:::

### Step 1. Setup a testing framework

Install pytest

```bash
pip install pytest
```

A good practice is to organize the codebase into a `src` directory for the source code and a `tests` directory for the test suite. For example:

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
  
### Step 2. Identify testable units
Identify functions, methods, or classes on your code that should be tested. Focus on critical computations and potential points of failure.

### Step 3. Write test cases
Write test functions using `pytest`. Here's an example:

```python
# src/mypkg/add.py
def add(x,y):
    return x + y

# tests/test_add.py
from mypkg.add import add

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
```

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Limit the number of `assert` statements in a single test function. Otherwise, when a particular assert fails, the remaining assertions in the test function will not be executed.
:::

### Step 4. Run tests locally
Run all tests in the project by executing the following command:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_add.py
```

### Step 5. Debug and fix failing tests
The test results displayed in the console will help you to identify any failures or errors. If errors occur, debug the failing tests by examining failure messages and stack traces.

### Step 6. Run coverage report locally
Generate a coverage report to gain insights into which parts of the codebase have been executed during testing (see [Code Coverage](./intermediate.md#code-coverage)). 

```bash
pip install pytest-cov
pytest --cov=mypkg tests/
```

### Step 7. Automate testing with Continuous Integration
Integrate youre test suite with a Continuous Integration service (e.g., GitHub Actions) to run tests automatically on every code change.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa graduation-cap >}} Learning materials for automated testing
- [Intermediate Research Software Development - CI for Automated Testing](https://carpentries-incubator.github.io/python-intermediate-development/23-continuous-integration-automated-testing.html)
- [Code Refinery - Automated testing](https://coderefinery.github.io/testing/continuous-integration/)
:::

### Examples of repositories with tests

- eScience Center - [Project `matchms`](https://github.com/matchms/matchms)
- Pandas library - [Repository tests](https://github.com/pandas-dev/pandas/tree/main/pandas/tests)

::: {.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- Pytest - [Getting Started](https://docs.pytest.org/en/8.0.x/getting-started.html#get-started)
- Code Refinery - [Pytest exercise](https://coderefinery.github.io/testing/locally/)
- RealPython - [Effective testing with pytest](https://realpython.com/pytest-python-testing/)
:::