---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
#date: YYYY-MM-DD

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
#title: Title of the document

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
#categories: 
# - 
# - 

---


## What to test?
In designing test cases for research software, it can be useful to conceptually differentiate between tests that verify **the technical correctness** of the code and tests that check **the scientific validity** of the results. With technical software tests, you can for example check whether a function behaves correctly for multiple input data types and produces errors and exceptions accordingly. With a scientific test, you could compare the outcome of a function to known experimental results. 

The following questions can help you decide what to test in your software:

- How can I ensure the algorithms and mathematical models implemented in the software are correct?
- How can I verify that the input data types, formats, and ranges adhere to expected standards and constraints?
- How does the software behave at boundary conditions and extreme values of input parameters?
- How does the software perform under varying workloads and dataset sizes, and is it scalable for large-scale simulations or data processing tasks?
- How do I compare the software's results against existing literature, experimental data, or validated simulations to validate their accuracy?

### Types of tests
In writing tests for research software, we can differentiate between four types of tests: **unit tests**, **integration tests**, **regression tests**, and **end-to-end tests**.

#### Unit tests
A unit test is a type of test where individual units or components of the software application are tested in isolation from the rest of the application. A unit can be a function, method, or class. The main purpose of unit testing is to validate that each unit of the software performs as designed.

#### Integration tests
Integration testing is a level of software testing where individual units are combined and tested as a group. The purpose is to verify that the units work together as expected and that the interfaces between them function correctly. Integration tests aims to expose defects in the interactions between integrated components.

#### Regression tests
Regression testing aims to verify that recent code changes haven't adversely affected existing features or functionality. It involves re-running previously executed test cases to ensure that the software still behaves as expected after modifications. The primary purpose of regression testing is to catch unintended side effects of code changes and ensure that new features or bug fixes haven't introduced regressions or broken existing functionality elsewhere in the code. Regression tests can include both unit tests and integration tests, as well as higher-level tests such as system tests. They are a good place to test the scientific validity of the software.

#### End-to-end tests
End-to-end testing is focused on validating the entire system from start to finish, simulating real use cases. The goal is to verify the software functions as a whole from the user's perspective.

## Getting started with testing

### Designing a test case 
For more complex integration, regression, or end-to-end tests, it can be useful to first describe the test case in words.

1. **Description:** _Description of test case_
1. **Preconditions:** _Conditions that need to be met before executing the test case_
1. **Test Steps:** _To execute test cases, you need to perform some actions. Mention all the test steps in detail and the order of execution_
1. **Test Data:** _If required, list data that needed to execute the test cases_
1. **Expected Result:** _The result we expect once the test cases are executed_
1. **Postcondition:** _Conditions that need to be achieved when the test case was successfully executed_

### Testing strategy

1. Learn the basics of testing for your programming language.
2. Choose and setup a testing framework.
3. Practice with writing unit tests for small functions or methods.
4. Identify critical parts of your software that requires testing and write tests to verify its proper technical and scientific functioning.
5. Incrementally add tests. Whenever you add or change a function, try to write a test to cover the code. 


::: {.callout-tip}
## Tips and good practices
- Large functions are difficult to test. Aim to write modular code consisting of small functions.
- Ensure that each test case is independent and does not rely on the state of other tests or external factors.
- Limit the number of assert statements per test. The execution of a test function is terminated after an assert statement fails.
- Aim for comprehensive test coverage to ensure that **critical parts** of your codebase are thoroughly tested. A good benchmark is to test at least 70% of your code base with unit tests.
- Design tests to run quickly to encourage frequent execution during development and continuous integration. A test that takes a long time to run is less likely to be executed frequently.
- Store your tests in a separate folder, either in the root of your repository called `tests/` or in `src/tests/`.
:::