---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-14

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

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
author_3: Aysun Urhan

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
  - Environments
  - Dependencies
  - Python
  - conda
  - venv
  - virtualenv
  - pyproject.toml
  - uv

---
When working with Python, managing dependencies and environments is important to ensure your project can be reproduced and shared. 

::: {.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Definitions:
A **dependency** is any external library your project needs, and a **virtual environment** is an isolated workspace where dependencies are installed.
:::

There are several ways to manage dependencies and environments:

- [Conda environments](#conda-environments)
- [Virtual environments](#virtual-environments-venvvirtualenv) (`venv`/`virtualenv`)
- [Dependency management tools](#dependency-management-tools) (e.g. `poetry`, `pipenv`)


### Conda Environments

Conda is a package and environment manager popular in the research and data science community. It allows you to manage both Python and non-Python dependencies.

#### **Basic commands**
```bash
# Create a new environment, e.g. with python 3.12
conda create -n your_env_name python=3.12

# List all environments
conda env list

# Activate an environment
conda activate your_env_name

# Install packages in an environment
conda install package_name

# Remove a package
conda remove package_name

# Export an environment to a file
conda env export > environment.yml

# Deactivate an environment
conda deactivate

# Remove an environment
conda env remove -n your_env_name
```	

#### **Conda environment files**
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
Python provides `venv` as a built-in tool for creating virtual environments. `virtualenv` is a third-party tool that provides similar functionality.

#### **Basic commands**

```bash
# Creating a virtual environment
# Using venv (Python 3.3+ built-in)
python -m venv your-env-name

# Using virtualenv (must be installed first)
pip install virtualenv
virtualenv your-env-name

#Activating the environment
# Linux/macOS
source your-env-name/bin/activate
# Windows
your-env-name\Scripts\activate

# Installing a library (package)
pip install lib_name

# Uninstalling a library (package)
pip uninstall lib_name

# To deactivate
deactivate

```

#### **Managing dependencies with `pip`**

A `requirements.txt` file lists all dependencies with their specific versions.

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

Consider using tools that offer more sophisticated dependency management by integrating virtual environment creation and dependency resolution. They maintain a project manifest (e.g., `pyproject.toml` for Poetry) that specifies primary dependencies and generate lockfiles to pin exact versions for reproducibility.

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

#### **Using `uv` for environments and dependencies**

Besides the aforementioned tools, `uv` is becoming increasingly adopted because it provides fast, reproducible Python dependency management built around `pyproject.toml` and a lockfile (`uv.lock`), and can create and manage virtual environments as well as download and select Python versions.

In practice, `uv` can replace `pip`, and often `virtualenv`, while also covering much of what tools like Poetry are used for but with a **clearer separation of responsibilities**. 

::: {.callout-tip icon="false"}
## {{< fa lightbulb >}} `uv` excels at Python-level dependencies

- `uv` does not replace system or distribution-level package managers (such as `conda`, `apt`, or `brew`)
- It is best suited for managing Python-level dependencies on top of an existing Python interpreter
- The Python interpreter can come from the system, a virtual environment, or a `conda` environment
:::

#### **Getting started with `uv`**

`uv` manages Python dependencies, not your operating system or system libraries. Before starting, decide where your Python interpreter comes from in your project:

1. **Use `venv + uv`. Use this when all dependencies are available from PyPI wheels**

- Create a new project
```bash
mkdir my_project
cd my_project
uv init
```
- Create a virtual environment
```bash
uv venv --python 3.12 --seed
```
Now you should have a `.venv/` directory and `pip` installed into it

- Add dependencies
```bash
uv add numpy pandas
```
The command above will update the `pyproject.toml` file, install packages into `.venv` and create a lockfile `uv.lock`

- Run commands inside the environment
```bash
uv run python script.py
uv run pytest
```

Activating the virtual environment is optional, since the commands with `uv` are by default run inside the environment.
```bash
source .venv/bin/activate
```

2. **Use `conda + uv`. Use this when you need non-Python libraries managed by `conda`**

- Create and activate a `conda` environment
```bash
conda create -n myenv python=3.12
conda activate myenv
```

- Install `uv` into the `conda` environment (unless you already have `uv` installed system-wide)
```bash
conda install -c conda-forge uv
```

- Initialize the project
```bash
uv init
```

- Add dependencies
```bash
uv add numpy pandas
```

This time, packages will be installed into the active `conda` environment

- Recreate the environment later
```bash
uv sync
```

This installs exactly what is declared in `pyproject.toml` and `uv.lock`

::: {.callout-tip icon="false"}
## {{< fa lightbulb >}} Some useful commands to make the most out of `uv`

- `uv add --dev <package>`: add a development dependency
- `uv pip list`: list installed Python packages
- `uv pip tree`: show dependency tree
- `uv run <command>`: run a command in the environment
:::

#### **What if you already have a `requirements.txt` file?**

- You can migrate your project to `uv` in a straightforward manner so that `pyproject.toml` and `uv.lock` become the core pieces for reproducing your environment

```bash
# Initialize uv
uv init

# Add everything from requirements.txt
uv add -r requirements.txt
```

- After running the above commands, you should have a `pyproject.toml` file with the dependencies, where the versions are resolved and everything is installed into the environment
- With your `uv.lock` file, the `requirements.txt` file becomes obsolete. You can still keep it around for reference, but ideally you stop updating it manually

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [`uv` documentation](https://docs.astral.sh/uv/)
:::
