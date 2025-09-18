---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-23

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-28

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Tooling

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Maurits Kok
author_2: Elviss Dvinskis

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
  - Software
  - Documentation
  - Sphinx
  - JupyterBook
  - MkDocs
  - Quarto
  - pkgdown
---

There are various tools available that can help you create, manage, and deploy project documentation more effectively.

## Sphinx
Sphinx is a versatile documentation tool that is well-suited for documenting Python projects due to its easy integration with Python's docstrings. Its capabilities extend beyond Python, making it a great solution for creating comprehensive documentation for projects in various programming languages (e.g. MATLAB).

Some key features of Sphinx include:

- Cross-referencing code and documentation across files.
- Automatic generation of documentation from docstrings.
- Syntax highlighting for code examples.
- Support for extensions and custom themes.
- Multiple output formats.

### Getting started with Sphinx

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} Tip
To get started with Sphinx, we recommend the [Coderefinery lesson on Sphinx and Markdown](https://coderefinery.github.io/documentation/sphinx/)
:::

1. **Install dependency:** You can [install Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html) in various ways, either through `apt-get` for Linux, Homebrew for macOS, or through Chocolatey for Windows. Assuming you have Python on your machine you can install it through `conda` or `pip`.
1. **Setup documentation:** Create a directory for your documentation (`/docs`), and run `sphinx-quickstart` in that directory. The default answers to the questions are fine.
1. **Configure Sphinx:** Once you have the `conf.py` and `index.rst` files, you will need to modify them further. The `index.rst` file acts as the front page of your documentation and the root of the table of contents. The `conf.py` file is the main configuration file for the Sphinx documentation. It holds all your extensions and controls various aspects of the build process that can be customized to suit your needs. For example, `sphinx.ext.autodoc` is used for pulling documentation from docstrings, and `sphinx.ext.mathjax` for displaying mathematical content.
    - [Built-in extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
    - [Third-party extensions](https://github.com/sphinx-contrib/)
1. **Write content:** Add content to your documentation. In addition to reStructureText, Sphinx also integrates with markdown documentation through the [MyST parser](https://myst-parser.readthedocs.io/en/latest/).
1. **Build documentation:** Once you have added the documentation files, you can build the documentation from the folder `/docs` with `sphinx-build . _build/` or `make html`.
1. **Further customization:** You can customize the look of your documentation by changing [themes](https://sphinx-themes.org/) in the `conf.py` file.

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} Sphinx configuration template

::: {.callout-note collapse="true" icon=false appearance="simple"} 
## `config.py`
```python
# Configuration file for the Sphinx documentation builder
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, as shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = "Project"
copyright = "year, name"
author = "name"

# The master toctree document.
master_doc = "index"

# The full version, including alpha/beta/rc tags
release = "0.1.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser", # MyST markdown parser
    "sphinxcontrib.matlab", # Required for MATLAB
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx_tabs.tabs"
]

myst_enable_extensions = [
    "linkify",
]

# MATLAB settings for autodoc
# here = os.path.dirname(os.path.abspath(__file__))
# matlab_src_dir = os.path.abspath(os.path.join(here, ".."))
# primary_domain = "mat"

# Napoleon settings
napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_use_param = False
# napoleon_preprocess_types = True

# This value contains a list of modules to be mocked up.
# autodoc_mock_imports = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# html_theme = "sphinx_book_theme"
html_theme = "sphinx_rtd_theme"
# html_theme = "pydata_sphinx_theme"


html_title = "title"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
```
:::

{{< fa exclamaition >}} When using Sphinx extensions or custom themes beyond core functionality, a `requirements.txt` file is mandatory for reproducible documentation builds across environments. For example, this is required for hosting platforms like Read the Docs.

::: {.callout-note collapse="true" icon=false appearance="simple"} 
## `requirements.txt`
```markdown
# Core
sphinx

# Sphinx extensions
sphinxcontrib-matlabdomain # Only for matlab source code
sphinx-tabs
sphinx-copybutton

# MyST parser
myst-parser
linkify-it-py

# Themes
pydata-sphinx-theme
sphinx-book-theme
sphinx-rtd-theme
```
:::
:::


:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}}  **Example repositories using Sphinx for Python:**

- [Python's official documentation is created using Sphinx](https://docs.python.org/3/)
- [Read The Docs](https://docs.readthedocs.io/en/stable/) - the platform for hosting documentation is itself documented using Sphinx.
- [NumPy](https://numpy.org/doc/stable/)
:::

### Sphinx autodoc
Once the Sphinx `config.py` is set up, you can generate the API reference documentation by using the [sphinx-autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). By creating `.rst` files with the autodoc syntax, Sphinx will build the API reference.

### Sphinx-matlabdomain
For documenting MATLAB projects, Sphinx can be extended for MATLAB. The [**sphinxcontrib-matlabdomain**](https://pypi.org/project/sphinxcontrib-matlabdomain/) extension allows Sphinx to interpret and render MATLAB specific documentation. The extension can be installed through `pip install sphinxcontrib-matlabdomain` and add the extension to the `conf.py` file. 

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} **Example repositories using sphinx for MATLAB:** 

- [ENIGMA Toolbox](https://enigma-toolbox.readthedocs.io/en/latest/) - provides documentation in both Python and MATLAB, generated by Sphinx and hosted using Read the Docs.
- [Cobra Toolbox](https://opencobra.github.io/cobratoolbox/stable/index.html)
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Coderefinery lesson on Sphinx and Markdown](https://coderefinery.github.io/documentation/sphinx/)
- [Getting started with Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
:::

## Jupyter Book
Jupyter Book uses Sphinx to convert notebooks and Markdown documents into an interactive publishing framework (with executable content). It integrates Jupyter Notebooks with Sphinx's documentation capabilities, enabling features like cell execution and output caching directly within the documentation. Jupyter Book is essentially a specialized wrapper around Sphinx and the MyST-NB extension, designed to make publishing content easier.

:::{.callout-note appearance="simple" icon="false"}
{{< fa info-circle >}} The [TU Delft OPEN Interactive Textbooks](https://textbooks.open.tudelft.nl/textbooks/catalog/category/interactive) platform uses Jupyter Book to create textbooks. 
:::

### Features
- Jupyter Book can integrate outputs by allowing code execution within the content, making it ideal for tutorials, courses, and technical documentation that require live examples.
- Jupyter Book uses Markdown for Jupyter (MyST) which extends the traditional Markdown syntax to include features normally available in reStructuredText (reST). **This makes it easier to include complex formatting and dynamic content directly in Markdown files.**
- Jupyter Book can execute notebook cells and cache outputs. This means that content including code outputs can be generated once and reused.

### Getting started
JupyterBook has extensive documentation on getting [started with building a book](https://jupyterbook.org/en/stable/start/your-first-book.html#).


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Further reading
- [How Jupyter Book and Sphinx relate to one another](https://jupyterbook.org/en/stable/explain/sphinx.html)
:::

## MkDocs
MkDocs is a static site generator that uses markdown for all documentation, simplifying the writing process, and is configured with a single YAML file. It is lightweight compared to Sphinx but less feature-rich for complex use cases, and is best suitable for straightforward project documentation without heavy API generation needs.

### Getting started

1. You can install it through pip (`pip install mkdocs`). Then you can initialize your MkDocs project by running `mkdocs new your_project_name`.
2. Place your markdown documentation in your `docs` directory and define the structure in your `mkdocs.yml` file.
3. You can preview your site locally and see live updates as you make changes by running `mkdocs serve`.
4. When you want to publish your documentation run `mkdocs build`.
5. MkDocs is designed to be hosted on almost any static file server and works well with GitHub Pages.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
 - [MkDocs](https://www.mkdocs.org) official site that includes a Getting Started and User Guide.
:::

## Quarto
Similar to Jupyter Book, Quarto is a publishing framework that allows you to create dynamic documents, presentations, reports, websites, and more. It supports multiple programming languages, including Python, R, and Julia, enabling the inclusion of executable code, interactive visualizations, equations, and rich formatting directly within the documents.

::: {.callout-warning appearance="simple" icon="false"}
**⮕ All of these guides are created with Quarto!**
:::

### Getting started
1. **Downloading:** You can download the installer for your operating system from the [Quarto website](https://quarto.org/docs/get-started/).
2. **Running Quarto:** You can run Quarto either from your command line or from VS Code, JupyterLab, RStudio, or any text editor. For VS Code you will need to install a Quarto extension. It is a stand-alone application and does not require Python.
3. **Markdown flavour:** Quarto projects use `.qmd` files which are a Markdown flavour.

:::{.callout-note appearance="simple" icon="false" collapse="true"}    
## {{< fa info-circle >}} Basic structure of a Quarto file
```
    ---
    title: "Your Document Title"
    format: html # Or pdf, word, etc.
    ---

    # Introduction

    Some text...

    ## Section 1

    Some text...

    ```python
    # This is a code block
    import pandas as pd
    data = pd.read_csv("data.csv")
    print(data.head())
    ```

    ## Section 2

    Some more text....

```
:::
4. **Adding content:** Write your text using standard Markdown syntax and add [code blocks](https://quarto.org/docs/authoring/markdown-basics.html#source-code).
5. **Building documentation:**
    - To compile a Quarto document, use `quarto render your-file-name.qmd`. This command converts your `.qmd` file into the output format specified in the file’s header (e.g., HTML, PDF).
    - You can watch a file or directory for changes and automatically re-render with `quarto preview your-file-name.qmd`, which is useful to see live updates.
6. **Additional features:**
    - Quarto supports cross-referencing figures, tables, and other elements within your document. You can also use BibTeX for citations.
    - You can have interactive components for web outputs (e.g. embeded Plotly charts).
    - Extensive options for custom styles and layouts.
7. **Publishing**: Quarto documents are portable and can be shared as is, allowing others to compile them on their own systems or published by hosting the output files on a server like GitHub Pages.

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} Examples
- [Quarto gallery](https://quarto.org/docs/gallery/)
:::

:::{.callout-note appearance="simple" icon="false"}
### {{< fa info-circle >}} PDF engine
In order to create PDFs you will need to install a LaTeX engine if you do not have one installed already. You could use a lightweight distribution like TinyTeX, which you can install with `quarto install tool tinytex`.
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Getting started with Quarto](https://quarto.org/docs/get-started/)
- [Comprehensive guide to using Quarto](https://quarto.org/docs/guide/)
- [Carpentries Incubator - Introduction to Working with Quarto documents](https://carpentries-incubator.github.io/reproducible-publications-quarto/05-quarto-documents.html)

:::

## Tools for R

R project documentation generally includes in-line comments and function documentation using `roxygen2`. Additionally, comprehensive examples and usage guides are often provided through vignettes, which are included within an R package itself.

To extend `roxygen2` documentation into a static website for your package you can use `pkgdown`. `pkgdown` automatically generates a website from your package's documentation and vignettes, similar to how Sphinx is used for Python projects.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [`pkgdown`](https://pkgdown.r-lib.org/index.html)
:::
