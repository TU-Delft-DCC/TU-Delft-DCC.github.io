---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-24

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
title: Development workflow

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
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
- version control
- project organization
- collaboration 

---

### Version control and collaboration
Version control ensures transparency, reproducibility, and smooth teamwork. Clear branching strategies and consistent workflows make it easier to track changes, review code, and integrate contributions.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa code-commit >}} Project Management
Managing your projects through version control platforms.

::: {.learn-more}
[Learn more »](./project_management.md)
:::
:::

::: {.feature}
### {{< fa code-branch >}} Branch Management
Choosing a branching strategy.

::: {.learn-more}
[Learn more »](./branch_management.qmd)
:::
:::

::: {.feature}
### {{< fa code-fork >}} Collaboration
Collaborative workflow.

::: {.learn-more}
[Learn more »](./collaboration.qmd)
:::
:::

:::
:::

### Project organization
A structured repository with defined folders, managed dependencies, and reusable components keeps you rproject consistent, scalable, and easier for others to understand and extend.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa folder-tree >}} Project Structure
Structuring your project.

::: {.learn-more}
[Learn more »](./project_structure.md)
:::
:::

::: {.feature}
### {{< fa copy >}} Project Templates and Reusability
Reusing projects and repositories.

::: {.learn-more}
[Learn more »](./reusing_projects.md)
:::
:::

::: {.feature}
### {{< fa cubes >}} Environments and Dependencies
Managing your environments and dependencies.

::: {.learn-more}
[Learn more »](./envs_dependencies.md)
:::
:::

::: {.feature}
### {{< fa diagram-successor >}} Workflow Management 
Tools for writing and managing workflows.

::: {.learn-more}
[Learn more »](./workflow_management.md)
:::
:::


:::
:::