---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
#date: YYYY-MM-DD

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
#date-modified: YYYY-MM-DD

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: MATLAB documentation

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Maurits Kok
author_2: Elviss Dvinskis

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
  - Software
  - Documentation
  - MATLAB

---

## Code comments
MATLAB has published a set of [Coding Guidelines](https://github.com/mathworks/MATLAB-Coding-Guidelines/blob/main/MATLAB-Coding-Guidelines.md) in 2025, which includes a section on code comments. Code comments are an essential part of code documentation, as they help explain the purpose and functionality of the code to other developers (and your future self).

## Docstrings
Docstrings are structured comments, associated with segments (rather than lines) of code which can be used to generate user documentation for users of your project. If properly formated, docstrings can be automatically extracted and compiled into user-friendly formats such as HTML or PDF, and can be accessed through the `help` function in MATLAB. 

Unfortunately, MATLAB does not offer a defined standard for docstring formatting, but the following structure is used by MATLAB for internal functions.

### Example docstring format
```matlab
function output = myFunction(input)
%myFunction - This function does something useful.
%   Detailed explanation goes here
% 
% Syntax
%   output = myFunction(input)
%
% Inputs Arguments
%   input - Description of input argument
%     data type
%
% Output Arguments
%   output - Description of output argument
%     data type
%
% Examples
%   Example usage of the function
```

The documentation can then be accessed in MATLAB through the `help` command:

```matlab
help myFunction
```

or viewed in a separate window with `doc`:

```matlab
doc myFunction
```

### Compatibility with Sphinx
If your software project uses Sphinx for documentation generation, you can use the [sphinxcontrib-matlabdomain](https://sphinxcontrib-matlabdomain.readthedocs.io/en/latest/) extension to parse MATLAB docstrings and include them in your Sphinx-generated documentation. For more information on how to set up and use this extension, refer to our [Tooling section](../tooling.md).
