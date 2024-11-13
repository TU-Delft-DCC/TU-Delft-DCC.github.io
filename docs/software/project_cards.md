---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
date: 11/13/2024

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: FAIR assessment cards

# Authors of the document, will not be parsed [manual entry]
author_1: Maurits Kok
author_2: Elviss Dvinskis

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Elviss Dvinskis
maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
categories: 
 - FAIR
 - Checklist

---

Add the cards below as issues to your repository to track the progress of adopting the best practices for FAIR research software.

## **Version Control**

```md
_Essential_
- [ ] Use [git](https://www.atlassian.com/git) as a version control system 
- [ ] Upload your project on [GitHub](https://github.com/) or [TU Delft GitLab](https://gitlab.tudelft.nl/)

_Recommended_  
- [ ] Make your repository [public](https://coderefinery.github.io/social-coding/)
- [ ] Consider your [branch hygiene](https://coderefinery.github.io/git-branch-design/)
- [ ] Use a branching model (e.g. [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow))
- [ ] Use [meaningful commit messages](https://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
```

## **Collaboration**

```md
_Essential_  
- [ ] Make use of [GitHub issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)

_Recommended_
- [ ] [Contribution guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [ ] [Code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
```

## **Project documentation**

```md
_Essential_  
- [ ] [README](https://www.makeareadme.com)
- [ ] Apply a TU Delft pre-approved [LICENSE](https://zenodo.org/records/4629635)
- [ ] [CITATION](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
```

## **Software documentation**

```md
_Essential_  
- [ ] Source code documentation ([docstrings](https://numpydoc.readthedocs.io/en/latest/format.html))
- [ ] Document your project dependencies
- [ ] Installation instructions
- [ ] User documentation

_Recommended_  
- [ ] Developer documentation and setup
- [ ] Examples and tutorials (e.g. Jupyter Notebooks)

_Optional_
- [ ] Documentation tools ([Sphinx](https://coderefinery.github.io/documentation/sphinx/), [JupyterBook](https://jupyterbook.org/intro.html), [Quarto](https://quarto.org/docs/guide/))
- [ ] Build an [API reference](https://developer.lsst.io/python/numpydoc.html) from docstrings
- [ ] Hosting ([GitHub Pages](https://pages.github.com/), [Readthedocs](https://readthedocs.org/))
```

## **Software testing**

```md
_Essential_
- [ ] Installation/execution verification

_Recommended_
- [ ] [Defensive programming](https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html)
- [ ] Test your software with [integration tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-integrationtest.html) and [unit tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-unittest.html)
- [ ] Make use of [Continuous Integration](https://coderefinery.github.io/testing/continuous-integration/) to automate testing

_Optional_
- [ ] Code coverage check (e.g. [Sonarcloud](https://sonarcloud.io/), [codecov](https://about.codecov.io))
```

## **Software quality**

```md
_Essential_
- [ ] [Organize](https://coderefinery.github.io/reproducible-research/organizing-projects/) your project for reproducibility
- [ ] [Record and manage](https://coderefinery.github.io/reproducible-research/dependencies/) your software dependencies 

_Recommended_
- [ ] Make [refactoring](https://refactoring.guru/refactoring) part of your workflow
- [ ] Follow [best coding practices](https://alan-turing-institute.github.io/rse-course/html/module07_construction_and_design/index.html)

_Recommended for Python_
- [ ] Follow [PEP8 guidelines](https://realpython.com/python-pep8/)
- [ ] Use a tool for dependency management (e.g. [poetry](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package.html))
- [ ] Use linter (e.g. [pylint](https://pypi.org/project/pylint/), [flake8](https://pypi.org/project/flake8/))
- [ ] Use a formatter (e.g. [black](https://github.com/psf/black))
```

## **Releases**

```md
_Essential_  
- [ ] Obtain a DOI ([Zenodo](https://zenodo.org/) or [4TU.ResearchData](https://data.4tu.nl/info/about-your-data/getting-started))

_Recommended_  
- [ ] Use [semantic versioning](https://semver.org/)
- [ ] Create tagged releases ([GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github))
- [ ] [CHANGELOG](https://keepachangelog.com/en/1.0.0/)
- [ ] Upload to [registry](https://github.com/NLeSC/awesome-research-software-registries) (e.g. [PyPI](https://realpython.com/pypi-publish-python-package/), [conda](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html))
- [ ] [Releasing guide](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

_Optional_
- [ ] [Continuous Integration](https://the-turing-way.netlify.app/reproducible-research/ci/ci-options.html) for automated build and release
``` 

