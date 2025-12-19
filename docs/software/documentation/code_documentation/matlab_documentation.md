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


## Docstrings
Docstrings are structured comments, associated with segments (rather than lines) of code which can be used to generate user documentation for users of your project. If properly formated, docstrings can be automatically extracted and compiled into user-friendly formats such as HTML or PDF, and can be accessed through the `help` function in MATLAB. Unfortunately, MATLAB does not offer a defined standard for docstring formatting, but the following examaple is used by MATLAB for internal functions.

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

Users can then access the documentation in MATLAB using the `help` command:

```matlab
help myFunction
```

or view the documentation in a separate window with `doc`:

```matlab
doc myFunction
```

```matlab
function [a, b, c] = triangleAngles(x, y, z, varargin)
    % TRIANGLEANGLES Compute angle of a triangle
    %
    % Args:
    %   x (double): triangle side 1
    %   y (double): triangle side 2
    %   z (double): triangle side 3
    %   degrees (logical): return angle in degrees. 
    %       The default is true.
    %
    % Returns:
    %   a (double): angle between side 1 and side 2
    %   b (double): angle between side 2 and side 3
    %   c (double): angle between side 1 and side 3
    %
    % Examples:
    %   [a, b, c] = triangleAngles(1, 1, sqrt(2))
    %   outputs a=90, b=45, c=45
    %
    %   [a, b, c] = triangleAngles(3, 4, 5)
    %   outputs a=90, b=60, c=30
end
```

- Indendation optional, but aids readability
- Difference between single and double quotes

## Extracting documentation
- MATLAB internal
- Sphinx