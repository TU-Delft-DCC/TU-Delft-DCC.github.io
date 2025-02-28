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
title: Environment and dependency management in Python

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
# - python
# - environments
# - dependencies
# - conda
# - venv
# - virtualenv

---

When working with Python, managing dependencies and environments is important to ensure your project can be reproduced and shared. 

::: {.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Definitions:
A **dependency** is any external library your project needs, and a **virtual environment** is an isolated workspace where dependencies are installed.
:::

There are several ways to manage dependencies and environments:
- Conda environments (scientific computing and package management)
- Virtual environments (`venv`/`virtualenv`) (lightweight, built into Python)
- Alternative dependency management tools


### Conda Environments

Conda is a package and environment manager popular the research and data science community. It allows you to manage both Python and non-Python dependencies.

#### Basic commands
```bash

# Create a new environment, e.g. with python 3.12
conda create -n your_env_name python=3.12

# List all environments
conda env list

# Activate an environment
conda activate your_env_name

# Install packages in an environment
conda install package_name

# Export an environment to a file
conda env export > environment.yml

# Deactivate an environment
conda deactivate

# Remove a package from an environment
conda env remove -n your_env_name
```	

#### Conda environment files
Conda environment files (`environment.yml`) are used to specify the dependencies of a project. They can be used to create an environment from scratch, or to update an existing environment.

```bash
# Export an environment to a file
conda env export > environment.yml

# Create an environment from a file
conda env create -f environment.yml

# Update an environment from a file
conda env update -f environment.yml
```

### Virtual Environments (`venv`/`virtualenv`)
Python provides `venv` as a buil-in tool for creating virtual environments. `virtualenv` is a third-party tool that provides similar functionality.

#### Creating a virtual environment

```bash
# Using venv (Python 3.3+ built-in)
python -m venv your-env-name

# Using virtualenv (must be installed first)
pip install virtualenv
virtualenv your-env-name
```

#### Activating the environment

```bash
# Linux/macOS
source your-env-name/bin/activate

# Windows
your-env-name\Scripts\activate

# To deactivate
deactivate

```

#### Managing dependencies with pip

```bash
# Export requirements.txt from an activated environment
pip freeze > requirements.txt

# Install dependencies from requirements.txt
pip install -r requirements.txt

```

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Use [`pip-chill`](https://pypi.org/project/pip-chill/) or [`pipreqs`](https://pypi.org/project/pipreqs/) instead of `pip freeze` to exclude unnecessary dependencies. `pip-chill` lists only packages you installed, while `pipreqs` lists packages your code actually uses.
:::


### Dependency Management Tools

For more control over dependencies, consider using alternative tool that can provide a more sophisticated dependency management by handling virtual environment creation and dependency resolution in together. They maintain a project manifest (e.g., `pyproject.toml` for Poetry) that specifies primary dependencies and generate lock files to pin exact versions for reproducibility.

- [Pipenv](https://pipenv.pypa.io/en/latest/): Combines `pip` and `virtualenv` into a single tool, with a focus on simplicity and ease of use.
- [Poetry](https://python-poetry.org/docs/): Manages dependencies, environments, and package building in a streamlined way.
- [Pixi](https://pixi.sh/latest/tutorials/python/): A new tool that aims to provide a more user-friendly experience for managing Python environments and dependencies.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [CodeRefinery - Recording dependencies](https://coderefinery.github.io/reproducible-research/dependencies/)
- [The Turing Way - Package Management Systems](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package)
- [Conda documentation](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
- [virtualenv documentation](https://virtualenv.pypa.io/en/latest/)
- [virtualenvwrapper extension](https://virtualenvwrapper.readthedocs.io/en/latest/)
:::
