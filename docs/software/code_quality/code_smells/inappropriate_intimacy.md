
### Inappropriate intimacy {.unnumbered}
This smell occurs when one class knows too much about the internal structure of another class, leading to tight coupling. Tight coupling makes the code harder to understand, maintain, and refactor because changes to one class can have ripple effects on other classes.

:::{.callout-important collapse="true" appearance="simple"}
## Example of violating Law of Demeter
```python
class GroundStation:
    def __init__(self, station_name):
        self.station_name = station_name
        self.kite = Kite()

    def get_kite_name(self):
        # Violation of the Law of Demeter:
        # Accessing a property of an object returned by another object
        return self.kite.name        

class Kite:
    def __init__(self):
        self.name = "Kite_1"

# Usage
ground_station = GroundStation("TUD")
kite_name = ground_station.get_kite_name()
```
:::

::::{.callout-note appearance="simple"}
## Solution
Follow the principles of least knowledge ([**Law of Demeter**](https://en.wikipedia.org/wiki/Law_of_Demeter)). Each unit should have only limited knowledge about other units, i.e. don't talk to strangers.

:::{.callout-tip collapse="true" appearance="simple"}
## Example solution - using a getter method
```python
class GroundStation:
    def __init__(self, station_name, kite):
        self.station_name = station_name
        self.kite = kite

    def get_kite_name(self):
        return self.kite.get_name()

class Kite:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name    

# Usage
kite = Kite("Kite_1")
ground_station = GroundStation("TUD", kite)
kite_name = ground_station.get_kite_name()
```
:::

:::{.callout-tip collapse="true" appearance="simple"}
## Example solution - limiting access
```python
class GroundStation:
    def __init__(self, station_name, kite_name):
        self.station_name = station_name
        self.kite_name = kite_name

    def get_kite_name(self):
        return self.kite_name

# Usage
ground_station = GroundStation("TUD", "Kite_1")
kite_name = ground_station.get_kite_name()
```
:::

::::
