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
title: More testing concepts

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
- testing 


---

#### **Code Coverage**
Code coverage measures how much of your code is executed during testing. It is a useful metric to ensure that your tests are comprehensive and indicate your code's quality. If your software becomes a dependency for others, a code coverage of 70% or higher is recommended for unit tests.

::: {.panel-tabset}
## Python
- [pytest-cov plugin](https://pypi.org/project/pytest-cov/) (for pytest)
- [Coverage.py documentation](https://coverage.readthedocs.io/en/latest/)

## MATLAB
- [Collect code coverage with Command Window execution](https://nl.mathworks.com/help/matlab/ref/runtests.html#d126e1481788) *(since R2023b)*
- [Code coverage with Test Browser](https://nl.mathworks.com/help/matlab/ref/testbrowser-app.html#:~:text=Generate%20Code%20Coverage%20Report) *(since R2023a)*
- [Collect code coverage metrics](https://nl.mathworks.com/help/matlab/matlab_prog/collect-statement-and-function-coverage-metrics-for-matlab-source-code.html)
:::

#### **Error handling**
Tests should check if your code behaves as expected when it encounters errors. This includes testing if the code raises the correct exceptions when given invalid input or when an error occurs.

::: {.panel-tabset}
## Python
- [Assert raised exceptions](https://docs.pytest.org/en/stable/how-to/assert.html#assertraises)

Example in Python:
```python
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

## MATLAB
- [Verify function throws specific exceptions](https://nl.mathworks.com/help/matlab/ref/matlab.unittest.qualifications.verifiable.verifyerror.html)

:::

#### **Fixtures** 
Fixtures are predefined states or sets of data used to set up the testing environment, ensuring consistent conditions for tests to run reliably. Fixtures can be used to set up databases, create temporary files, or initialize other resources, that then available to all tests in a test suite.

::: {.panel-tabset}
## Python
- [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)

## MATLAB
- [Create shared fixtures](https://mathworks.com/help/matlab/matlab_prog/write-test-using-shared-fixtures.html)
::: 
    
#### **Parameterization**
Parameterization involves running the same test with different inputs or configurations to ensure broader coverage and identify potential edge cases. 
    
::: {.panel-tabset}
## Python
- [Parameterizing unit tests](https://carpentries-incubator.github.io/python-intermediate-development/22-scaling-up-unit-testing.html#parameterising-our-unit-tests)

## MATLAB
- [Create a basic parameterized test](https://nl.mathworks.com/help/matlab/matlab_prog/create-basic-parameterized-test.html)
::: 

#### **Mocking**
Mocking (or monkeypatching) is a technique used to simulate the behavior of dependencies or external systems during testing, allowing isolated testing of specific components. For example, if your software requires a connection to a database, you can *mock* this interaction during testing.

![MathWorks, MATLAB Mocking Diagram, MATLAB Documentation, [link to image.](https://nl.mathworks.com/help/matlab/matlab_prog/create-mock-object.html)](https://nl.mathworks.com/help/matlab/mocking_overview.png)

::: {.callout-note appearance="simple" icon="false" collapse="true"} 
## 🐒 Monkeypatching?
The term monkey patch seems to have come from an earlier term, guerrilla patch, which referred to changing code sneakily – and possibly incompatibly with other such patches – at runtime. The word guerrilla, nearly homophonous with gorilla, became monkey, possibly to make the patch sound less intimidating.
:::

::: {.panel-tabset}
## Python
- [How to monkeypatch/mock modules and environments](https://docs.pytest.org/en/latest/how-to/monkeypatch.html)

## MATLAB
- [Create Mock Object](https://nl.mathworks.com/help/matlab/matlab_prog/create-mock-object.html) 
:::

#### **Marks and tags**
You can use test tags to group tests into categories and then run tests with specified tags. This is useful when you want to run only a subset of tests, such as regression tests, or when ignoring slow tests during development. 

::: {.panel-tabset}
## Python
- [Working with custom markers](https://docs.pytest.org/en/7.1.x/example/markers.html)

## MATLAB
- [Tag unit tests](https://nl.mathworks.com/help/matlab/matlab_prog/tag-unit-tests.html)
:::
