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

One of the most straightforward ways to reuse code across projects is by packaging it into an installable library that can be managed as a dependency. You can also use Git submodules or Git subtree to integrate external code into your project.

### Git submodules

Git submodules allow you to keep a Git repository as a subdirectory of another Git repository. It is a record that points to a specific commit in another external repository. Submodules are useful for incorporating external code or libraries into your project while keeping them separate and easily updatable.

##### **Adding submodules**

This will add a new submodule to your repository: ` git submodule add <repo-url>`

##### **Cloning a repository with submodules**

When you clone a repository that has submodules, you will have to initialize and fetch the submodules: `git submodule init` and then
`git submodule update`.

To update the submodules to the latest commit use: `git submodule update --remote`. 

You can also point to a specific commit within a submodule by navigating to the submodule's directory and using: `git checkout <specific-commit>`, and then committing the change to the main repository.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip

You can use the shorthand command that automatically clones, initializes, and updates all the submodules: `git clone --recurse-submodules <repo-url>`

:::

##### **Check the status of your submodules**

To check the status of your submodules, run: `git submodule status`

There should also be a file called `.gitmodules`, it's important to also version control that similarly to `.gitignore`. Then, commit and push your changes, as you would typically.

::: {.callout-warning collapse="true"}
## If you are using GitHub Desktop
If you are using GitHub Desktop, be aware that there might be some limitations when working with submodules. While GitHub Desktop supports basic submodule functionality, some operations may require using the command line. Known issues include difficulties in initializing submodules, switching branches with submodules, and visualizing submodule changes. These limitations are acknowledged and tracked by the GitHub Desktop team. Although some issues have been addressed over time, there might still be case-by-case issues.

See this [discussion](https://github.com/desktop/desktop/issues/7523) as an example. For more details, refer to the official GitHub Desktop documentation or [issue tracker](https://github.com/desktop/desktop/issues).
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Simplified Git submodules tutorial](https://www.atlassian.com/git/tutorials/git-submodule)
- [Guide on Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) - comprehensive guide that covers everything from the basics to advanced workflows
:::

### Git subtree
[Git subtree](https://www.atlassian.com/git/tutorials/git-subtree) allows you to merge the history of one repository into another as a subdirectory. It essentially brings the contents of a repository into another as if it were part of the directory structure.

::: {.callout-warning}
## To be avoided

- Storing commonly-used folders in a separate folder on your system and adding the folder to the PATH. Other users/developers will not have access to these folders.
- Direct copy-and-pasting of code as you lose any upstream changes to the external repository.
:::