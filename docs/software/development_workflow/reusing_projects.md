---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-24

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Project templates and reusability

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
#categories: 
# - git subtree
# - git submodules
# - templates
# - repository structures

---

## Project templates

Templates can help you to standardize your software development process.

### GitHub repository templates
You can turn an existing repository into a template, so you and others can generate new repositories with the same directory structure, branches, and files. Note, the template repository cannot include files stored using Git LFS.

:::{.callout-tip appearance="simple" icon="false"}
## **{{< fa laptop-file >}} Repository templates**
- [Creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [Repository template example](https://github.com/manuGil/fair-code) to make your code more compliant with FAIR principles
:::

### Cookiecutter for Python

[Cookiecutter](https://www.cookiecutter.io/) creates Python projects from project templates. The advantage of using Cookiecutter is that new projects are set up quickly from a standardized template structure and can include everything needed to get started on a project, such as directory layouts, sample code, and even integrations with tools and services.


:::{.callout-tip appearance="simple" icon="false"}
## **{{< fa book >}} Tutorials**
- [Tutorial for Cookiecutter](https://cookiecutter-python.readthedocs.io/en/latest/tutorial.html)
- For installation instructions, have a look at [Cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/1.7.3/installation.html).
:::
:::{.callout-tip appearance="simple" icon="false"}
## **{{< fa laptop-file >}} Cookiecutter templates**
- [Cookiecutter templates on GitHub](https://github.com/search?q=cookiecutter&type=Repositories)
- Cookiecutter PyPackage: template for distributing Python libraries.
  - GitHub - [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
  - GitHub - [Netherlands eScience Center template](https://github.com/NLeSC/python-template)
- [**Cookiecutter Machine Learning:**](https://dagshub.com/DagsHub/Cookiecutter-MLOps) template for machine learning projects.
:::

## Reusing projects and repositories

One of the easiest ways to reuse code across projects is by packaging it into an installable library that can be used as a dependency. Alternatively, you can integrate external code into your project using **Git submodules** or **Git subtree**.

::: {.callout-warning}
## Practices to avoid
- Storing commonly-used folders in a separate folder on your system and adding the folder to the PATH. Other users/developers will not have access to these folders.
- Direct copy-and-pasting of code as you lose any upstream changes to the external repository.
:::

#### What’s the Difference?

| Feature        | Git Submodules | Git Subtree |
|-----------------|---------------|-------------|
| **How it works** | Adds an external repository inside your project as a separate Git reference. | Merges an external repository’s contents into your project’s directory structure. |
| **Version Control** | Tracks a specific commit of the external repository (not automatically updated). | The external repository’s commits are fully merged into your project's commit history. |
| **Updating** | Requires running `git submodule update --remote` to pull new changes. | Updates by merging changes from the external repository into your project. |
| **Ideal For** | Keeping external code separate while still using it in your project. | Fully integrating external code while keeping its history. |

: {tbl-colwidths="[20,40, 40]"}

In short:

- Use **Git submodules** when you want to include an external repository but keep it separate, track its exact version, and update it manually.
- Use **Git subtree** if you want to fully integrate an external repository’s code into your project while keeping its commit history.

### Git submodules

A Git submodule allows you to add a separate Git repository inside another repository as a subdirectory. It is a record that points to a specific commit in another external repository. Submodules are useful for incorporating external code or libraries into your project while keeping them separate and easily updatable.

::: {.callout-tip collapse="true"}
## Git submodule commands

##### Adding a submodule
To add an external repository as a submodule inside your project, use:
```bash
git submodule add <repo-url>
```

##### Cloning a repository with submodules
When cloning a repository that contains submodules, follow these steps:
1. Clone the repository:
```bash
git clone <repo-url>
```
2. Initialize the submodules:
```bash
git submodule init
```
3. Fetch the submodule content:
```bash
git submodule update
```

Alternatively, you can use the shorthand command to clone and initialize submodules:
```bash
git clone --recurse-submodules <repo-url>
```

##### Updating submodules
To update the submodules to the latest commit, use:
```bash
git submodule update --remote
```

:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Simplified Git submodules tutorial](https://www.atlassian.com/git/tutorials/git-submodule)
- [Guide on Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) - comprehensive guide that covers everything from the basics to advanced workflows
:::


::: {.callout-warning collapse="true"}
## If you are using GitHub Desktop
If you are using GitHub Desktop, be aware that there can be limitations when working with submodules. While GitHub Desktop supports basic submodule functionality, some operations may require using the command line. Known issues include 

- difficulties in initializing submodules
- switching branches with submodules
- visualizing submodule changes. 

For more details, check out [this discussion](https://github.com/desktop/desktop/issues/7523) or visit the [GitHub Desktop issue tracker](https://github.com/desktop/desktop/issues).
:::

### Git subtree
Unlike Git submodules, Git subtree merges the history of one repository into another as a subdirectory. This makes the external repository’s files appear as if they are part of your project while still allowing updates.

For more details, check out this [Git subtree guide](https://www.atlassian.com/git/tutorials/git-subtree).