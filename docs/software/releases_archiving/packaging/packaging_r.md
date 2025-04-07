---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-04

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Creating an R package

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - package
 - R

---

In this guide we will briefly touch the necessary steps to create an R package. For a more detailed guide, please refer to the excellent [R packages book](https://r-pkgs.org/) written by Hadley Wickham and Jennifer Bryan. The book is available online for free and is licensed under the [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license. The book covers everything from the basics of package creation to advanced topics. It provides clear explanations, practical examples, and helpful tips to guide you through the process of building high-quality R packages.

## Prerequisites

You will need the following packages installed to develop R packages:
```r
install.packages(c("devtools", "roxygen2", "testthat", "usethis"))
```

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Please refer to our [*R code documentation guide*](../../documentation/code_documentation/r_documentation.md) on how to document your R code. The guide covers the use of `roxygen2` for generating documentation, which is a key part of creating an R package.
:::

## Creating the package structure

To create an R package, we can use the `devtools` and `usethis` packages which include a variety of tools aimed at package development. The `devtools` package provides a set of functions that simplify the process of package development in R. The `usethis` package is another option for creating an R package structure. It provides a set of functions that help you create and manage R packages, including functions for creating package skeletons, adding dependencies, and managing package metadata. The two packages are often used together. For example, you can use `usethis` to create a package structure and then use `devtools` to add functions, tests, and documentation.

Either way, you can create a package structure using the following command:

```r
# Using devtools
devtools::create("your_package_name")
# Using usethis
usethis::create_package("your_package_name")
```

Alternatively, you can create a package structure using the RStudio IDE. This is a more user-friendly option for those who prefer a graphical interface. To create a package structure in RStudio, follow these steps:

1. Open RStudio and create a new project.
2. Select "New Directory" and then "R Package".
3. Choose a name for your package and select the location where you want to create it.
4. Click "Create Project" to generate the package structure.

Every option will create a basic folder structure with essential files including DESCRIPTION, NAMESPACE, and R/ directory. The DESCRIPTION file contains metadata about your package, such as its name, version, author, and dependencies. The NAMESPACE file defines the functions and objects that will be exported from your package. The R/ directory is where you will write your package functions.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Please visit our [*Project structure*](../../development_workflow/project_structure.md) guide for a recommendation on how to structure your R project.
:::


## Adding functions and documentation

Once you have the package structure for your R project, you will need to:

1. Edit the `DESCRIPTION` file and fill in the package metadata, including the package name, version, author, licensing information and dependencies.
2. All your package functions should be placed in the `R/` directory. You can create multiple R scripts in this directory to organize your functions logically.
3. Use `roxygen2` and `devtools::document()` to generate the documentation for your package based on the comments in your code. This will create `.Rd` files in the `man/` directory.
4. The `NAMESPACE` file should be generated automatically by `roxygen2` based on `@export` tags.
5. Use `devtools::build_vignettes()` to build the package vignettes. This will create HTML files in the `vignettes/` directory.

## Testing and building the package

Once you have added your functions and documentation, you can test and build your package using the following steps:

1. Use `devtools::test()` to run your package tests. This will run any tests you have written in the `tests/` directory.
2. To load and test your package, use `devtools::load_all()`. This will load your package into the R session, allowing you to test it interactively.
3. Use `devtools::check()` to check your package for any issues or errors. This will run a series of checks on your package and report any problems.
4. Use `devtools::build()` to create a tarball of your package. This will create a `.tar.gz` file in the parent directory of your package.
5. Use `devtools::install()` to install your package locally for testing. This will install the package from the tarball you just created.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [R packages book](https://r-pkgs.org/)
- [`usethis` package](https://usethis.r-lib.org/index.html)
- [`devtools` package](https://devtools.r-lib.org/index.html)

:::


## Next steps

The next step would be to publish your package. Visit our [*Release your R package*](../releases/releases_cran.md) guide for information on how to publish your package to CRAN.