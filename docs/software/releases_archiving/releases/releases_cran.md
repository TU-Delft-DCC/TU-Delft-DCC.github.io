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
title: Release your R package

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
 - r
 - cran
 - release

---

After building and testing your R package, you can release it to CRAN. This process involves several steps to ensure that your package is ready for distribution. Unlike PyPI for Python, CRAN has specific requirements and guidelines that must be followed.

## Preparing for a CRAN submission

Ensure that your package is well-documented, tested, and follows CRAN policies. This includes having a DESCRIPTION file with all necessary fields filled out, a NAMESPACE file, and proper documentation for all functions. We already mentioned the use of `devtools::check()` and `devtools::build()` in the [*R packaging guide*](../packaging/packaging_r.md). These functions will help you prepare your package for submission. The package should pass all tests and checks without errors or warnings. The tarball created by `devtools::build()` will be used for submission.

Additionally, you would want to run `devtools::check_rhub()` to check your package on different platforms and R versions. The difference between `devtools::check()` and `devtools::check_rhub()` is that the former checks your package on your local machine, while the latter checks it on a remote server with different configurations. 

This will help you identify any potential issues that may arise when users try to install your package on different systems. It can check your package on various platforms, including Windows, macOS, and different Linux distributions. It will also check for common issues that may arise when users try to install your package on different systems. While R-hub includes Windows builders, many developers specifically use `devtools::check_win_devel()` and `devtools::check_win_release()` before CRAN submission, as Windows compatibility issues are common.

Review the CRAN policies and guidelines to ensure your package complies with their requirements. You can find the policies [here](https://cran.r-project.org/web/packages/policies.html).

## Submitting to CRAN

Ensure that your package size is within the limits set by CRAN. You can check the size of your package using `file.info()` on the tarball created in the previous step. Then:

1. **Create a CRAN account**: If you don't already have one, create an account on the CRAN website.
2. **Submit your package**: Use `devtools::submit_cran()` to submit your package to CRAN. This function will prompt you to enter your CRAN username and password, and it will automatically upload your package tarball to CRAN.
3. **Fill out the submission form**: After submitting your package, you will be directed to a web form where you can provide additional information about your package, such as a description, title, and any other relevant details.
4. **Wait for CRAN review**: After submitting your package, it will be reviewed by CRAN. This is an important distinction from PyPI, where packages are typically available immediately after submission. The CRAN team will check your package for compliance with their policies and guidelines.
   - If your package passes the review, it will be published on CRAN.
   - If there are issues, they will contact you for additional information or to request changes to your package.
5. **Respond to feedback**: If the CRAN team requests changes or has questions about your package, make any necessary adjustments.
6. **Release your package**: Once your package has been approved, it will be available on CRAN for others to install and use.

### Additional resources

The R packages book also has a detailed section on the [CRAN submission process](https://r-pkgs.org/release.html), including how to handle feedback from CRAN maintainers and how to respond to requests for changes.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [R packages book - CRAN submission](https://r-pkgs.org/release.html)
- [CRAN policies](https://cran.r-project.org/web/packages/policies.html#Top)
- [CRAN submission process](https://cran.r-project.org/web/packages/policies.html#Submission-1)
:::