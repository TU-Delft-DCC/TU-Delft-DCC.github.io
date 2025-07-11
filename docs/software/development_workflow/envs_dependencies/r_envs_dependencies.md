---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-14

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
title: Environment and dependency management in R

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
#categories: 
# - r
# - environments
# - dependencies
# - conda
# - renv


---

R users often rely on RStudio Projects and `renv` to manage their development environments. RStudio Projects organize your workspace by managing file paths and configurations, while `renv` tracks and restores package dependencies to ensure reproducibility. Together, they provide a structured and reliable workflow for managing R projects.

Although Conda can be used to create isolated R environments, it is less common in R workflows. Conda is most useful when managing multiple R versions, working in a Python + R setup, or handling system dependencies that are difficult to install through CRAN.

### Projects

RStudio Projects provide an organized workspace for your analyses and scripts, ensuring that file paths and working directories remain consistent across sessions. When you open an RStudio Project, it automatically sets the project’s root directory as your working directory and loads project-specific settings stored in the `.Rproj` file. Using RStudio Projects helps you to keep your code, data, and output bundled together, and avoid issues with file paths.

**Creating a new RStudio Project:**

- In RStudio, go to File → New Project.
- Choose whether to create a new directory, use an existing directory, or clone a project.
- Follow the prompts to configure your project settings.

### renv

The `renv` package manages R package dependencies within a project. It creates a reproducible snapshot of your package environment, ensuring that collaborators (or your future self) can recreate the exact setup. Some key `renv` commands:

**Initialize renv in your project:**
```r
# From your R console within the project directory:
renv::init()
```
This creates a dedicated library and a `renv.lock` file that tracks all installed packages. If a `renv.lock` file exists, `renv::init()` will automatically install the recorded dependencies. Otherwise, it sets up a new environment.

**Create a snapshot of your dependencies:**
```r
renv::snapshot()
```
This updates the `renv.lock` file to reflect the current package versions in your project.

**To restore an environment from a lockfile:**
```r
renv::restore()
```
This reinstalls packages according to the `renv.lock` file and reconstructs the environment.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Using RStudio Projects](https://support.posit.co/hc/en-us/articles/200526207-Using-RStudio-Projects)
- [renv for R](https://rstudio.github.io/renv/articles/renv.html)

:::