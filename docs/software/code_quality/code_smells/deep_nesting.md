
### Deep nesting {.unnumbered}
Deep nesting occurs when there are too many levels of indentation in the code, making it harder to understand, maintain, and debug. It can lead to spaghetti code and decreased readability. 

:::{.callout-important collapse="true" appearance="simple"} 
## Example deep nesting
```python
def validate_model_convergence(model: Model) -> bool:
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
:::


::::{.callout-note appearance="simple"}
## Solution

Refactoring to reduce nesting levels and employing techniques like early returns or breaking down complex logic into smaller, more modular functions can help alleviate this code smell.


:::{.callout-tip collapse="true" appearance="simple"}
## Example solution 1 deep nesting
```python
def validate_model_convergence(model: Model) -> bool:
    if model.convergence <= 1:
        return False
    if model.convergence >= 0.1:
        return False
    if model.secondary_condition == False
        return False
    return True
        
```
:::

:::{.callout-tip collapse="true" appearance="simple"} 
## Example solution 2 deep nesting

Or alternatively using the `any/all` built-in functions
```python
def validate_model_convergence(model: Model) -> bool:
    return all([
        model.convergence > 1,
        model.convergence < 0.1,
        model.secondary_condition == True,
    ])

```

with the equivalent in MATLAB
```matlab 
function result = validate_model_convergence(model)
    result = all([model.convergence > 1, model.convergence < 0.1, model.secondary_condition == true]);
end
```

:::
::::