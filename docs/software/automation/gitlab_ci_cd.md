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
title: GitLab pipelines

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
  - GitLab
  - CI/CD

---

As previously mentioned in the [Project management](../development_workflow/project_management.md#version-control-platforms) section, TU Delft has its own GitLab instance. However, it does not (yet) have preconfigured servers available to run [**GitLab pipelines**](https://docs.gitlab.com/ee/ci/pipelines/), the equivalent of GitHub Actions. 

In order to set up a pipeline, you will need to request a TU Delft Virtual Private Server and configure a GitLab runner there. The DCC has developed a step-by-step guide (see below), along with guidance on setting up a CI pipeline for a MATLAB environment.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa brands square-gitlab >}} Continuous Integration with GitLab
Set up CI/CD for your project in TU Delft GitLab.

::: {.learn-more}
[Learn more »](./gitlab/gitlab_docker.md)
:::
:::

::: {.feature}
### {{< fa brands square-gitlab >}} Setting up a GitLab runner for MATLAB
Create a CI pipeline for a MATLAB environment in TU Delft GitLab.

::: {.learn-more}
[Learn more »](./gitlab/runner_matlab.md)
:::
:::

:::
:::