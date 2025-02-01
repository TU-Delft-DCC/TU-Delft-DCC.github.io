
### Code duplication {.unnumbered}
Duplicated code refers to instances where similar or identical blocks of code appear in multiple places within a codebase. This code smell can increase maintenance efforts, as changes in one place might require corresponding changes in other places.

:::{.callout-note appearance="simple"}
## Solution 
- Refactor the code to accept parameters as arguments, instead of hard-coding them.
- Extract common functionality into functions or methods.
- Refactor duplicated code into higher-level abstractions.
- Make use of utility functions to centralize common code and avoid duplication.
:::