---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
#date: MM/DD/YYYY

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Software testing

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

>_“Before relying on a new experimental device, an experimental scientist always establishes its accuracy. A new detector is calibrated when the scientist observes its responses to known input signals. The results of this calibration are compared against the expected response.”_
>
> [From [Testing and Continuous Integration with Python](https://carpentries-incubator.github.io/python-testing/), created by K. Huff]

Simulations and analyses using software should be held to the same standards as experimental measurement devices!

For a solid introduction and motivation on writing tests, we recommend the [lesson on testing](https://coderefinery.github.io/testing/motivation/) from the Code Refinery.


## Approach

### What to test?
When writing tests, ask yourself the following questions:
- How would you manually check the correctness of the code? 
- Do you need to test a particular parameter space?
- What do you compare the result to?
- How much time would it take to run the module (and therefore the test)?

### Type of tests

* **Unit test**: testing of individual units of source code (scripts, functions, classes).
* **Integration test**: testing of a combination of individual units as a group.
* **Regression test**: re-running all tests to ensure that the previously developed and tested code still performes after a code change.