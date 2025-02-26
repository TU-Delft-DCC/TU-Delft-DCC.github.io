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
title: Project structure

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
# - repository structures
# - 
# - 

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

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Choosing layout
- [Choosing between a `src/` layout and a flat layout for Python](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
:::

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
├── man/                      # helper files for package functions generated from roxygen2 (if applicable)
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
