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

When using Python you have multiple options to manage dependencies and environments, each suited to different needs. To ensure reproducibility and manage dependencies use:

### Conda Environments

Conda is a popular choice within the research community for managing dependencies and environments. Conda is a system package manager that allows for managing both packages and environments. It is ideal for projects requiring specific Python versions, packages not available via pip.

**To create a conda environment:**

```bash
conda create -n your_env_name python=3.12
# You can specify your Python version
```
**To activate:**
```bash
conda activate your_env_name
```
**To export your environment:**
```bash
conda env export > environment.yml
```
**To deactivate:**
```bash
conda deactivate
```
**To list your conda environments:**
```bash
conda env list
```
**To delete an environment:**
```bash
conda env remove -n your_env_name
```

### Virtual Environments (`venv`/`virtualenv`)

If you prefer or need a pip-based solution, tools like `venv` or `virtualenv` allow you to create isolated Python environments. This prevents package versions installed globally from interfering with your project-specific dependencies.

**To create a virtual environment:**

```bash
# Using venv (Python 3.3+ built-in)
python -m venv your-env-name

# Using virtualenv (requires pip install first)
pip install virtualenv
virtualenv your-env-name
```

**To activate:**

```bash
# Linux/macOS
source your-env-name/bin/activate

# Windows
your-env-name\Scripts\activate
```
**Export `requirements.txt` from an activated environment:**
```bash
pip freeze > requirements.txt
```
This provides a snapshot of your dependencies.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
You can use [`pip-chill`](https://pypi.org/project/pip-chill/) instead of `pip freeze` to generate a cleaner `requirements.txt` that lists only your explicitly installed packages, excluding OS-specific dependencies and sub-dependencies. This avoids bloat and ensures reproducibility across environments while allowing version flexibility.
:::

**To deactivate:**
```bash
deactivate
```
**To list your environments:**

Virtual environments created with `venv` or `virtualenv` must be manually tracked through your filesystem. However, with `virtualenv` you can install the `virtualenvwrapper` extension that allows for easier managing of your development workflow.

**To delete an environment:**

You'll need to manually navigate and remove your environment directories. However, if you are using `virtualenv` with `virtualenvwrapper` you can remove an environment using the `rmvirtualenv` command:
```bash
rmvirtualenv your-env-name
```

### Dependency Files

A `requirements.txt` or `environment.yml` file lists all dependencies with their specific versions. 

**To recreate an environment in conda:**
```bash
conda env create -f environment.yml
```
**With pip:**

```bash
python -m venv your-new-env
#or
virtualenv your-new-env
#then (macOS/Linux)
source your-new-env/bin/activate
# or (Windows)
your-new-env\Scripts\activate
```
then navigate to where your `requirements.txt` is located, and
```bash
pip install -r requirements.txt
```

### Dependency Management Tools

Tools like `poetry` and `pipenv` provide a more sophisticated dependency management by handling virtual environment creation and dependency resolution in a more integrated manner. They maintain a project manifest (e.g., `pyproject.toml` for Poetry) that specifies primary dependencies and generate lock files to pin exact versions for reproducibility.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [CodeRefinery - Recording dependencies](https://coderefinery.github.io/reproducible-research/dependencies/)
- [The Turing Way - Package Management Systems](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package)
- [Conda documentation](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
- [virtualenv documentation](https://virtualenv.pypa.io/en/latest/)
- [virtualenvwrapper extension](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [pipenv documentation](https://pipenv.pypa.io/en/latest/)
- [poetry documentation](https://python-poetry.org/docs/)
- [pip-chill on PyPI](https://pypi.org/project/pip-chill/)
:::



