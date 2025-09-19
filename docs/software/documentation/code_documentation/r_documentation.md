---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-26

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: R documentation

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Elviss Dvinskis
#author_2:

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
  - R
  - roxygen2
  - Vignettes

---

## roxygen2

The standard approach for documenting R projects is using `roxygen2`, a package that enables inline documentation for R scripts and packages. It is tightly integrated with the R ecosystem, making it straightforward to generate user-friendly documentation in the form of help files (`.Rd` files). `roxygen2` allows you to write documentation alongside your code as specially formatted comments, which are then parsed and converted into the appropriate documentation format as `.Rd` files.


Key features of `roxygen2`:

- **Inline documentation:** Document functions, arguments, and return values directly in the script.
- **Integration with R's help option:** Generates `.Rd` files, which are then converted into the help pages users can access with `?function_name`.
- **Cross-referencing:** You can easily link to other functions within the documentation.
- **Namespace management:** Automatically manages the `NAMESPACE` file for proper imports and exports. A `NAMESPACE` file is typical for CRAN submissions.

### Getting started with `roxygen2`

1. Install with `install.packages("roxygen2")`.
2. Ensure you are in the correct project directory and it has the standard R package structure.
3. **Writing documentation:**
    Documentation is written as comments starting with `#'` directly above your function definitions. `roxygen2` processes this and stores `.Rd` files in the `man/` directory.
    <br>Common tags include:
    - `@param`: Describes function arguments.
    - `@return`: Describes the return value.
    - `@examples`: Provides example usage.
    - `@import`: For importing functions from other packages.
    - `@inheritParams`: To inherit parameter descriptions from another documented function.
    - `@export`: Makes the function available to package users.
    - `@seealso` : For cross-referencing.
4. **Generating documentation:**
    Run `roxygenise()` to convert your documentation into `.Rd` files. You can also use `devtools::document()`since it is a wrapper around `roxygenise()`.
5. When packaging your R project, you can use `devtools::check()` to ensure your documentation is consistent with your function definitions.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} roxygen2 example
```r
#' Summarize a numeric vector
#'
#' This function calculates the mean, median, and standard deviation of a given 
#' numeric vector and returns the results in a data frame.
#'
#' @param x A numeric vector.
#' @return A data frame with the following columns:
#' \describe{
#'   \item{mean}{The mean of the numeric vector.}
#'   \item{median}{The median of the numeric vector.}
#'   \item{sd}{The standard deviation of the numeric vector.}
#' }
#' @details This function provides a quick summary for a numeric vector, returning 
#' measures of central tendency (mean and median) and a measure of 
#' dispersion (standard deviation) using R’s base functions mean(), median(), and sd().
#' @examples
#' # Basic example
#' summarize_vector(c(1, 2, 3, 4, 5))
#' 
#' @export
summarize_vector <- function(x) {
  if (!is.numeric(x)) stop("Input must be a numeric vector.")
  
  mean_val <- mean(x)
  median_val <- median(x)
  sd_val <- sd(x)
  
  return(data.frame(mean = mean_val, median = median_val, sd = sd_val))
}
```
:::

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} **Example repositories using roxygen2:** 
- [`ggplot2` on GitHub](https://github.com/tidyverse/ggplot2/)
- [`dplyr` on GitHub](https://github.com/tidyverse/dplyr/)
:::

## Vignettes

Vignettes are detailed guides or tutorials included with R packages, providing users with in-depth explanations and examples, complementing the shorter help files. They are useful for demonstrating package functionality and use cases. Vignettes are automatically compiled and included in the package documentation.

You can create a vignette by running:
```r
usethis::use_vignette("your_vignette_name")
```
This creates a template in the `vignettes/` directory with the necessary YAML header and structure. You can combine text, code chunks, and outputs using standard R Markdown syntax. Include explanations, usage examples, and visualizations to enhance clarity.

Once written, build the vignette using:

 ```r
 devtools::build_vignettes()
```
This generates HTML or PDF versions of the vignette, which are then included in the package documentation. Use `devtools::install(build_vignettes = TRUE)` to test your package and built vignettes together (see how a user would experience them).

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn More

- Explore `vignette("roxygen2")` in R
- [`roxygen2` documentation](https://roxygen2.r-lib.org/)
- [Function documentation from *R Packages*](https://r-pkgs.org/man.html)
- [Writing vignettes](https://r-pkgs.org/vignettes.html)
- [CRAN Submission guidelines](https://cran.r-project.org/web/packages/policies.html)
:::