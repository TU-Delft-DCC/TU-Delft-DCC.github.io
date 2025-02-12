---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-03

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

Hard-coding variables occurs when constants, configuration values, or logic are directly embedded into the code, making changes difficult. Hard-coding leads to rigid systems that require modifying the source code itself to change behavior, rather than adjusting parameters, settings, or external configurations.

## Symptoms
- Magic numbers or string literals appear directly in the code.
- You find yourself searching the codebase for specific values to tweak behavior for different executions.
- The same constant value appears multiple times, making updates error-prone.
- The logic is less readable, since magic numbers don’t indicate what they represent.
- A small behavior change requires altering the core code, instead of adjusting an input parameters of config file.

## Example - Hard coding and magic numbers
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


### Solution
Using named constants and configurable parameters makes the code more readable, maintainable, and flexible.

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

## Example - Rigid code
This simulation hard-codes the time step and duration, making it rigid.

```python
def run_simulation():
    step_size = 0.01  # Fixed timestep
    total_time = 10  # Fixed total duration
    for t in range(0, total_time, step_size):
        update_system(t)

```

#### Issues
- Change the step size of total duration required modifying the source code.
- The code is not reusable across different simulations.

### Solution
Introduce function parameters or external configuration files for flexibility and reproducibility.

```python
def run_simulation(step_size=0.01, total_time=10):
    for t in range(0, total_time, step_size):
        update_system(t)

# Calling with different configurations
run_simulation(step_size=0.05, total_time=20)  # Adjust without modifying the underlying code
```

For larger projects, moving configuration values to a separate file or class can further improve reproducibility and maintainability. Users would then only need to adjust the (text-based) configuration file without touching the core code.

```yaml
# config.yaml
simulation:
  step_size: 0.01
  total_time: 10
```

```python
import yaml

def load_config(file_path="config.yaml"):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
run_simulation(config['simulation']['step_size'], config['simulation']['total_time'])
```

## Key takeaways
- Use named constants for improved readability.
- Externalize configuration values to allow easy adjustments without modifying the source code.
- Configuration files or classes can further improve maintainability and reproducibility.


<!-- ::: {.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- 
::: -->
