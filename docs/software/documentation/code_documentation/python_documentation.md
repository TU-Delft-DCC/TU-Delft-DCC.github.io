---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-27

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Python code documentation

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Maurits Kok
author_2: Elviss Dvinskis

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
  - Software
  - Documentation
  - Python
  - Docstrings
  - Code comments

---

- **Code readability** is detailed in a coding style guide.
- **Code comments** are useful for clarifying complex parts of code, noting why certain decisions were made in specific blocks or lines.
- **Docstrings** provide a description of the function, class, or module that follows immediately after it is defined, and should contain all the relevant information needed for using them, rather than explaining how the code works. Ideally, every module should have a docstring, and so should every function and class that a module makes available. 

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Further reading
[Documenting Python code](https://realpython.com/documenting-python-code/)
:::

## Code comments

Code comments are inline annotations meant for developers who read or maintain the source code. They should:

- explain parts that are not intuitive from the code itself
- explain the purpose of a piece of code (why over how)
- need to be kept up-to-date as wrong comments are not caught through testing
- **do not** replace readable and structured code
- **do not** turn old code into commented zombie code (see code smells)
- **do not** repeat in natural language what is written in your code, e.g.

```python
# Now we check if the age of a patient is greater than 18
if age_patient > 18:
```

## Docstrings
Docstrings are structured comments, associated with segments (rather than lines) of code which can be used to generate documentation for users (and yourself!) of your project. They allow you to provide documentation to a segment (function, class, method) that is relevant for the user. Docstrings are placed in triple quotes `"""` and enable automated generation of API documentation.

Two docstring styles are commonly used for their readability:


::: {.panel-tabset}

## NumPy style


```python
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    return True
```
⮕ Check out the [NumPy style guide](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) or a [full example](https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html#example-numpy).

## Google style


```python
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True
```
⮕ Check out the [Google style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) or a [full example](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google).

:::

### Docstring formatting
   
[Python's PEP 257](https://peps.python.org/pep-0257/) provides guidelines on how to effectively write docstrings to ensure they are clear, concise, and useful. Some pointers:

- The summary sentence of the docstring should appear on the same line as the opening triple quotes.
- The closing triple quotes should be placed on a separate line, except for one-line docstrings.
- Docstrings for methods and functions should not have blank lines before or after them.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Example
```python
def find_max(numbers):
    """Find the maximum value in a list of numbers.

    Parameters
    ----------
    numbers : iterable
        A collection of numerical values from which the maximum will be determined.

    Returns
    -------
    max_value : `float`
        The highest number in the given list of numbers.
    """
    pass
```
:::
- Docstrings for classes should immediately follow the class definition without any preceding blank lines. However, a single blank line should follow the docstring, separating it from subsequent code such as class variables or the **__init__** method.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Example
```python
class Circle(object):
    """A circle defined by its radius.

    Parameters
    ----------
    radius : `float`
        The radius of the circle.
    """

    def __init__(self, radius):
        self.radius = radius
```
:::

- The content of a docstring must align with the indentation level of the code it documents.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Correct and incorrect examples

::: {.panel-tabset}

## {{< fa thumbs-up >}}

```python
def get_length(items):
    """Calculate the number of items in the list.

    Parameters
    ----------
    items : list
        A list whose length is to be determined.

    Returns
    -------
    length : int
        The number of items in the list.
    """
    return len(items)
```
## {{< fa thumbs-down >}}

```python
def get_length(items):
    """Calculate the number of items in the list.

Parameters
----------
items : list
    A list whose length is to be determined.

Returns
-------
length : int
    The number of items in the list.
"""
    return len(items)
```
:::

:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- Build [API reference](https://developer.lsst.io/python/numpydoc.html) from docstrings
- [Numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html) -  best practices for docstrings
:::

### Docstring contents
Formatting conventions are important for clarity and readability across different APIs or libraries. Here we adhere to the numpydoc convention. 

#### **Summaries**
Docstrings should start with a one-sentence summary and if additional clarification is needed, you could add an [extended summary](https://developer.lsst.io/python/numpydoc.html#py-docstring-extended-summary). For functions and methods, use imperative voice, framing its summary as a command or instruction that the user can execute through the API. For classes, the summary should clearly describe what the class represents or its primary responsibility.

#### **Parameters and arguments**
The *Parameters* section lists the input parameters of a class, function, or method. It should include the parameter name, type, and a brief description of what the parameter represents. *Parameters* are listed in the same order as they appear in the function definition.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Full description and example

[Describing parameters](https://developer.lsst.io/python/numpydoc.html#py-docstring-parameters)

Basic example:
```python
def calcDistance(x, y, x0=0., y0=0., **kwargs):
    """Calculate the distance between two points.

    Parameters
    ----------
    x : `float`
        X-axis coordinate.
    y : `float`
        Y-axis coordinate.
    x0 : `float`, optional
        X-axis coordinate for the second point (the origin,
        by default).

        Descriptions can have multiple paragraphs, and lists:

        - First list item.
        - Second list item.
    y0 : `float`, optional
        Y-axis coordinate for the second point (the origin,
        by default).
    **kwargs
        Additional keyword arguments passed to
        `calcExternalApi`.
    """
```

:::

#### **Returns and Yields**
*Returns* is an explanation about the returned values and their types, following the same format as *Parameters*. This is applicable to functions and methods. Use *Yields* for generators.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} *Returns* and *Yields* examples

- [Documenting Returns](https://developer.lsst.io/python/numpydoc.html#py-docstring-returns)
- [Documenting Yields](https://developer.lsst.io/python/numpydoc.html#yields)
 
::: {.panel-tabset}

## Basic example for *Returns*:

```python
def getCoord(self):
    """Get the point's pixel coordinate.

    Returns
    -------
    x : `int`
        X-axis pixel coordinate.
    y : `int`
        Y-axis pixel coordinate.
    """
    return self._x, self._y
```

## Basic example for *Yields*:

```python
def items(self):
    """Iterate over items in the container.

    Yields
    ------
    key : `str`
        An item's key.
    value : obj
        An item's value.
    """
    for key, value in self._data.items():
        yield key, value
```

:::
:::

#### **Raises**
For classes, methods, and functions the *Raises* section is used to describe exceptions that are explicitly raised.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Example

- [Documenting Raises](https://developer.lsst.io/python/numpydoc.html#raises)

```python
Raises
------
IOError
    Raised if the input file cannot be read.
TypeError
    Raised if parameter ``example`` is an invalid type.
```
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Documenting modules](https://developer.lsst.io/python/numpydoc.html#documenting-modules)
- [Documenting classes](https://developer.lsst.io/python/numpydoc.html#documenting-classes)
- [Documenting methods and functions](https://developer.lsst.io/python/numpydoc.html#documenting-methods-and-functions)
- [Documenting constants and class attributes](https://developer.lsst.io/python/numpydoc.html#documenting-constants-and-class-attributes)
- [Documenting class properties](https://developer.lsst.io/python/numpydoc.html#documenting-class-properties)
- [Complete example module](https://developer.lsst.io/python/numpydoc.html#complete-example-module)
- [numpydoc example](https://numpydoc.readthedocs.io/en/latest/example.html#example)
:::

