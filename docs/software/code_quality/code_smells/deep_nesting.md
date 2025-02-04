---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY/MM/DD]
# Uncomment and populate the next line accordingly
date: 2025/02/03

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Deep Nesting

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
- refactoring

---

> "Code is like humor. When you have to explain it, it’s bad."
>
> **Cory House**

Deep nesting occurs when there are too many levels of indentation in the code, making it harder to understand, maintain, and debug. It can lead to reduced readability, and increases cognitive load for developers. 

## Symptoms
- Excessive indentation makes it hard to track logic.
- Many nested `if` statements or `for` loops.
- Hard-to-follow branching logic.
- Slow performance due to inefficient code.
- Increased likelihood of bugs due to complexity.

## Example deeply nested conditional statements

```python
def validate_model_convergence(model):
    if model.convergence > 1:
        if model.convergence < 0.1:
            if model.secondary_condition == True
                return True
            else:
                return False
        else:
            return False
    else:
        return False
```

### Solution

Refactoring deep nesting improves readability and maintainability. Techniques to reduce deep nesting include:

- Using early returns to eliminate unnecessary indentation.
- Extracting complex logic into helper functions for better modularity.
- Using built-in functions like `any` and `all` to simplify conditions.


#### Solution 1: Using early returns
```python
def validate_model_convergence(model):
    if model.convergence <= 1:
        return False
    if model.convergence >= 0.1:
        return False
    if not model.secondary_condition:
        return False
    return True
        
```

Thia solution uses early returns to reduce the nesting level and make the code more readable. Each condition is checked separately, and if it fails, the function returns immediately, avoiding further nesting and evaluation of unnecessary conditions.

#### Solution 2: Using `all` for conciseness

Alternatively, we can use the `all` function to check multiple conditions in a single line, which can make the code more concise and easier to read.


```python
def validate_model_convergence(model):
    return all([
        model.convergence > 1,
        model.convergence < 0.1,
        model.secondary_condition,
    ])

```



## Example deeply nested loops
In this example, we have three nested loops to iterate over three 3D arrays and sum their corresponding elements. This code can be refactored using NumPy to improve performance and readability.

```python
# Create three random 10x10x10 arrays
A = np.random.rand(10, 10, 10)
B = np.random.rand(10, 10, 10)
C = np.random.rand(10, 10, 10)

# Using nested loops (inefficient)
result = np.zeros((10, 10, 10))
for i in range(10):
    for j in range(10):
        for k in range(10):
            result[i, j, k] = A[i, j, k] + B[i, j, k] + C[i, j, k]
``` 

### Solution
Using NumPy, we can perform the same operation without nested loops, which is more efficient and easier to read.

```python
# Create three random 10x10x10 arrays
A = np.random.rand(10, 10, 10)
B = np.random.rand(10, 10, 10)
C = np.random.rand(10, 10, 10)

# Vectorized solution (fast & efficient)
result = A + B + C
```

## Benefits
By restructuring nested code using these techniques, we create cleaner, more maintainable software while reducing the risk of logical errors.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} **Learn more:**
- [RealPython - "Look Ma, No For-Loops"](https://realpython.com/numpy-array-programming/)
:::