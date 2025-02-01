
### The "long method" {.unnumbered}
A "long method" is a common code smell that refers to a method or function that is overly long, handling multiple responsibilities at once. This makes the code hard to read, understand, test, and maintain. Long methods often indicate that the method is doing too much and may benefit from being broken into smaller, more focussed helper functions.

:::{.callout-important collapse="true" appearance="simple"}
## Example long method
```python
def load_data(filepath: str):
    # Check if data file exists
    # If file extension is .json: load json data
    # If file extionsion is .pickle: load pickled data
    # If file extionsion is .csv: load cvs data
    # Verify content of data set
```
:::

::: {.callout-note appearance="simple"}
## Solution
Identify logical blocks of code within the long method/function and extract them into separate methods with descriptive names. We should aim to make each method responsible for a singular task and compose more complex functionalities from modular components.

> "Functions should do one thing. They should do it well. They should do it only."
> 
> **Robert C. Martin**

::: {.callout-tip collapse="true" appearance="simple"}
## Example solution long method

```python
def load_data(filepath: str) -> Data:
    verify_filepath(filepath: str)  
    data = read_data(filepath: str)
    verify_data(data)
    return data

# Helper function to verify validity of filepath
def verify_filepath(filepath: str): pass

# Helper function to read data from file based on its extension
def read_data(filepath: str) -> Data:
    _, extension = os.path.splitext(filepath)
    data_types = {
        ".json": read_from_json,
        ".pickle": read_from_pickle,
        ".csv": read_from_csv,
    }

    try:
        read_function = data_types[extension]
    except KeyError:
        raise ValueError(f"Unsupported file format: {extension}")
    return data_types[extension](filepath)

# Helper functions to read data from different file formats
def read_from_json(filepath: str): pass
def read_from_pickle(filepath: str): pass
def read_from_csv(filepath: str): pass

# Helper function to verify the content of the data set
def verify_data(data: Any) -> bool: pass
```
:::
:::