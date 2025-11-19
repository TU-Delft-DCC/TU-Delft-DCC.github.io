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
title: Inappropriate Intimacy

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
  - Software
  - Refactoring
  - Tight Coupling

---

This code smell occurs when one part of the system knows too much about the internal details of another, leading to **tight coupling**. When components are too dependent on each other, it becomes difficult to modify or extend the system without breaking other parts.

A good design principle to follow is the [**Law of Demeter**](https://en.wikipedia.org/wiki/Law_of_Demeter), also known as the **"Don't talk to strangers"** rule. It suggests that a module should only interact with its direct dependencies rather than deeply nested objects.

## Symptoms
- A class accesses properties of another object’s properties, exposing too much detail.
- Changes in one part of the code require changes in multiple other places.
- Because multiple classes depend on each other’s internal structures, small changes can cause unintended issues.

## Example - Violating Law of Demeter
In this example, a `SensorSystem` directly accesses the `TemperatureSensor` internal attributes, creating tight coupling.
```python
class TemperatureSensor:
    def __init__(self, temperature):
        self.temperature = temperature  # Internal detail exposed

class SensorSystem:
    def __init__(self, sensor):
        self.sensor = sensor

    def get_temperature(self):
        # Law of Demeter violation: Directly accessing sensor's attribute
        return self.sensor.temperature

# Usage
sensor = TemperatureSensor(25)
system = SensorSystem(sensor) 
temperature = system.get_temperature()
print(temperature)  # 25
```
**Problem:** The `SensorSystem` class depends on the internal structure of `TemperatureSensor`. If the way temperature is stored changes (e.g., a new sensor model), `SensorSystem` must also change.


### Solutions

#### Example solution - Using getter methods
Instead of directly accessing attributes, define **getter methods** in `TemperatureSensor` to limit exposure.

```python
class TemperatureSensor:
    def __init__(self, temperature):
        self._temperature = temperature  # Use a private variable

    def get_temperature(self):
        return self._temperature  # Encapsulated access

class SensorSystem:
    def __init__(self, sensor):
        self.sensor = sensor

    def get_temperature(self):
        return self.sensor.get_temperature()  # Indirect access through method

# Usage
sensor = TemperatureSensor(25)
system = SensorSystem(sensor)
print(system.get_temperature())  # 25
```
**Why is this better?**

- The `SensorSystem` no longer needs to know the internal structure of `TemperatureSensor`.
- If `TemperatureSensor` changes, only `get_temperature()` needs to be updated, not every place it’s used.


#### Example solution - Removing the dependency
A better design is to pass only the needed data instead of an entire object.
```python
class SensorSystem:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature  # Works directly with the value

# Usage
temperature = 25
system = SensorSystem(temperature)
print(system.get_temperature())  # 25
```
**Why is this better?**

- `SensorSystem` no longer depends on `TemperatureSensor`, making it more modular and reusable.
- Works even if the source of temperature data changes (e.g., from a file, API, or another sensor).

:::{.callout-tip appearance="simple"}
Balance between dependecy injection and encapsulation. If the data is simple and does not require complex operations, pass it directly. If the data is complex or requires additional logic, encapsulate it in a class.
:::

## Key Takeaways
- Follow the Law of Demeter - Only interact with direct dependencies.
- Encapsulate data - Use getters and setters to access and modify data.
- Reduce dependencies - pass only the necessary information to other components.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [RealPython - Python Classes](https://realpython.com/python-classes/)
- [RealPython - Getters and Setters](https://realpython.com/python-getter-setter/)
:::