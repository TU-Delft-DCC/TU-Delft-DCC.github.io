---
section: software
title: FAIR4RS checklist
author_1: Maurits Kok
author_2: Elviss Dvinskis
---

# FAIR checklist for research software

The goal of the FAIR principles is to improve research transparency, reproducibility and reusability. To achieve this, your research needs to be described through metadata, should be open for inspection, well-documented, and well structured. This ensures that it can be replicated, expanded upon, merged, reinterpreted, or reimplemented. The acronym FAIR stands for:

- **F**indable: Your research software can be easily found (i.e. has rich metadata, unique identifiers).
- **A**ccessible: Once found, it can be accessed, ideally through well-defined and open protocols.
- **I**nteroperable: Your research is compatible with other datasets, tools, and workflows, allowing for integration and reuse across various applications and fields.
- **R**eusable: The ultimate goal is that your research outputs can be reused in different contexts. This requires comprehensive documentation, clear licensing, and a modular structure.

While originally targetting data management, the FAIR for Research Software (FAIR4RS) extends these principles to research software, which, unlike data, is executable and evolves over time. Ensuring the findability of software involves metadata, identifiers, and version control systems, while accessibility includes guidelines for obtaining, installing, and running the software. Interoperability involves adherence to community-driven standards or protocols, and reusability requires detailed documentation and user guides to effectively apply the software in new research projects.

:::{seealso}

- [FAIR Guiding Principles for scientific data management and stewardship to research software](https://zenodo.org/records/6623556)
- [FAIR4RS community in Zenodo](https://zenodo.org/communities/fair4rs/records?q=&l=list&p=1&s=10&sort=newest)
- [FAIR Software Checklist](https://fair-software.nl/) - five recommendations for FAIR (scientific) software 
:::


## Checklist

:::{admonition} Version Control  
_Essential_
- [ ] Use [git](https://www.atlassian.com/git) as a version control system 
- [ ] Upload your project on [GitHub](https://github.com/) or [TU Delft GitLab](https://gitlab.tudelft.nl/)

_Recommended_  
- [ ] Make your repository [public](https://coderefinery.github.io/social-coding/)
- [ ] Consider your [branch hygiene](https://coderefinery.github.io/git-branch-design/)
- [ ] Use a branching model (e.g. [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow))
- [ ] Use [meaningful commit messages](https://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
:::

:::{admonition} Collaboration
_Essential_  
- [ ] Make use of [GitHub issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)

_Recommended_
- [ ] [Contribution guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [ ] [Code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)

:::

:::{admonition} Project documentation
_Essential_  
- [ ] [README](https://www.makeareadme.com)
- [ ] Apply a TU Delft pre-approved [LICENSE](https://zenodo.org/records/4629635)
- [ ] [CITATION](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

:::

:::{admonition} Software documentation
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
:::

:::{admonition} Software testing
_Essential_
- [ ] Installation/execution verification

_Recommended_
- [ ] [Defensive programming](https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html)
- [ ] Test your software with [integration tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-integrationtest.html) and [unit tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-unittest.html)
- [ ] Make use of [Continuous Integration](https://coderefinery.github.io/testing/continuous-integration/) to automate testing

_Optional_
- [ ] Code coverage check (e.g. [Sonarcloud](https://sonarcloud.io/), [codecov](https://about.codecov.io))
:::

:::{admonition} Software quality
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
:::

:::{admonition} Releases
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
:::

## Example repositories
* [eScience Center - matchms](https://github.com/matchms/matchms) - Matchms is an open-source Python package to import, process, clean, and compare mass spectrometry data.
* [TU Delft - Transposonmapper](https://github.com/SATAY-LL/Transposonmapper) - Transposonmapper is an open-source python package and Docker image for mapping transposons from sequencing data.

:::{seealso}
For more information on the principles behind FAIR software, please have a look at the following resources:

- [The Turing Way - Guide for Reproducible Research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html) - general guide to reproducible research
- [Towards FAIR principles for research software](https://content.iospress.com/articles/data-science/ds190026) - publication on the translation of FAIR principles for data to FAIR principles for software
- [From FAIR research data toward FAIR and open research software](https://doi.org/10.1515/itit-2019-0040)
- [FAIR Principles for Research Software](https://zenodo.org/records/6623556)
:::

## Acknowledgements
The checklist was in part based on the checklist provided by the [eScience Center](https://guide.esciencecenter.nl/#/nlesc_specific/checklist_matrix), licensed under CC BY 4.0.