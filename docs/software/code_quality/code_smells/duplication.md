---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-03

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
title: Duplicated code

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Fixing duplicated code in your codebase
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
  - Software
  - Refactoring
  - Duplicated Code

---

> "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."
>
> **Antoine de Saint-Exupéry**

Duplicated code occurs when similar or identical blocks of code appear multiple times within a codebase. This can increase maintenance efforts, as changes in one place might require corresponding changes elsewhere, leading to inconsistencies and higher changes or errors. 

## Symptoms
- The same logic appears in multiple places, sometimes with minor variations.
- Fixing a bug required modifying the same code in multiple places.
- Adding a new feature results in copy-pasting existing code rather than reusing it.

## Example - Duplicate code in functions
```python
def time_of_flight_ball(initial_velocity, launch_angle):
    g = 9.81  # Earth's gravity (m/s²)
    return (2 * initial_velocity * np.sin(launch_angle)) / g

def time_of_flight_rocket(initial_velocity, launch_angle):
    g = 9.81
    return (2 * initial_velocity * np.sin(launch_angle)) / g

def time_of_flight_satellite(initial_velocity, launch_angle):
    g = 9.81
    return (2 * initial_velocity * np.sin(launch_angle)) / g

```

### Solution 
- Refactor the code to accept parameters as arguments, instead of hard-coding them.
- Extract common functionality into functions or methods.
- Refactor duplicated code into higher-level abstractions.
- Make use of utility functions to centralize common code and avoid duplication.

```python	
def time_of_flight(initial_velocity, launch_angle, gravity=9.81):
    """Compute time of flight for any projectile."""
    return (2 * initial_velocity * np.sin(launch_angle)) / gravity

# Usage
tof_ball = time_of_flight(30, np.pi/4)       # Time of flight for a ball
tof_rocket = time_of_flight(100, np.pi/3)    # Time of flight for a rocket
tof_mars_probe = time_of_flight(300, np.pi/6, gravity=3.71)  # Gravity adjusted for Mars
```	

## Key takeaways
- Extracting common functionality into functions or methods can help reduce duplication and improve code reuse.

<!-- 
:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more


:::
 -->
