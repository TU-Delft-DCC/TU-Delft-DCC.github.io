---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-26

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Testing strategy

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Guidelines for researchers new to testing and experienced test writers.
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: ChatGTP
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
# - testing
# - 
---

In designing test cases for research software, it can be useful to conceptually differentiate between tests that verify **the technical correctness** of the code and tests that check **the scientific validity** of the results. With technical software tests, you check whether a function behaves as expected. With a scientific test, you compare the outcome of a function to known (experimental) scientific results. 

The following questions can help you decide what to test in your software:

- How can I ensure the algorithms and mathematical models implemented in the software are correct?
- How can I verify that the input data types, formats, and ranges adhere to expected standards and constraints?
- How does the software behave at boundary conditions and extreme values of input parameters?
- How does the software perform under varying workloads and dataset sizes, and is it scalable for large-scale simulations or data processing tasks?
- How do I compare the software's results against existing literature, experimental data, or previous simulations to check their accuracy?

### Roadmap to testing

::: {.panel-tabset}

## New to testing

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 1. Familiarize yourself with the basics

Begin by learning a testing framework that is well-suited for your programming language; for example, you might explore `pytest` if you are using Python. It is also important to understand the basic types of tests, focusing primarily on unit tests and simple integration tests.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 2. Identify critical components in your code
Take the time to inspect your codebase and determine which parts are most important or particularly prone to error. These are the areas where you should focus your testing efforts.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 3. Start small
Begin by writing minimal (unit) tests for individual functions or modules. Creating tests based on expected inputs and outputs will help confirm that your code behaves as intended. The primary goal at this stage is to understand the testing process rather than aiming for complete coverage from the start.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 4. Incrementally expand the number of tests
As you introduce new functionality, adopt an approach by writing tests alongside your new code. Over time, gradually add tests to your existing code -- especially when you make changes or improvements -- to steadily increase overall test coverage and improve the reliability of your software. Make sure to focus on testing the critical parts of your codebase first.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 5. Refactor your code for testability
If you find it difficult to write tests for your codebase, consider [refactoring](/docs/software/code_quality/refactoring.md) it into smaller, more testable units. Clear documentation and comments on your functions will further aid in writing tests by providing a well-defined understanding of each component's intent.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 6. Automate and adopt
Finally, add automated testing to your development workflow by using a continuous integration tool to run tests automatically with each code change. Establishing a regular habit of testing will, over time, lead to significant improvements in the quality and reliability of your research code.
:::

## Familiar with testing

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 1. Develop a testing strategy
For researchers already experienced with testing, it is useful to develop a testing strategy. Start by adopting the test pyramid approach: ensure that all core functions and algorithms are covered by unit tests, verify that modules interact correctly with integration tests, and, when applicable, use end-to-end tests to simulate real-world user workflows. Regularly running regression tests is also important to catch any unintended side effects of code changes.

Aim for comprehensive test coverage to ensure that critical parts of your codebase are thoroughly tested. A good benchmark is to test at least 70% of your code base with unit tests.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 2. Adopt a practice of writing tests first
Consider methodologies such as Test-Driven Development (TDD) into your workflow. With TDD, you write tests before you write the actual code to define the desired behavior, ensure clear specifications, and obtain immediate feedback.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 3. Research-specific testing
In a research context, certain quality measures become particularly important. Prioritize reproducibility by writing tests that verify experiments yield consistent outputs for a given dataset and configuration. If your code relies on statistical methods, use fixed random seeds to ensure reproducibility across different runs. Additionally, consider implementing validation tests that compare your results against known benchmarks or experimental data.
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 4. Consider advanced testing practices
- **Coverage Analysis:**  
  Employ code coverage tools to identify untested paths and critical areas that require additional testing.
- **Parameterization:**  
  Run tests with a range of inputs to validate robustness across different scenarios.
- **Error Handling:**
  Verify that your code behaves as expected when encountering errors.
- **Fixtures:**
  Use fixtures to set up a consistent and reusable testing environment.
- **Mocking:**  
  Use mocks to simulate external systems or heavy computations, isolating tests for faster feedback.
- **Tagging and Filtering:**
  Organize tests into categories and run specific subsets based on tags or filters.
{{< fa up-right-from-square>}} [Advanced testing practices](/docs/software/testing/intermediate.md)
:::

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## 5. Integrate with CI/CD
Finally, integrate your testing processes into a continuous integration/deployment pipeline. Automate your test runs so that every code commit triggers a suite of tests to catch issues early in the development cycle. Monitor test performance and code coverage over time to continuously refine and enhance your testing strategy, ensuring a high level of quality and reliability in your research software.
:::
:::

