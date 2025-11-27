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
title: Dead code

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
author_2: Manuel Garcia

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
  - Dead Code

---

Dead code refers to unused or unreachable code that remains in the codebase but serves no functional purpose. Commented-out code consists of inactive code blocks that developers have disabled rather than deleting. Both contribute to clutter and reduce maintainability.

## Symptoms

- Unused variables or functions.
- Conditional blocks that never execute.
- Large blocks of commented-out code.
- Using comments to disable code to change the behavior of the code.

:::{.callout-tip}
Do not use comments to change the behavior of the code. Instead, make use of input parameters or configuration settings to control the behavior of the code.
:::

## Example - Dead code

Unreachable or unused code that remains in the codebase but serves no purpose.

::: {.panel-tabset}

## Python

```python
def calculate_discount(price, customer_type):
    if customer_type == "premium":
        discount = 0.20
    elif customer_type == "standard":
        discount = 0.10
    else:
        discount = 0

    final_price = price * (1 - discount)

    # Dead code - this variable is never used
    unused_result = final_price * 2

    # Dead code - this function is never called
    def log_transaction():
        print("Transaction logged")

    return final_price
```

## R

```r
calculate_discount <- function(price, customer_type) {
  if (customer_type == "premium") {
    discount <- 0.20
  } else if (customer_type == "standard") {
    discount <- 0.10
  } else {
    discount <- 0
  }

  final_price <- price * (1 - discount)

  # Dead code - this variable is never used
  unused_result <- final_price * 2

  # Dead code - this function is never called
  log_transaction <- function() {
    print("Transaction logged")
  }

  return(final_price)
}
```

:::

#### Issues

- `unused_result` is computed but never returned or used, wasting memory and computation.
- `log_transaction()` is defined but never called, adding unnecessary clutter.
- Dead code confuses readers about the actual functionality of the function.
- Makes refactoring and maintenance more difficult.

### Solution - Dead code

Remove unused code completely. Use version control (e.g., Git) to restore it if needed later.

::: {.panel-tabset}

## Python

```python
def calculate_discount(price, customer_type):
    if customer_type == "premium":
        discount = 0.20
    elif customer_type == "standard":
        discount = 0.10
    else:
        discount = 0

    final_price = price * (1 - discount)
    return final_price
```

## R

```r
calculate_discount <- function(price, customer_type) {
  if (customer_type == "premium") {
    discount <- 0.20
  } else if (customer_type == "standard") {
    discount <- 0.10
  } else {
    discount <- 0
  }

  final_price <- price * (1 - discount)
  return(final_price)
}
```

:::

## Example - Commented-out code

Disabling code with comments instead of deleting it or using configuration settings to control behavior.

::: {.panel-tabset}

## Python

```python
def process_data(data, debug=False):
    # Debug logging is controlled by comments instead of a parameter
    # print("Processing started")  # Commented-out for production

    result = []
    for item in data:
        value = item * 2
        # print(f"Processing: {item} -> {value}")  # Commented-out debug statement
        result.append(value)

    # Entire feature disabled via commenting - no way to re-enable without editing code
    # if debug:
    #     with open("log.txt", "w") as f:
    #         f.write(str(result))

    return result
```

## R

```r
process_data <- function(data, debug = FALSE) {
  # Debug logging is controlled by comments instead of a parameter
  # cat("Processing started\n")  # Commented-out for production

  result <- c()
  for (item in data) {
    value <- item * 2
    # cat(sprintf("Processing: %d -> %d\n", item, value))  # Commented-out debug statement
    result <- c(result, value)
  }

  # Entire feature disabled via commenting - no way to re-enable without editing code
  # if (debug) {
  #   write.table(result, file = "log.txt", quote = FALSE, row.names = FALSE)
  # }

  return(result)
}
```

:::

#### Issues

- Commented-out code is confusing: is it there for a reason or was it forgotten?
- It blocks maintenance - developers won't refactor around dead code they don't understand.
- The `debug` parameter exists but is never used because the logging is disabled via comments.
- Makes version history harder to follow with unclear code blocks.

### Solution - Commented-out code

Use [input parameters or configuration settings](./hardcoded_values.md) to control behavior (execution) instead of commenting out code.

::: {.panel-tabset}

## Python

```python
def process_data(data, debug=False):
    """
    Process data with optional debug logging.

    Parameters:
    -----------
    data : list
        The data to process
    debug : bool
        If True, enable debug output
    """
    if debug:
        print("Processing started")

    result = []
    for item in data:
        value = item * 2
        if debug:
            print(f"Processing: {item} -> {value}")
        result.append(value)

    if debug:
        with open("log.txt", "w") as f:
            f.write(str(result))

    return result

# Usage
process_data([1, 2, 3], debug=False)      # Production mode
process_data([1, 2, 3], debug=True)       # Debug mode
```

## R

```r
process_data <- function(data, debug = FALSE) {
  # Process data with optional debug logging
  #
  # Parameters:
  # -----------
  # data : vector
  #   The data to process
  # debug : logical
  #   If TRUE, enable debug output

  if (debug) {
    cat("Processing started\n")
  }

  result <- c()
  for (item in data) {
    value <- item * 2
    if (debug) {
      cat(sprintf("Processing: %d -> %d\n", item, value))
    }
    result <- c(result, value)
  }

  if (debug) {
    write.table(result, file = "log.txt", quote = FALSE, row.names = FALSE)
  }

  return(result)
}

# Usage
process_data(c(1, 2, 3), debug = FALSE)   # Production mode
process_data(c(1, 2, 3), debug = TRUE)    # Debug mode
```

:::

## Key takeaways

- **Delete dead code immediately** - use version control to recover it if needed later.
- **Do not use comments to disable code** - use parameters, configuration settings, or conditional logic instead.
- **Commit removals meaningfully** - explain in the commit message why code was removed.
- **Keep code clean** - cluttered code with dead sections is harder to understand and maintain.
