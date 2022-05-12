# Software testing

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


## Table of contents
```{tableofcontents}
```