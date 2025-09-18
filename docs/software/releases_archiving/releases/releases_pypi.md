---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-04

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
title: Release your Python package

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
  - Package
  - Release
  - Python
  - PyPI
  - TestPyPI
---

After bundling your source code into a package, you can publish it to PyPI. This will allow others to easily install your package using `pip`.

## Testing packaging on TestPyPI before publishing to PyPI

By testing your package on [TestPyPI](https://test.pypi.org) before publishing it to PyPI, you can identify and address any issues with your package metadata, dependencies, or distribution files before making your package publicly available. 

You'll need to create an account for TestPyPI. The next step is to create distribution packages for your package. These packages are archives that can be uploaded to TestPyPI/PyPI and installed using `pip`. Then you can use [Twine](https://twine.readthedocs.io/en/latest/) to upload your package to TestPyPI.

1. Register on TestPyPI.
2. Check if PyPA build is installed:

    ```bash
    pip install --upgrade build
    ```

3. To create distribution packages, navigate to the directory where your `pyproject.toml` file is located, and run:

::: {.panel-tabset}

### Linux/macOS

```bash
python3 -m build
```
### Windows

```bash
py -m build
```

:::

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Output
After running this command, you’ll see a substantial amount of text output. Upon completion, it will generate two files (a wheel and `.tar.gz` file) in the `dist/` directory. The `.tar.gz` file represents a source distribution, while the `.whl` file is a built distribution. More recent versions of `pip` prioritize the installation of built distributions, reverting to source distributions if necessary. It’s advisable to always upload a source distribution and include built distributions compatible with the platforms your project supports.
:::

4. Then, install Twine:

    ```bash
    pip install twine
    ```

5. Upload to TestPyPI by specifying the `--repository` flag:

    ```bash
    twine upload --repository testpypi dist/*
    ```
    - You will be prompted to enter your username and password for TestPyPI.
    - If you have a `~/.pypirc` file, Twine will use the credentials from there.

6. You will find your package on `https://test.pypi.org/project/your_pkg_name`. You can then `pip install` it by adding the `--index-url` flag:

    ```bash
    pip install --index-url https://test.pypi.org/simple/your_pkg_name
    ```

## Publishing to PyPI

Once you have tested your package on TestPyPI and ensured everything works as expected, you can publish it to the official PyPI repository. It will be accessible to anyone in the Python community, allowing them to install your package using a simple `pip install your_pkg_name` command.

You'll also need an account for PyPI. TestPyPI and PyPI use separate databases so you need to register on both sites. However, the workflow is about the same:

1. Register on PyPI.
2. Run `pip install --upgrade build` to ensure you have the latest version of the build tool.
3. Navigate to the directory where your `pyproject.toml` file is located, and run:

::: {.panel-tabset}

### Linux/macOS

```bash
python3 -m build
```
### Windows

```bash
py -m build
```

:::

4. Upload your package to PyPI:

    ```bash
    twine upload dist/*
    ```

    - Input your credentials associated with the account you registered on the official PyPI platform.
5. **Your package is live on PyPI!**
6. You can now install it by simply `pip install your_pkg_name`.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
If you need a particular name for your package, check whether it is taken on PyPI and claim it as soon as possible if available.
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [RealPython Packaging guide](https://realpython.com/pypi-publish-python-package/)
- [Twine Read the Docs](https://twine.readthedocs.io/en/latest/)
- [Using TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/)
:::