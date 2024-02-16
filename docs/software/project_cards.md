# FAIR assessment cards

Add the cards below as issues to your repository to track the progress of adopting the best practices for FAIR research software.

````{panels}
:column: col-lg-12 p-2
:header: bg-info

**Version Control**
^^^

```md
_Essential_  
- [ ] Use [git](https://www.atlassian.com/git) as a version control system 
- [ ] Upload your project on [GitHub](https://github.com/) or [TU Delft GitLab](https://gitlab.tudelft.nl/)

_Recommended_  
- [ ] Make your repository [public](https://coderefinery.github.io/social-coding/)
- [ ] [Branch hygiene](https://coderefinery.github.io/git-branch-design/)
- [ ] [Meaningful commit messages](https://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
```

---
**Dependency management**
^^^

```md
_Essential_
- [ ] Document your project dependencies
- [ ] Provide instructions for replicating the computational environment

_Recommended_
- [ ] Use a [dependency manager](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package.html)
- [ ] Pin [exact versions](https://github.com/conda/conda-lock) used to generate your environment

_Optional_
- [ ] [Containerized workflow](https://the-turing-way.netlify.app/reproducible-research/renv/renv-containers.html)
```

---
**Project documentation**
^^^

```md
_Essential_  
- [ ] [README](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md)
- [ ] [LICENSE](https://doi.org/10.5281/zenodo.4629662)
- [ ] [CITATION](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

_Recommended_  
- [ ] Make use of [Github issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [ ] [Code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
```

---
**Software documentation**
^^^

```md
_Essential_  
- [ ] Installation instructions
- [ ] User documentation
- [ ] Developer documentation
- [ ] Source code documentation ([docstrings](https://numpydoc.readthedocs.io/en/latest/format.html))

_Recommended_  
- [ ] Examples and tutorials (Jupyter notebooks, videos, screencasts)
- [ ] Automate documentation building with [sphinx](https://coderefinery.github.io/sphinx-lesson/)
- [ ] Website ([github.io pages](https://pages.github.com/), [Readthedocs](https://readthedocs.org/), [JupyterBook](https://jupyterbook.org/intro.html))

_Optional_  
- [ ] Build [API reference](https://developer.lsst.io/python/numpydoc.html) from docstrings
```

---
**Collaboration**
^^^

```md
_Essential_
- [ ] Make use of [Github issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [ ] Provide contribution [guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)

_Recommended_
- [ ] Choose a branching model ([DCC Guides on branches](https://tu-delft-dcc.github.io/software/git/branch_management.html))
- [ ] Make use of [issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [ ] Provide a [Code of Conduct](https://www.contributor-covenant.org/)
- [ ] Use [semantic versioning](https://semver.org/) for your releases
```

---
**Software testing**
^^^

```md
_Essential_
- [ ] Document verification of user installation
- [ ] Document how users can verify the proper functioning of the software

_Recommended_  
- [ ] [Defensive programming](https://swcarpentry.github.io/python-novice-inflammation/10-defensive/index.html)
- [ ] Test your software with [integration tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-integrationtest.html) and [unit tests](https://the-turing-way.netlify.app/reproducible-research/testing/testing-unittest.html)
- [ ] Make use of [Continuous Integration](https://the-turing-way.netlify.app/reproducible-research/ci/ci-options.html)
- [ ] Code coverage check ([Codecov](https://about.codecov.io/), [Sonarcloud](https://sonarcloud.io/), [Travis](https://www.travis-ci.com/))
```

---
**Code quality**
^^^

```md	
_Essential_
- [ ] Project [organisation](https://coderefinery.github.io/reproducible-research/organizing-projects/)
- [ ] Record [software dependencies](https://coderefinery.github.io/reproducible-research/dependencies/)

_Recommended_
- [ ] Follow a consistent code style, such as [PEP8 guidelines](https://realpython.com/python-pep8/)
- [ ] Use a linter ([pylint](https://pypi.org/project/pylint/), [flake8](https://pypi.org/project/flake8/))
- [ ] Use a formatter ([black](https://github.com/psf/black), [yapf](https://github.com/google/yapf))
- [ ] Follow [best coding practices](https://alan-turing-institute.github.io/rse-course/html/module07_construction_and_design/index.html)
```

---
**Releases**
^^^

```md
_Essential_  
- [ ] Obtain a DOI from ([Zenodo](https://zenodo.org/) or [4TU.ResearchData](https://data.4tu.nl/info/about-your-data/getting-started))

_Recommended_  
- [ ] [Semantic versioning](https://semver.org/)
- [ ] Tagged releases ([GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github))
- [ ] [CHANGELOG](https://keepachangelog.com/en/1.0.0/)
- [ ] Upload to registry ([PyPI](https://realpython.com/pypi-publish-python-package/), [conda](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html), [DockerHub](https://docs.docker.com/docker-hub/repos/))
- [ ] [Release guide](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [ ] [Continuous Integration](https://the-turing-way.netlify.app/reproducible-research/ci/ci-options) for build and release
```

````    

