
### Hard coding and magic numbers {.unnumbered}
This happens when constants and specific values are directly embedded into the code instead of being defined as variables or passed as arguments. Hard-coding makes the code less flexible and harder to maintain because changing the behavior requires modifying the source code rather than adjusting parameters. This smell is often noticed when you need to make changes to the source code in order to change the behaviour of the software at runtime.

:::{.callout-important collapse="true" appearance="simple"} 
## Example of hard coding and magic numbers
```python
def calculate_area(radius):
    # Hard-coded value of pi
    return 3.14 * radius * radius

def check_temperature(temperature):
    # Hard-coded magic numbers for temperature thresholds
    if temperature > 30:
        print("It's too hot!")
    elif temperature < 10:
        print("It's too cold!")
```
:::

::::{.callout-note appearance="simple"}
## Solution
Using configurable parameters or constants can make the code more adaptable and easier to maintain.

:::{.callout-tip collapse="true" appearance="simple"}
## Example solution with default parameters
```python
def calculate_area(radius, pi):
    return np.pi * radius * radius

def check_temperature(temperature, hot_threshold=30, cold_threshold=10):
    # If needed, you can use default values
    if temperature > hot_threshold:
        print("It's too hot!")
    elif temperature < cold_threshold:
        print("It's too cold!")
```
:::
::::
