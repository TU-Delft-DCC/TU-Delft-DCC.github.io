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
title: Releases

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
author_2: Elviss Dvinskis

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
 - release
 - r
 - python

---

Once you have your software packaged, you can release it to the public. This process typically involves uploading your package to a repository or platform where users can easily access and install it. The most common platforms for releasing software packages are PyPI for Python packages and CRAN for R packages.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa box >}} Release your Python package
Publish your Python package on PyPI.

::: {.learn-more}
[Learn more »](./releases_pypi.md)
:::
:::

::: {.feature}
### {{< fa box >}} Release your R package
Publish your R package on CRAN.

::: {.learn-more}
[Learn more »](./releases_cran.md)
:::
:::

:::
:::