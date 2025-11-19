---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-22

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-10-28

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Automation for software development

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
  - Software
  - Automation
  - GitHub
  - GitLab
  - CI/CD

---

Continuous Integration (CI) refers to the build and unit testing stages of the software release process. Every committed revision can trigger an automated build and test. With Continuous Delivery (CD), code changes are automatically built, tested, and prepared for a release to production.

![Source: Solidstudio (solidstudio.io). [Asset path](https://cdn.sanity.io/images/lofvu8al/production/e37ce13c88889f048aa2b1acae7d6cbfeea5678f-2048x876.png).](https://solidstudio.io/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Flofvu8al%2Fproduction%2Fe37ce13c88889f048aa2b1acae7d6cbfeea5678f-2048x876.png&w=640&q=75){width=60%}

You can implement Continuous Integration and Continuous Delivery (CI/CD) workflows for your research software using either GitHub Actions or GitLab pipelines. Choose the platform that fits your project needs based on factors such as privacy and security needs, collaboration requirements, and available features.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa brands square-github >}} GitHub Actions
GitHub Actions workflows and concepts.

::: {.learn-more}
[Learn more »](./github_ci_cd.md)
:::
:::

::: {.feature}
### {{< fa brands square-gitlab >}} GitLab pipelines
GitLab pipelines in TU Delft GitLab.

::: {.learn-more}
[Learn more »](./gitlab_ci_cd.md)
:::
:::

:::
:::