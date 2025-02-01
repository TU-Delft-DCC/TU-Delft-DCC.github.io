### Monolithic design and large classes {.unnumbered}

A monolithic design is where the entire application or system is built as a single, tightly coupled unit, without clear separation of responsibilities or modularization. Often, this smell is encountered as large classes and indicates that a single class in the codebase is responsible for handling too many responsibilities or has grown too complex.

:::{.callout-important collapse="true" appearance="simple"}
## Example of violating the Single Responsibility Principle
In this example, the `KiteController` class is responsible for both adjusting the kite angle based on wind speed and generating power from the kite. 

```python
class WindSensor:
    def measure_wind_speed(self):
        # Placeholder for wind speed measurement
        return 10

class KiteController:
    def __init__(self):
        self.wind_sensor = WindSensor()

    def adjust_kite_angle(self):
        wind_speed = self.wind_sensor.measure_wind_speed()
        # Logic to adjust kite angle based on wind speed
        if wind_speed > 15:
            print("Strong wind detected. Adjusting kite angle for stability.")
        else:
            print("Moderate wind detected. Maintaining kite angle.")

    def generate_power(self):
        # Logic to generate power based on kite angle and wind speed
        wind_speed = self.wind_sensor.measure_wind_speed()
        if wind_speed > 15:
            print("Generating high power from kite.")
        else:
            print("Generating moderate power from kite.")

def main():
    kite_controller = KiteController()
    kite_controller.adjust_kite_angle()
    kite_controller.generate_power()

if __name__ == "__main__":
    main()
```
:::

::::{.callout-note appearance="simple"}
## Solution
- Follow the **Single Responsibility Principle (SRP)** -  Ensure that each class has only one job. If a class is doing too much, split its responsibilities into separate classes.
- Use **dependency injection**: Reduce class coupling by calling dependencies as arguments (injecting dependencies) rather than hard-coding them. This promotes modularity and testability, as well as making it easier to swap out components.



:::{.callout-tip collapse="true" appearance="simple"}
## Example solution with dependency injection 
The `main` function serves as the entry point and demonstrates dependency injection by creating instances of `WindSensor`, `KiteController`, and `PowerGenerationSystem` externally and passing them to each other's constructors. 

```python
class WindSensor:
    def measure_wind_speed(self):
        # Simulate wind speed measurement
        return 10  # Placeholder value for demonstration purposes

class KiteController:
    def __init__(self, wind_sensor):
        self.wind_sensor = wind_sensor

    def adjust_kite_angle(self):
        wind_speed = self.wind_sensor.measure_wind_speed()
        # Logic to adjust kite angle based on wind speed
        if wind_speed > 15:
            print("Strong wind detected. Adjusting kite angle for stability.")
        else:
            print("Moderate wind detected. Maintaining kite angle.")

class PowerGenerationSystem:
    def __init__(self, kite_controller):
        self.kite_controller = kite_controller

    def generate_power(self):
        self.kite_controller.adjust_kite_angle()
        # Logic to generate power based on kite angle and wind speed
        print("Generating power from kite.")

# Dependency Injection
def main():
    wind_sensor = WindSensor() 
    kite_controller = KiteController(wind_sensor) # Through dependency injection, the WindSensor can be easily replaced with another sensor
    power_generation_system = PowerGenerationSystem(kite_controller)

    power_generation_system.generate_power()

if __name__ == "__main__":
    main()
```
:::
::::