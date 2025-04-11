---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-03

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Testing in R

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
- testing 
- R

---

R offers several testing frameworks, but the most widely used is the `testthat` package. It provides a straightforward way to write unit tests for your R code. The package is designed to be easy to use, even for those who are new to testing.

## Setting up `testthat`

To get started with `testthat`, you need to install the package and set up a testing structure in your R project. You need to have a `tests` directory in your project root. Inside this directory, you need a subdirectory called `testthat`. You can create this with:

```R
# Install packages if not already installed, and load them
install.packages(c("devtools", "testthat", "usethis", "covr"))
# and then run
usethis::use_testthat()
```

It will set up the `tests/testthat` directory and a `testthat.R` file. This file will contain the setup code for your tests. It will also add the `testthat` package to your package's `DESCRIPTION` file under the 'Suggests' field.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Please visit our [*Project structure*](../development_workflow/project_structure.md) guide for a recommendation on how to structure your R project.
:::

## Writing tests with `testthat`

Your files in the `tests/testthat` directory should be named `test-*.R`, where `*` is a descriptive name for the test. The `testthat.R` file will source all the test files in the `tests/testthat` directory, so you do not need to load them manually. They must match the same structure as the functions under your /R directory. For example, if you have a function `my_function()` in `R/my_function.R`, you should create a test file `tests/testthat/test-my_function.R` to test it.

So let's say we have a trivial function `count_tu_delft_faculties()` in your project that counts the number of faculties at TU Delft. TU Delft has 8 faculties, so the function should return 8.
You would create a file `R/count_tu_delft_faculties.R` with the following content:

```R
#' Count the number of faculties at TU Delft
#'
#' @return The number of faculties at TU Delft
#' @export
count_tu_delft_faculties <- function() {
    # This is a placeholder function
    return(8)
}
```
This function is a simple placeholder that returns the number of faculties at TU Delft. In a real-world scenario, this function would contain logic to count the faculties dynamically, perhaps by querying a database or an API. 

Then, you would create a test file `tests/testthat/test-count_tu_delft_faculties.R` to test this function. The test file should contain tests that check if the function returns the expected value (8 in this case).

```R
test_that("description of the test", {
  # Call the function
  result <- count_tu_delft_faculties()
  
  # Test that it returns the expected value
  expect_identical(result, 8)
  
  # We could add more expectations
  expect_type(result, "double")
  # etc.
})
```
You can use various `expect_*` functions to check the results of your code. 

## Running tests

You should run your tests regularly to ensure that your code is working as expected. You can run all the tests in your package using:

```R
devtools::test()
```
This will run all the tests in the `tests/testthat` directory and report any failures or errors. You can also run individual test files by specifying the file name:

```R
devtools::test_file("tests/testthat/test-count_tu_delft_faculties.R")
```
This will run only the tests in the specified file.

## Test coverage

To check the test coverage of your package, you can use `devtools::test_coverage()`. This will generate a report showing which part of your code is covered by tests and which are not. 

You can also use the `covr` package to have a more detailed control over coverage reporting. To check the coverage of your package:

```R
covr::package_coverage()
```
You can also use `covr::report()` to generate an HTML report of the coverage.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [R packages book - Testing](https://r-pkgs.org/testing-basics.html)
- [Introduction to testing R code](https://stirlingcodingclub.github.io/code_testing/testing_notes.html)
- [`testthat` package](https://testthat.r-lib.org/)
- [`covr` package](https://covr.r-lib.org/)
:::