---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-06

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Code style and tools

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of code style guides, static analysis tools, and formatters.
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
- code quality
# - 

---

> "Programs must be written for people to read, and only incidentally for machines to execute."
>
> **Harold Abelson**

## Style guide
Style guides are a set of rules and conventions that define how code should be written in a particular programming language. They cover aspects such as naming conventions, indentation, line length, and other formatting rules. Style guides help to ensure that code is consistent, readable, and maintainable, and they are often enforced by static analysis tools and formatters. Many programming languages have official style guides, and there are also community-driven style guides that provide additional recommendations and best practices.

## Static analysis tool
Static analysis tools are used to analyze source code without executing it. They can identify potential issues in the code, such as syntax errors, bugs, and [code smells](./code_smells.md). Static analysis tools can also enforce coding standards and best practices, and help to identify security vulnerabilities. They are often integrated into Continuous Integration workflows to ensure that code quality is maintained throughout the development process.

## Formatters
Formatters are tools that automatically adjust the formatting of your code to make it consistent and readable according to predefined style guidelines. They do not identify errors in the logic of the code but instead can restructure the whitespace, line breaks, and indentation so that the code is more uniform across a project. 

## Overview of programming languages

| Language  | Style Guide | Static Analysis Tools | Formatters |
|-----------|------------|----------------------|------------|
| **Python** | [PEP 8](https://peps.python.org/pep-0008/) | [`pylint`](https://pylint.pycqa.org/), [`flake8`](https://flake8.pycqa.org/), [`prospector`](https://prospector.landscape.io/en/master/) | [`black`](https://black.readthedocs.io/), [`autopep8`](https://github.com/hhatto/autopep8), [`yapf`](https://github.com/google/yapf) |
| **R** | [Tidyverse Style Guide](https://style.tidyverse.org/) | [`lintr`](https://lintr.r-lib.org/) | [`styler`](https://github.com/r-lib/styler) |
| **MATLAB** | [MATLAB Style Guidelines 2.0](https://nl.mathworks.com/matlabcentral/fileexchange/46056-matlab-style-guidelines-2-0) | [`checkcode`](https://www.mathworks.com/help/matlab/ref/checkcode.html) | [`Code Analyzer`](https://www.mathworks.com/help/matlab/ref/codeanalyzer-app.html) |
| **C/C++** | [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) | [`cppcheck`](http://cppcheck.sourceforge.net/), [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/) | [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html), [`astyle`](http://astyle.sourceforge.net/) |
| **Julia** | [Julia Style Guide](https://docs.julialang.org/en/v1/manual/style-guide/), [Blue Style Guide](https://github.com/invenia/BlueStyle) | [`JET.jl`](https://github.com/aviatesk/JET.jl), [`Aqua.jl`](https://github.com/JuliaTesting/Aqua.jl) | [`JuliaFormatter.jl`](https://github.com/domluna/JuliaFormatter.jl) |
| **Fortran** | [Fortran Best Practices](https://fortran-lang.org/en/learn/best_practices/) | [`fortran-linter`](https://github.com/fortran-lang/fpm/issues/174) | [`fprettify`](https://github.com/pseewald/fprettify) |


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [The Turing Way - Code Quality](https://the-turing-way.netlify.app/reproducible-research/code-quality)
- [The Turing Way - Code Style](https://the-turing-way.netlify.app/reproducible-research/code-quality/code-quality-style)
- [RealPython - Python Code Quality](https://realpython.com/python-code-quality/)
- [RealPython - PEP8](https://realpython.com/python-pep8/)
:::