---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-19

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Documentation

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

---

Documentation serves as a bridge between the developer and user, and effectively communicating and explaining the code is as important as the code itself. Often, two types of documentation are distinguished - user and developer documentation. Both are essential for the success of a software project, and they serve different purposes.

### User documentation
User documentation is aimed at those who will use the software. This documentation typically includes user manuals and tutorials, possibly FAQs and troubleshooting guides. The focus is on simplicity and accessibility, ensuring that anyone can understand how to use the software.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa book-open-reader >}} README
How to write a good README.

::: {.learn-more}
[Learn more »](./write_a_readme.md)
:::
:::

::: {.feature}
### {{< fa scale-balanced >}} Licenses
Apply an open-source license.

::: {.learn-more}
[Learn more »](./license.md)
:::
:::

::: {.feature}
### {{< fa quote-left >}} CITATION
Cite your software.

::: {.learn-more}
[Learn more »](./citation.md)
:::
:::

:::
:::


### Developer documentation
Developer documentation targets developers who need to understand the internal parts of the software for purposes of development, maintenance, or integration. It can include additional details such as API documentation and development guidelines. Developer documentation is more detailed providing insights necessary for modifying and enhancing the software.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa laptop-code >}} Code Documentation
Documenting your codebase.

::: {.learn-more}
[Learn more »](./code_documentation/code_documentation.md)
:::
:::

::: {.feature}
### {{< fa screwdriver-wrench >}} Tooling
Deploy your documentation.

::: {.learn-more}
[Learn more »](./tooling.md)
:::
:::

::: {.feature}
### {{< fa globe >}} Hosting
Host your documentation.

::: {.learn-more}
[Learn more »](./hosting.md)
:::
:::

::: {.feature}
### {{< fa code-merge >}} Contributing Guidelines
Define how to contribute to your project.

::: {.learn-more}
[Learn more »](./contributing_guidelines.md)
:::
:::

::: {.feature}
### {{< fa handshake-angle >}} Code of Conduct
Set expectations for respectful, inclusive collaboration among contributors.

::: {.learn-more}
[Learn more »](./code_of_conduct.md)
:::
:::

:::
:::