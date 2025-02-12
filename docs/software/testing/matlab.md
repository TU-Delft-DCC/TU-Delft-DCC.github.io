---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-10

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Testing with MATLAB

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

In this guide, we will discuss writing and running tests with MATLAB. See the [documentation from Matlab](https://nl.mathworks.com/help/matlab/matlab-unit-test-framework.html) for more information.

## Writing tests

Tests should be kept separate from the code base, usually in a folder `tests/`. The naming convention for writing a test for a particular MATLAB script is to prefix “test_” to the name of the script that is being tested. For example, a test for the file `draw_random_number.m` should be called `test_draw_random_number.m`. In general, Matlab will recognize any scripts that are prefixed or suffixed with the string “test” as tests.

You can find an example below with the matlab syntax for writing [Class-based unit tests](https://nl.mathworks.com/help/matlab/class-based-unit-tests.html):

:::{.callout-note collapse="true" title="Click to view"}
{{< include _matlab_testclass.md >}}
:::


## Executing tests
We will create a Matlab script called `run_testsuite.m` in the folder `tests/`. This function can run the tests present in the folder `tests/` and can create test reports.

:::{.callout-note collapse="true" title="Click to view"}
{{< include _matlab_runtests.md >}}
:::


Additionally, we can selectively run test by defining TestTags. In the example above, we added the tag 'Unit'. You can then call the function in the MATLAB command window to run all tests with the tag 'Unit' with

```matlab
result = run_testsuite('TestTag', 'Unit')
```

:::{.callout-tip}
If you want to quickly check whether your tests pass without having to start up Matlab, you can also call `run_testsuite` from the terminal. In the folder containing the function, execute

```bash
matlab -batch "run_testsuite('TestTag', 'Unit')"
```

:::


## Testing in MATLAB

MATLAB supports **script-based**, **function-based**, and **class-based** unit tests, allowing for a range of testing strategies from simple to advanced use cases. See the MATLAB documentation for more information:

- [Matlab - Ways to write unit tests](https://nl.mathworks.com/help/matlab/matlab_prog/ways-to-write-unit-tests.html)
    - [Script-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/write-script-based-unit-tests.html)
    - [Function-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/write-function-based-unit-tests.html)
    - [Class-based testing](https://nl.mathworks.com/help/matlab/matlab_prog/author-class-based-unit-tests-in-matlab.html)

Because of the limiting features of the script- and function-based testing, this guide will discuss **class-based testing**. Class-based tests give you  access to shared test fixtures, test parameterization, and grouping tests into categories.


### Writing tests in MATLAB

::: {.callout-tip}
🎥 Check out this short [**MATLAB video**](https://nl.mathworks.com/support/search.html/videos/matlab-unit-testing-framework-74975.html?fq%5B%5D=asset_type_name:video&fq%5B%5D=category:matlab/matlab-unit-test-framework&page=1) on writing class-based tests.
:::

The naming convention for writing a test for a particular MATLAB script is to prefix “test_” to the name of the script that is being tested. For example, a test for the file `draw_random_number.m` should be called `test_draw_random_number.m`. In general, MATLAB will recognize any scripts that are prefixed or suffixed with the string `test` as tests.

💡 Check out the MATLAB documentation: [Write Simple Test Case Using Classes](https://nl.mathworks.com/help/matlab/matlab_prog/write-simple-test-case-using-classes.html)

::: {.callout-note collapse="true"}
## Matlab template for class-based unit tests
Additionally, here is a template with an explanation for writing of a class-based unit test in MATLAB for the file `sumNumbers.m`:

{{< include _matlab_testclass.md >}}
:::

### Executing tests in MATLAB

MATLAB offers four ways to run tests.

#### 1. Script editor
When you open a function-based test file in the MATLAB® Editor or Live Editor, or when you open a class-based test file in the Editor, you can interactively run all tests in the file or run the test at your cursor location.

![Script editor testing](https://nl.mathworks.com/help/matlab/matlab_prog/runtests_options.png)

👉 [Script Editor documentation](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-in-editor.html)


#### 2. `runtests()` in Command Window
You can run tests through the MATLAB Command Window, by executing the following command in the root of your repository:

```matlab
results = runtests(pwd, "IncludeSubfolders", true);
```

MATLAB will automatically find all tests. If you make use of tags to categorize tests, you can run specific tags with:
```matlab
results = runtests(pwd, "IncludeSubfolders", true, "Tag", '<tag-name>');
```

👉 [`runtests()` documentation](https://nl.mathworks.com/help/matlab/ref/runtests.html#d126e1481769)

#### 3. MATLAB Test Browser App
The Test Browser app enables you to run script-based, function-based, and class-based tests interactively. The app is available since R2023a.

![MATLAB test browser](https://nl.mathworks.com/help/matlab/matlab_prog/test_run_results.png)

👉 [MATLAB Test browser documentation](https://nl.mathworks.com/help/matlab/matlab_prog/run-tests-using-test-browser.html)

#### 4. MATLAB Test
MATLAB Test provides tools for developing, executing, measuring, and managing dynamic tests of MATLAB code, including deployed applications and user-authored toolboxes. 

👉 [MATLAB Test Addon documentation](https://nl.mathworks.com/products/matlab-test.html)

### MATLAB Simulink
    
In addition to script, function, and class-based unit tests, MATLAB offers [Simulink Test](https://nl.mathworks.com/products/simulink-test.html) for comprehensive simulation-based testing for Simulink.

- Simulink Test - [Introduction video](https://nl.mathworks.com/videos/simulink-test-overview-99891.html)
- Simulink Test - [Examples](https://nl.mathworks.com/help/sltest/examples.html)