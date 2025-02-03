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
title: Hard coding

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Explanation of hard coding and how to address it
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
categories: 
- refactoring 

---

Hard-coding variables occurs when constants and specific values are directly embedded into the code instead of being defined as variables or passed as arguments. Hard-coding makes the code less flexible and harder to maintain because changing the behavior requires modifying the source code rather than adjusting parameters. 

This smell is often noticed when changing the program's behavior required direct source code modification, rather than simple configuration changes or parameter adjustments.


## Symptoms
- You find yourself searching the codebase for specific values to tweak behavior for different executions.
- The same constant value appears multiple times, making updates error-prone.
- The logic is less readable, since magic numbers don’t indicate what they represent.
- Code cannot easily adapt to different contexts without modification.

## Example of hard coding and magic numbers
```python
def calculate_area(radius):
    # Hard-coded value of pi
    return 3.14 * radius * radius # What if you need more precision?

def check_temperature(temperature):
    # Hard-coded temperature values for thresholding
    if temperature > 30: # What does 30 represent
        print("It's too hot!")
    elif temperature < 10:
        print("It's too cold!")
```

### Issues
- The value of pi is hard-coded as `3.14`, which can lead to precision issues.
- The temperature thresholds (30, 10) are buried in the logic, making them difficult to modify.
- The meaning of 30 and 10 is unclear - are they for a specific region, season, or use case?


## Solution
Using named constants and configurable parameters makes the code more readable, maintainable, and flexible.

## Example solution with default parameters
```python
import numpy as np  # Use a library constant

HOT_THRESHOLD = 30  # Defined constant for readability
COLD_THRESHOLD = 10  # Defined constant for readability

def calculate_area(radius):  # Default parameter allows customization
    return np.pi * radius * radius # Use library constant for pi

def check_temperature(temperature, hot_threshold=HOT_THRESHOLD, cold_threshold=COLD_THRESHOLD):
    if temperature > hot_threshold: # Use named constants for readability
        print("It's too hot!")
    elif temperature < cold_threshold:
        print("It's too cold!")

```
