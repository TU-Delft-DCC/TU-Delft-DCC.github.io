---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-02

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
title: Creating a Python package

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
  - Software
  - Package
  - Python
  - pyproject.toml
  - uv
---

By turning your code into a package and hosting it on a platform like PyPI (Python Package Index), you enhance the quality and sustainability of your software, promote reuse and embrace contributions from external collaborators.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Comprehensive introduction to Python packaging

- If you are new to Python packaging, please start with the [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) and the [Real Python packaging guide](https://realpython.com/pypi-publish-python-package/). 
- This guide is intended for those who have some experience with Python packages and focuses on the essentials of `pyproject.toml`.
:::

## `pyproject.toml`

In the [*Development workflow*](../../development_workflow/index.md) section we looked at how to [structure your project](../../development_workflow/project_structure.md). Here we will focus on the `pyproject.toml` file, which is a configuration file used in Python projects to define build system requirements and project metadata. It is part of the [PEP 517](https://peps.python.org/pep-0517/) and [PEP 518](https://peps.python.org/pep-0518/) specifications, which aim to standardize the way Python projects are built and packaged. The `pyproject.toml` consists of TOML tables, and can include `[build-system]`, `[project]`, or `[tools]` tables. 

### `[build-system]`

The `[build-system]` table is essential because it defines which [build backend](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend) you will be using, and also which dependencies are required to build your project. This is needed because frontend tools like `pip` are not responsible for transforming your source code into a distributable package, and this is handled by one of the build backends (e.g. setuptools, Hatchling).

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Example

```toml
[build-system]
requires = ["setuptools>=64.0"]
build-backend = "setuptools.build_meta"
```
:::

### `[project]`

Under the `[project]` table you can describe your metadata. It can become quite extensive, but this is where you would list the name of your project, version, authors, licensing, dependencies specific to your project, and other requirements, as well as other optional information. For a detailed list of what can be included under `[project]` check the [Declaring project metadata](https://packaging.python.org/en/latest/specifications/pyproject-toml/#declaring-project-metadata-the-project-table) section of Python Packaging Guide.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Example

```toml
[project]

name = "exampleproject"
# Define the name of your project here. This is mandatory. Once you publish your package for the first time,
# this name will be locked and associated with your project. It affects how users will
# install your package via pip, like so:
#
# $ pip install exampleproject
#
# Your project will be accessible at: https://pypi.org/project/exampleproject/
#
version = "2.0.0"
# Version numbers should conform to PEP 440, and are also mandatory (but they can be set dynamic)
# https://www.python.org/dev/peps/pep-0440/
#
description = "Short description of your project"
# Provide a short, one-line description of what your project does. This is known as the
# "Summary" metadata field:
# https://packaging.python.org/specifications/core-metadata/#summary
#
readme = "README.md"
# Here, you can include a longer description which often mirrors your README file.
# This description will appear on PyPI when your project is published.
# This corresponds to the "Description" metadata field:
# https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#readme
#
requires-python = ">=3.10"
# Indicate the versions of Python your project is compatible with. Unlike the
# 'Programming Language' classifiers, 'pip install' will verify this field
# and prevent installation if the Python version does not match.
#
license = {file = "LICENSE.txt"}
# This specifies the license.
# It can be a text (e.g. license = {text = "MIT License"}) or a reference to a file with the license text as shown above.
#
keywords = ["field_specific_keyword1", "field_specific_keyword2"]
# Keywords that describe your project. These assist users in discovering your project on PyPI searches.
# These should be a comma-separated list reflecting the nature or domain of the project.
#
authors = [
  {name = "A. Doe", email = "author@tudelft.nl" }
]
# Information about the original authors of the project and their contact details.
#
maintainers = [
  {name = "B. Smith", email = "maintainer@tudelft.nl" }
]
# Information about the current maintainers of the project and their contact details.
#
#
#
# Classifiers help categorize the project on PyPI and aid in discoverability.
# For a full list of valid classifiers, see https://pypi.org/classifiers/
classifiers = [
  # Indicate the development status of your project (maturity). Commonly, this is
  #   3 - Alpha
  #   4 - Beta
  #   5 - Stable
  #.  6 - Mature
  "Development Status :: 4 - Beta",

  # Target audience
  "Intended Audience :: Developers",
  "Topic :: Scientific/Engineering",

  # License type
  "License :: OSI Approved :: MIT License",

  # Python versions your software supports. This is not checked by pip install, and is different from "requires-python".
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3 :: Only",
]

# Dependencies needed by your project. These packages will be installed by pip when
# your project is installed. Ensure these are existing, valid packages.
#
# For more on how this field compares to pip's requirements files, see:
# https://packaging.python.org/discussions/install-requires-vs-requirements/
dependencies = [
  "numpy", 
  "pandas>=1.5.3", 
  "matplotlib>=3.7.1"
]
#
# You can define additional groups of dependencies here (e.g., development dependencies).
# These can be installed using the "extras" feature of pip, like so:
#
#   $ pip install exampleproject[dev]
#
# These are often referred to as "extras" and provide optional functionality.
[project.optional-dependencies]
test = ["coverage"]
#
[project.urls]
"Homepage" = "https://github.com/your_handle_or_organisation"
"Source" = "https://github.com/your_handle_or_organisation/exampleproject"
#
# List of relevant URLs for your project. These are displayed on the left sidebar of your PyPI page.
# This can include links to the homepage, source code, changelog, funding, etc.
#
#
# This [project] example was adopted from https://github.com/pypa/sampleproject/blob/main/pyproject.toml
```
:::

### `[tools]`

The `[tool]` table contains subtables specific to each tool. For example, Poetry uses  the `[tool.poetry]` table instead of the `[project]` table.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} **Example:** [Poetry project setup](https://python-poetry.org/docs/basic-usage/)
:::

:::{.callout-important appearance="simple" icon="false"}
## **{{< fa triangle-exclamation >}} Difference between `[build system]` and `[project]`**
<br>
The `[build-system]` and `[project]` tables serve distinct roles. The `[build-system]` table must always be included, as it specifies the build tool used, regardless of the backend. On the other hand, the `[project]` table is recognized by most build backends for defining project metadata, though some backends may not and use a different format.
:::


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [`pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [Configuring setuptools using `pyproject.toml` files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
:::


Before shifting to `pyproject.toml`, a common approach was to use a `setup.py` build script. You might encounter them in legacy projects.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Is `setup.py` deprecated?](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/#setup-py-deprecated)
- [How to modernize a `setup.py` based project?](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)
:::

## Package structuring 

If you want to distribute your Python code as a package, you will need to have an `__init__.py` file in the root directory of your package. This allows Python to treat that directory as a package that can be imported. Every subfolder should also contain an `__init__.py` file.

When importing a package, Python searches through the directories on `sys.path` looking for the package subdirectory. The presence of `__init__.py` files within these directories is crucial, as it tells Python that these directories should be treated as packages. This mechanism helps avoid the scenario where directories with commonplace names accidentally overshadow valid modules that appear later in the search path. 

While `__init__.py` can simply be an empty file, serving just to mark a directory as a package, it can also contain code that runs when the package is imported. This code can initialize package-level variables, import submodules, and other tasks.


Referring to the [project structure](../../development_workflow/project_structure.md) in our [*Development workflow*](../../development_workflow/index.md) guide, we can build on top of that structure. 


:::{.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} **Reminder about flat vs `src` layout**

In a flat layout, the project's root directory directly contains the package directories and modules. This layout is straightforward and works well for simple projects.

```bash
your_project/
│
├── your_pkg_name/ 
│   ├── __init__.py
│   ├── module.py
│   └── subpkg1/
│       └── __init__.py
│
...
```

The `src` layout places the package directory inside a top-level `src` directory. This layout helps prevent accidental imports from the current working directory, ensuring that you always import from the installed package rather than the source directory.

```bash
your_project/
│
├── src/
│   └── your_pkg_name/ 
│       ├── __init__.py
│       ├── module.py
│       └── subpkg1/
│           └── __init__.py
│
...
```
:::


So our example package structure would now look like this:

::: {.panel-tabset}

### **Python**

```bash
your_project/
│
├── docs/                     # Documentation directory
├── notebooks/                # Jupyter notebooks
├── src/                      # Contains your main code
│   └── your_pkg_name/        # A folder where your organized code lives - your package
│       ├── __init__.py       # A marker file for package initialization
│       ├── module.py         # A nested module
│       └── subpkg1/          # A sub-package
│           └── __init__.py   # A marker file for sub-package initialization
├── tests/                    # Your test directory  
│
├── data/                     # Data files used in the project (if applicable)
├── processed_data/           # Files from your analysis (if applicable)
├── results/                  # Results (if applicable)
│
├── .gitignore                # Untracked files 
├── pyproject.toml            # TOML file
│
│
├── README.md                 # README
└── LICENSE                   # License information
```
:::

You might notice that in our updated structure the `requirements.txt` is absent. In many cases, if you have a `pyproject.toml` file, you may not need a `requirements.txt` file anymore, since the `pyproject.toml` file is part of the new standardized Python packaging format (defined in [PEP 518](https://peps.python.org/pep-0518/)) and can include dependencies.

However, some deployment and CI/CD pipelines might still expect a `requirements.txt` file, because a set of fixed dependency versions creates more stable pipelines. For simple projects, you can still prefer to use a `requirements.txt` for its simplicity and wide adoption. 

:::info
It is not considered best practice to use the `pyproject.toml` to pin dependencies to specific versions or to specify sub-dependencies (i.e. dependencies of your dependencies). This is overly-restrictive, and prevents a user from gaining the benefit of dependency upgrades. For more info, see [**this discussion**](https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/).
:::

### `lib/` and `build/` directories

It is possible that you might have `lib/` and `build/` directories in your project. These directories are not part of the standard Python package structure, but they can be created by certain tools or processes.

- The `build/` directory is typically used to store compiled or built artifacts of your project, such as binary executables, wheels, or other distribution files. This directory is usually not part of your source code repository and is generated during the (automated) build or packaging process.
- The `lib/` directory stores third-party libraries or dependencies that are not installed through a package manager. By specifying your project's dependencies in the `pyproject.toml` file, and using a package manager like `pip` or `poetry` to install and manage them, these dependencies will be automatically downloaded and installed in the appropriate location (usually the site packages directory).

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Good integration practices](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html)
- [Python documentation packages](https://docs.python.org/3/tutorial/modules.html#packages)
:::

## Local package installation
By installing a Python package locally during development you can test your changes in an environment that mimics how the package will be used once it is deployed. This process allows you to ensure that your package works correctly when installed and imported by others.

You can use `pip` to install your package in editable mode (`-e`). This way, changes you make to the source code are immediately available without needing to reinstall the package.

```python
pip install -e .
```

## Next steps

Once you have your package ready, you can publish it. Visit our [*Release your Python package*](../releases/releases_pypi.md) guide for information on how to publish your package to PyPI.

### Using `uv` for building and releasing Python packages

If you're looking to streamline your Python packaging workflow even further, consider using `uv`. Alongside traditional tooling, `uv` offers a fast, unified workflow for packaging. It reads project metadata from `pyproject.toml`, builds source and wheel distributions, and can publish directly to package indexes (e.g., PyPI). This consolidates steps that typically require separate tools (e.g., `build` and `twine`) and helps keep release processes consistent across local development and continuous integration.

In practice, `uv build` produces artifacts under `dist/` using the configured build backend, and `uv publish` can upload those artifacts using PyPI API tokens or interactive credentials. Because `uv` also manages environments and Python runtimes, the same tool can be used to create an isolated build environment, lock dependencies for reproducibility, and run test commands before releasing.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [`uv` documentation](https://docs.astral.sh/uv/)
:::
