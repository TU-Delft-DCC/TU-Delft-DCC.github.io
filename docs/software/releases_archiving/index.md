---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-03-20

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
title: Packaging, releases and archiving

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
author_2: Maurits Kok

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
- package
- release
- archive
# - 

---

Eventually your software will be at a sharable and publishable point. One way to distribute your software is to package it and release it on a platform like PyPI (Python Package Index), or CRAN (Comprehensive R Archive Network). Additionally, you want to archive your software for long-term preservation in repositories like Zenodo or 4TU.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa box-open >}} Packaging
Package your software.

::: {.learn-more}
[Learn more »](./packaging/packaging.md)
:::
:::

::: {.feature}
### {{< fa box >}} Releases
Publish your software.

::: {.learn-more}
[Learn more »](./releases/releases.md)
:::
:::

::: {.feature}
### {{< fa box-archive >}} Archiving
Archive your software.

::: {.learn-more}
[Learn more »](./archiving.md)
:::
:::

:::
:::