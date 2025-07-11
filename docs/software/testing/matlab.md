---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-10

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
title: Testing in MATLAB

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Writing and running tests with MATLAB
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
#corresponding:

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
    - testing
    - MATLAB

---

This guide explains how to write and execute tests in MATLAB. For additional details, refer to the [official MATLAB documentation](https://nl.mathworks.com/help/matlab/matlab-unit-test-framework.html).

## Writing tests
MATLAB supports **script-based**, **function-based**, and **class-based** unit tests, allowing for a range of testing strategies from simple to advanced use cases. See the MATLAB documentation for more information:

- [Matlab - Ways to write unit tests](https://nl.mathworks.com/help/matlab/matlab_prog/ways-to-write-unit-tests.html)
    - [Script-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/write-script-based-unit-tests.html)
    - [Function-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/write-function-based-unit-tests.html)
    - [Class-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/author-class-based-unit-tests-in-matlab.html)


#### Convention for writing tests
- It is recommened place tests in a separate folder, typically named `tests/`. 
- Prefix test files with “test” followed by the file that is tested. For example, a test for the file `DrawRandomNumber.m` should be called `TestDrawRandomNumber.m`. Matlab will recognize any scripts that are prefixed or suffixed with the string “test” as tests.

### Class-based unit tests

Because of the limited features of the script- and function-based testing, this guide will discuss **class-based testing**. Class-based tests give you access to shared test fixtures, test parameterization, and grouping tests into categories. Check out our [additional testing concepts](/docs/software/testing/intermediate.md) for more information about these concepts.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa video >}} Introduction to class-based testing
Check out this short [**MATLAB video**](https://nl.mathworks.com/support/search.html/videos/matlab-unit-testing-framework-74975.html?fq%5B%5D=asset_type_name:video&fq%5B%5D=category:matlab/matlab-unit-test-framework&page=1) on writing class-based tests.
:::

You can find an example below with the matlab syntax for writing Class-based unit tests:

```matlab
classdef TestSumNumbers < matlab.unittest.TestCase
    methods (Test)
        function testSumNumbers(testCase)
            result = sumNumbers(2, 3);            
            testCase.verifyEqual(result, 5)
        end
    end
end
```
{{< fa lightbulb >}} Check out the MATLAB documentation for an introductory example: [Write Simple Test Case Using Classes](https://nl.mathworks.com/help/matlab/matlab_prog/write-simple-test-case-using-classes.html)

:::{.callout-note collapse="true" title="Annotated class-based unit test example"}
{{< include _matlab_testclass.md >}}
:::


## Executing tests

### 1. Running tests in the MATLAB Command Window

You can run tests through the MATLAB Command Window, by executing the following command in the root of your repository:

```matlab
results = runtests(pwd, "IncludeSubfolders", true);

% The argument `pwd` specifies the current working directory
% `IncludeSubfolders` specifies whether to include subfolders in the search for tests
```

MATLAB will automatically find all tests. If you make use of tags to categorize tests, you can run specific tags with:
```matlab
results = runtests(pwd, "IncludeSubfolders", true, "Tag", '<tag-name>');
```

{{< fa hand-point-right >}} For more details: [`runtests()` documentation](https://nl.mathworks.com/help/matlab/ref/runtests.html#d126e1481769)

#### Custom testsuite script

We have a [custom script](./_matlab_runtests.md) available to run tests in a more structured way. It can be useful to:

- run tests with specific tags 
- ignore specific tests
- generate various test reports

When placed in the folder `tests/`, the script can be executed by running the following command in the MATLAB Command Window:

```matlab
run_testsuite('TestTag', 'Unit')
```

### 2. Script editor
You can run tests interactively by opening a test file in the MATLAB Editor and selecting "Run All" or "Run Current Test".

![MathWorks, Script editor testing, MATLAB Documentation, [link to image.](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-in-editor.html)](https://nl.mathworks.com/help/matlab/matlab_prog/runtests_options.png)

{{< fa hand-point-right >}} For more details: [Script Editor documentation](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-in-editor.html)


### 3. MATLAB Test Browser App
The Test Browser app (available since R2023a) enables you to run script-based, function-based, and class-based tests interactively. You can run all tests, selected tests, or individual tests.

![MathWorks, MATLAB test browser, MATLAB Documentation, [link to image.](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-using-test-browser.html)](https://nl.mathworks.com/help/matlab/matlab_prog/test_run_results.png)

{{< fa hand-point-right >}} For more details: [MATLAB Test browser documentation](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-using-test-browser.html)

### Simulink testing
For Simulink models, MATLAB provides [Simulink Test](https://nl.mathworks.com/products/simulink-test.html) for simulation-based testing.

- [Simulink Test - Introduction video](https://nl.mathworks.com/videos/simulink-test-overview-99891.html)
- [Simulink Test - Examples](https://nl.mathworks.com/help/sltest/examples.html)