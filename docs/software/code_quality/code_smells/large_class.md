---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-04

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Large Classes

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

A **monolithic design** is where an entire system is built as a single, tightly coupled unit without clear separation of responsibilities or modularization. This often keads to large, complex classes that hadle multiple responsibilities, making the codebase harder to understand, modify, and maintain.


## Symptoms
- Large classes that try to handle too many responsibilities.
- Code duplication across multiple parts of the system.
- Difficulties in testing because changes in one part of the code affect others.
- Limited reusability of components due to tight coupling.
- Small modifications require extensive changes across the codebase.

## Example - Violating the Single Responsibility Principle
In this example, we are writing code for a temperature monitoring system. A bad design would be putting everything inside one big class:

```python
class SensorSystem:
    def __init__(self):
        self.temperature = 0

    def read_temperature(self):
        # Simulated temperature reading
        self.temperature = 25  
        print(f"Temperature: {self.temperature}°C")

    def log_temperature(self):
        # Simulated logging
        print(f"Logging temperature: {self.temperature}°C")

    def send_alert(self):
        if self.temperature > 30:
            print("ALERT: High temperature detected!")

def main():
    sensor_system = SensorSystem()
    sensor_system.read_temperature()
    sensor_system.log_temperature()
    sensor_system.send_alert()

if __name__ == "__main__":
    main()

```

### Solution
We should split this class into smaller, focused classes:
- `TemperatureSensor` – Handles sensor readings.
- `Logger` – Handles logging.
- `AlertSystem` – Handles alerts.

1. Follow the **Single Responsibility Principle (SRP)** -  Ensure that each class has only one job. If a class is doing too much, split its responsibilities into separate classes.
2. Use **dependency injection**: Reduce class coupling by calling dependencies as arguments (injecting dependencies) rather than hard-coding them. This promotes modularity and testability, as well as making it easier to swap out components.


```python
class TemperatureSensor:
    def read_temperature(self):
        # Simulated sensor reading
        return 25  

class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class AlertSystem:
    def send_alert(self, temperature):
        temp_threshold = 30
        if temperature > temp_threshold:
            print("⚠️ ALERT: High temperature detected!")

class SensorSystem:
    def __init__(self, sensor, logger, alert_system):
        self.sensor = sensor
        self.logger = logger
        self.alert_system = alert_system

    def monitor_temperature(self):
        temperature = self.sensor.read_temperature()
        self.logger.log(f"Temperature: {temperature}°C")
        self.alert_system.send_alert(temperature)

# Dependency Injection
def main():
    sensor = TemperatureSensor()
    logger = Logger()
    alert_system = AlertSystem()
    sensor_system = SensorSystem(sensor, logger, alert_system) # dependencies injected

    sensor_system.monitor_temperature()

if __name__ == "__main__":
    main()
``` 

**Why is this better?**

- No unnecessary mixing of concerns.
- Easily swap different logging or alerting mechanisms.
- Each component can be tested in isolation.

## Key Takeaways
- If your class is doing too many things, split it into smaller, focused classes.
- Use dependency injection to keep components flexible and testable.
- Following modular design makes your code easier to understand, modify, and reuse.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [ArjanCodes - Dependency Injection Best Practices](https://arjancodes.com/blog/python-dependency-injection-best-practices/)

:::