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
title: Types of tests

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Different types of tests to ensure your software works as expected.
hide-description: true

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
# - testing
# - 

---

In writing tests for research software, we often differentiate between four types of tests: **unit tests**, **integration tests**, and **end-to-end tests**. In addition, **regression tests** are used to ensure that recent code changes haven't adversely affected existing features or functionality. 

[![Testing pyramid © 2023 SketchingDev](/docs/img/testing-pyramid.jpg){width=50%}](https://sketchingdev.co.uk/sketchnotes/testing-pyramid.html)

#### **Unit tests**
A unit test is a type of test where individual units or components of the software application are tested in isolation from the rest of the application. A unit can be a function, method, or class. The main purpose of unit testing is to validate that each unit of the software performs as designed.

#### **Integration tests**
Integration testing is a level of software testing where individual units are combined and tested as a group. The purpose is to verify that the units work together as expected and that the interfaces between them function correctly. Integration tests aims to expose defects in the interactions between integrated components.

#### **End-to-end tests**
End-to-end testing is focused on checking the entire system from start to finish, simulating real use cases. The goal is to verify the software functions as a whole from the user's perspective.

#### **Regression tests**
Regression testing aims to verify that recent code changes haven't adversely affected existing features or functionality. It involves re-running previously executed test cases to ensure that the software still behaves as expected after modifications. The primary purpose of regression testing is to catch unintended side effects of code changes and ensure that new features or bug fixes haven't introduced regressions or broken existing functionality elsewhere in the code. Regression tests can include both unit tests and integration tests, as well as higher-level tests.

### Designing a test case 
For more complex integration, regression, or end-to-end tests, it can be useful to first describe the test case in words.

1. **Description:** _Description of test case_
1. **Preconditions:** _Conditions that need to be met before executing the test case_
1. **Test Steps:** _To execute test cases, you need to perform some actions. Mention all the test steps in detail and the order of execution_
1. **Test Data:** _If required, list data that needed to execute the test cases_
1. **Expected Result:** _The result we expect once the test cases are executed_
1. **Postcondition:** _Conditions that need to be achieved when the test case was successfully executed_