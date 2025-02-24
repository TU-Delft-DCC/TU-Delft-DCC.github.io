---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-14

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Project organisation

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

In software development, the choiches you make at the start will affect your project's final outcome. One key decision is how to structure your project, as a well-organised setup is essential for reproducibility and long-term maintainability.

### Essential principles
- **Consitant directory structure**: Have a consistent and meaningful directory naming convention.
- **Clear file and folder naming**: Opt for lowercase names combined with underscores or hyphens.
- **Managing access levels**: Use different Git repositories for public and private parts of your project. Use `.gitignore` or a specific non-tracked folder for sensitive content and/or files that are too large.
- **Clear documentation**: Include a `README` at the project's root to offer a summary, and add an appropriate `LICENSE` to define the terms for reuse and modification.
- **Coding standards**: Adhere to a consistent coding style to enhance code readability.

### Other recommendations
- **Code reusability**: Store reusable software elements in a separate repository for efficiency across projects or consider packaging them.
- **Modular code design**: Aim for modular code design to improve maintainability and reusability.
- **Dependency management**: Use virtual environments to manage project dependencies, ensuring consistent environments across different setups.

## Repository structures

A well-organized repository structure would be similar to this:

::: {.panel-tabset}

### Python

```bash
your_project/
│
├── docs/                     # Documentation directory
├── notebooks/                # Jupyter notebooks
├── src/                      # Contains your main code
│   └── your_project/            # A folder where your organized code lives
│       ├── __init__.py       # A marker file that indicates this folder is for Python code
│       ├── module            # A file or folder with specific functions or classes
│       └── extras/           # A folder for additional, related code
│           └── __init__.py   # A marker file for the additional code folder
├── tests/                    # Your test directory  
│
├── data/                     # Data files used in the project (if applicable)
├── processed_data/           # Files from your analysis (if applicable)
├── results/                  # Results (if applicable)
│
├── .gitignore                # Untracked files 
├── requirements.txt          # Software dependencies (environment.yml if using Conda)
│							  #	↑ Even better to use a build system config (pyproject.toml)
│							  #	↑ which is becoming the new standard
├── README.md                 # README
└── LICENSE                   # License information
```

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Choosing layout
- [Choosing between a `src/` layout and a flat layout for Python](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
:::

### MATLAB

```bash
your_project/
│
├── docs/                   # Documentation and user guides
├── src/                    # Main MATLAB code
│   ├── utils/              # Helper functions and scripts
│   ├── models/             # Core functions or classes implementing models/algorithms
│   └── main_script.m       # Main script/-s or entry point for the project
│
├── scripts/                # Scripts folder (e.g. for analysis and demo scripts)
├── tests/                  # Tests folder (e.g. MATLAB unit tests)
├── data/                   # Raw data files
├── results/                # Output files (figures, processed data, etc.)
├── examples/               # Example usage or tutorials
│
├── .gitignore              # Specifies files/folders to ignore in version control
├── README.md               # Project overview and instructions
└── LICENSE                 # License information

```

### R

```bash
your_project/
│
├── R/                        # R scripts and functions (can also be called src/)
│   ├── function.R            # R functions used across analyses
│   └── other_function.R      
│
├── data/                     # raw data files (if applicable)
├── processed_data/           # processed data files (if applicable)
│
├── doc/                      # project documentation
├── man/                      # manual files for package functions generated from roxygen2 (if applicable)
│      
├── vignettes/                # explanatory vignettes for the project (if applicable)
│   └── function_vignette.Rmd # vignettes for each function
│
├── tests/                    # test cases for your functions (highly recommended)
│   └── testthat/             # using the testthat package
│
├── results/                  # output from data analyses etc. (if applicable)
│
├── scripts/                  # high-level scripts for running analyses
│   └── analysis_script.R     # script running the main analysis
│
├── .gitignore                # gitignore
├── DESCRIPTION               # package description file (if applicable)
├── NAMESPACE                 # namespace file for package (if applicable)
├── README.md                 # README
└── LICENSE                   # license information
```

:::

This structure is a guideline and should be adapted based on the specific needs and practices of your project. Additionally:

- Particular metadata files are often capitalized, such as README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG, CITATION.cff, NOTICE, and MANIFEST.
- Generally, all content that is generated upon building or running your code should be added to `.gitignore`. This likely includes the content of `processed_data` and `results` folder. 
- Git cannot track empty folders. If you want to add empty folders to enforce a folder structure, e.g., `processed_data` or`results`, add the file `.gitkeep` to the folder.

:::{.callout-warning appearance="simple" icon="false"}
## {{< fa warning >}} **Warning**
- If your raw data files or any data assets are large (typically more than a few megabytes), it’s usually best not to include them directly in the repository. Instead:
    - Keep such files externally (e.g. cloud storage, Git LFS), and add only a reference or a small sample to the repository.
    - Adding placeholder files or instructions in the README for how to obtain the complete datasets.
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Code Refinery - Organizing your projects](https://coderefinery.github.io/reproducible-research/organizing-projects/)
- [ArjanCodes guide to structuring Python projects](https://arjancodes.com/blog/guide-to-structuring-python-projects/)
- [A collection of `.gitignore` templates](https://github.com/github/gitignore)
- [Git LFS](https://git-lfs.com)
:::

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

