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
title: Many arguments

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: 
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

When a function or method takes many parameters (inputs), it can become difficult to understand, maintain, and test. If a function needs a lot of information to work, it might be doing too many things at once, and this can confuse programmers or lead to mistakes. Refactoring the code to reduce the number of parameters or organizing the data in a more logical way can make the code easier to read and work with.

## Symptoms
- Functions or methods with many parameters, especially if some of them are not used within the function.
- Functions with long and confusing parameter lists, which are hard to remember or use correctly.
- Code that’s hard to change or update because of too many parameters being passed around.
- Functions often require the same set of parameters, which can be grouped together logically.

:::{.callout-warning icon="false"}
## A good rule of thumb
- 1-3 parameters: Generally fine.
- 4-5 parameters: Might be acceptable if needed, but review if they can be grouped.
- 6+ parameters: Strongly consider refactoring the function or method.
:::

## Example - Long parameter list
Here's an example of a function that takes many parameters:

::: {.panel-tabset}

## Python
```python
def process_machine_operation(machine_id, temperature, pressure, speed, duration):
    # Perform machine operation
    print("Machine ID:", machine_id)
    print("Temperature:", temperature)
    print("Pressure:", pressure)
    print("Speed:", speed)
    print("Operation Duration:", duration)

# Usage
process_machine_operation(
    machine_id="M001",
    temperature=100.5,
    pressure=200.0,
    speed=1500.0,
    duration=5.0)
```

## R
```r
process_machine_operation <- function(machine_id, temperature, pressure, speed, duration) {
  # Perform machine operation
  print(paste("Machine ID:", machine_id))
  print(paste("Temperature:", temperature))
  print(paste("Pressure:", pressure))
  print(paste("Speed:", speed))
  print(paste("Operation Duration:", duration))
}

# Usage
process_machine_operation(
  machine_id = "M001",
  temperature = 100.5,
  pressure = 200.0,
  speed = 1500.0,
  duration = 5.0
)
```

:::

This function takes a lot of information at once: the machine ID, temperature, pressure, speed, and duration. If the function grows even more complex, it will become very hard to keep track of what each parameter means, and it could make the code difficult to maintain.


### Solutions
To solve this problem, we can do one or both of the following:

1. **Simplify the Function:** Break the function into smaller parts that do one thing each.
2. **Use Objects to Group Related Data:** Instead of passing many individual pieces of information, we can group them together into one object or structure that holds related information.


#### 1. Using a Dataclass (or S3 Classes in R)

::: {.panel-tabset}

## Python
```python
from dataclasses import dataclass

# Create a dataclass to group the machine operation parameters
@dataclass
class MachineOperationData:
    machine_id: str
    temperature: float
    pressure: float
    speed: float
    duration: float
```

## R
```r
# Create an S3 class to group the machine operation parameters
MachineOperationData <- function(machine_id, temperature, pressure, speed, duration) {
  structure(
    list(
      machine_id = machine_id,
      temperature = temperature,
      pressure = pressure,
      speed = speed,
      duration = duration
    ),
    class = "MachineOperationData"
  )
}
```

:::


Now, instead of passing five separate parameters to our function, we'll just pass one object that holds everything. Next, we change our `process_machine_operation` function to accept this new object, making it simpler and cleaner.


::: {.panel-tabset}

## Python
```python
def process_machine_operation(operation_data):
    # Perform machine operation
    print("Machine ID:", operation_data.machine_id)
    print("Temperature:", operation_data.temperature)
    print("Pressure:", operation_data.pressure)
    print("Speed:", operation_data.speed)
    print("Operation Duration:", operation_data.duration)

# Usage
operation_data = MachineOperationData(
    machine_id="M001",
    temperature=100.5,
    pressure=200.0,
    speed=1500.0,
    duration=5.0)

process_machine_operation(operation_data)
```
:::{.callout-tip}
**Python**: You can combine dataclasses with data validation through [**Pydantic**](https://docs.pydantic.dev/latest/).
:::

## R
```r
process_machine_operation <- function(operation_data) {
  # Perform machine operation
  print(paste("Machine ID:", operation_data$machine_id))
  print(paste("Temperature:", operation_data$temperature))
  print(paste("Pressure:", operation_data$pressure))
  print(paste("Speed:", operation_data$speed))
  print(paste("Operation Duration:", operation_data$duration))
}

# Usage
operation_data <- MachineOperationData(
  machine_id = "M001",
  temperature = 100.5,
  pressure = 200.0,
  speed = 1500.0,
  duration = 5.0
)

process_machine_operation(operation_data)
```


:::{.callout-tip}

**R**: S3 is R's lightweight object-oriented system. For more advanced OOP features and validation, consider using the `R6` package or the `S7` package.
:::

:::


#### 2. Divide and conquer

Although using a single dataclass is a good start, we don't want our data structure to become too big and complicated. If the dataclass starts holding too much data, it can make the code harder to understand. Instead, we can break it into smaller, simpler data classes that work together. For example:

::: {.panel-tabset}

## Python
```python
@dataclass
class Machine:
    machine_id: str
    manufacturer: str

@dataclass
class OperationParameters:
    temperature: float
    pressure: float
    speed: float
    duration: float

@dataclass
class EnvironmentalConditions:
    humidity: float
    altitude: float

@dataclass
class MachineOperationData:
    machine: Machine
    operation_parameters: OperationParameters
    environmental_conditions: EnvironmentalConditions

def process_machine_operation(operation_data):
    print("Machine ID:", operation_data.machine.machine_id)

    # Implement machine operation
```

## R
```r
# Define constructor functions for each component
Machine <- function(machine_id, manufacturer) {
  structure(
    list(machine_id = machine_id, manufacturer = manufacturer),
    class = "Machine"
  )
}

OperationParameters <- function(temperature, pressure, speed, duration) {
  structure(
    list(temperature = temperature, pressure = pressure,
         speed = speed, duration = duration),
    class = "OperationParameters"
  )
}

EnvironmentalConditions <- function(humidity, altitude) {
  structure(
    list(humidity = humidity, altitude = altitude),
    class = "EnvironmentalConditions"
  )
}

MachineOperationData <- function(machine, operation_parameters, environmental_conditions) {
  structure(
    list(machine = machine,
         operation_parameters = operation_parameters,
         environmental_conditions = environmental_conditions),
    class = "MachineOperationData"
  )
}

# Usage with composed S3 classes
operation_data <- MachineOperationData(
  machine = Machine("M001", "TechCorp"),
  operation_parameters = OperationParameters(100.5, 200.0, 1500.0, 5.0),
  environmental_conditions = EnvironmentalConditions(65.0, 500.0)
)

process_machine_operation <- function(operation_data) {
  print(paste("Machine ID:", operation_data$machine$machine_id))

  # Implement machine operation
}
```

:::

Here, instead of having one large `MachineOperationData` class, we've divided it into smaller pieces. Each class now represents a specific part of the data, which can then be used individually or grouped together as needed. This approach keeps everything organized and easy to work with.

## Key takeaways
- Don’t pass too many parameters. If a function requires many parameters, it’s a sign that the function might be doing too much. Group related data together to reduce the number of parameters or break the function into smaller parts.
- Use classes or dataclasses to help organize related data into neat packages that are easy to pass around in your code.
- Keep things simple: Don’t let your classes become too big. If necessary, break them down into smaller parts, but keep them organized and easy to understand.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [RealPython - Data Classes](https://realpython.com/python-data-classes/)
- [R S3 Classes](https://adv-r.hadley.nz/s3.html)
:::