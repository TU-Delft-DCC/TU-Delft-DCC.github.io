---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY/MM/DD]
# Uncomment and populate the next line accordingly
date: 2025/02/01

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Long Method

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Refactor long methods into smaller, more focussed functions
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
# - 

---

> "Functions should do one thing. They should do it well. They should do it only."
> 
> **Robert C. Martin** (Uncle Bob)

A "long method" is a common code where a method or function becomes overly long and handles multiple responsibilities at once. This makes the code hard to read, understand, test, and maintain. Long methods often indicate that a function is doing too much and may benefit from being broken into smaller, more focussed helper functions.

## Symptoms
A long method often:

- Performs multiple tasks rather than a single, well-defined responsibility.
- Has deeply nested control structures, making it harder to follow.
- Includes multiple sections of logic that could be extracted into separate functions.

### Example long method
Below is an example of a function that is doing too much:


::: panel-tabset
#### Python

```python
def load_data(filepath: str):
    # Check if data file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not found")
    
    _, extension = os.path.splitext(filepath)

    # Load data based on file extension    
    if extension == ".json":
        with open(filepath, "r") as file:
            # If file extension is .json: load json data
            data = json.load(file)
    elif extension == ".pickle":
        with open(filepath, "rb") as file:
            # If file extionsion is .pickle: load pickled data
            data = pickle.load(file)
    elif extension == ".csv":
        # If file extionsion is .csv: load cvs data
        data = read_csv(filepath)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
    
    # Verify content of data set
    if not isinstance(data, (list, dict, pd.DataFrame)):
        raise ValueError("Invalid data format")

    return data
```
#### MATLAB
```matlab
function data = load_data(filepath)
    if ~isfile(filepath)
        error('File not found');
    end
    
    [~, ~, ext] = fileparts(filepath);
    
    if strcmp(ext, '.json')
        data = read_json(filepath);
    elseif strcmp(ext, '.mat')
        data = read_mat(filepath);
    elseif strcmp(ext, '.csv')
        data = read_csv(filepath);
    else
        error('Unsupported file format: %s', ext);
    end
    
    if ~validate_data(data)
        error('Invalid data format');
    end
end
```

#### R
```r
load_data <- function(filepath) {
  if (!file.exists(filepath)) {
    stop("File not found")
  }
  
  ext <- tools::file_ext(filepath)
  
  if (ext == "json") {
    data <- read_json(filepath)
  } else if (ext == "rds") {
    data <- read_rds(filepath)
  } else if (ext == "csv") {
    data <- read_csv(filepath)
  } else {
    stop("Unsupported file format: ", ext)
  }
  
  if (!validate_data(data)) {
    stop("Invalid data format")
  }
  
  return(data)
}
```
:::

### Issues
- The function is handling file validation, data loading, and data verification, which are separate concerns.
- It is now difficult to test individual parts in isolation.
- Adding support for new file types requires modifying a large function.


## Solution
Identify logical blocks of code within the long method/function and extract them into separate methods with descriptive names. We should aim to make each method responsible for a singular task and compose more complex functionalities from modular components.

### Example solution long method

::: panel-tabset

#### Python
```python
def load_data(filepath: str) -> Data:
    verify_filepath(filepath: str)  
    data = read_data(filepath: str)
    verify_data(data)
    return data

# Helper function to verify file path
def verify_filepath(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not found")

# Helper function to read data from file based on its extension
def read_data(filepath: str) -> Data:
    # Extract file extension
    _, extension = os.path.splitext(filepath)
    
    # Create dictionary mapping file extensions to read functions
    data_types = {
        ".json": read_from_json,
        ".pickle": read_from_pickle,
        ".csv": read_from_csv,
    }

    # Select read function based on file extension
    try:
        read_function = data_types[extension]
    except KeyError:
        raise ValueError(f"Unsupported file format: {extension}")
    return data_types[extension](filepath)

# Placeholder for helper functions to read data from different file formats
def read_from_json(filepath: str): pass
def read_from_pickle(filepath: str): pass
def read_from_csv(filepath: str): pass
```

#### MATLAB
```matlab
function data = load_data(filepath)
    verify_filepath(filepath);
    data = read_data(filepath);
    verify_data(data);
end

function verify_filepath(filepath)
    if ~isfile(filepath)
        error('File not found');
    end
end

function data = read_data(filepath)
    [~, ~, ext] = fileparts(filepath);
    
    data_types = struct('.json', @read_json, ...
                         '.mat', @read_mat, ...
                         '.csv', @read_csv);
    
    if isfield(data_types, ext)
        read_function = data_types.(ext);
        data = read_function(filepath);
    else
        error('Unsupported file format: %s', ext);
    end
end

function data = read_json(filepath)
    fid = fopen(filepath, 'r');
    raw = fread(fid, inf, '*char')';
    fclose(fid);
    data = jsondecode(raw);
end

function data = read_mat(filepath)
    dataStruct = load(filepath);
    data = dataStruct.data;
end

function data = read_csv(filepath)
    data = readtable(filepath);
end

function verify_data(data)
    if ~iscell(data) && ~isstruct(data) && ~istable(data)
        error('Invalid data format');
    end
end
```

#### R
```r
load_data <- function(filepath) {
  verify_filepath(filepath)
  data <- read_data(filepath)
  verify_data(data)
  return(data)
}

verify_filepath <- function(filepath) {
  if (!file.exists(filepath)) {
    stop("File not found")
  }
}

read_data <- function(filepath) {
  ext <- tools::file_ext(filepath)
  
  data_types <- list(
    json = read_json,
    rds = read_rds,
    csv = read_csv
  )
  
  if (ext %in% names(data_types)) {
    return(data_types[[ext]](filepath))
  } else {
    stop("Unsupported file format: ", ext)
  }
}

read_json <- function(filepath) {
  jsonlite::fromJSON(filepath)
}

read_rds <- function(filepath) {
  readRDS(filepath)
}

read_csv <- function(filepath) {
  read.csv(filepath, stringsAsFactors = FALSE)
}

verify_data <- function(data) {
  if (!is.data.frame(data) && !is.list(data)) {
    stop("Invalid data format")
  }
}
```
:::

### Benefits of refactoring
- Each function now has a **single responsibility**, making the code easier to understand.
- Each function can be **tested independently**, making debugging more efficient.
- Adding support for new file types only requires modifying read_data, without changing the entire load_data function.

{{< fa thumbs-up >}} By breaking the long method into smaller helper functions, we improve the overall structure and maintainability of the code.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [eScience Center - Lesson on writing modular code](https://esciencecenter-digital-skills.github.io/good-practices-lesson/2-modular-code.html)
:::