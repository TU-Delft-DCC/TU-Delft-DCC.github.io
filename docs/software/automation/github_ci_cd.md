---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-22

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-10-28

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: GitHub Actions

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
  - Automation
  - GitHub
  - CI/CD

---

[GitHub Actions](https://docs.github.com/en/actions) is a CI/CD platform that automates building, testing, and deploying code. You can set up workflows that build and test every pull request in your repository, and optionally deploy changes after those pull requests are merged, triggered automatically based on your chosen rules.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Exploring GitHub Actions

[Setting up a demo workflow in GitHub Actions.](https://docs.github.com/en/actions/quickstart)
:::

:::{.callout-tip appearance="simple" icon="false"}
### {{< fa lightbulb >}} Tips
- GitHub has templates available. Go to the **Actions tab** in your repository and select **new workflow** for an overview.
- You can find [**workflow examples**](https://github.com/sdras/awesome-actions) shared in the community.
- Add **`workflow_dispatch`** as a trigger for your GitHub Actions workflow. With this trigger, you can [**manually run an action**](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow), instead of having to rely on external triggers. This is quite useful when testing your workflow.
- Test your workflow in a separate branch to avoid committing many small changes during debugging of the workflow.
:::

### Automating testing
A common usecase of automation is to trigger automatic testing when pushing changes and creating pull requests.

::: {.panel-tabset}

#### Python
The example below is taken from the CodeRefinery lesson on [Continuous Integration](https://coderefinery.github.io/testing/continuous-integration/).

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa circle-check >}} Python testing

```yaml
name: Python package testing

on:
  push:
    branches: [ "main", "develop" ]
  pull_request:
    branches: [ "main", "develop" ]
  workflow_dispatch:
  
jobs:
  test:
    permissions:
      contents: read
      pull-requests: write

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest pytest-cov
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the job if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest and calculate coverage
      run: |
        pytest --cov-report "xml:coverage.xml"  --cov=.
    - name: Create Coverage 
      if: ${{ github.event_name == 'pull_request' }}
      uses: orgoro/coverage@v3.1
      with:
          coverageFile: coverage.xml
          token: ${{ secrets.GITHUB_TOKEN }}
```
:::

#### MATLAB
MATLAB has multiple [pre-defined GitHub Actions available](https://github.com/matlab-actions) to use in your workflows.

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa circle-check >}} MATLAB testing

```yaml
name: Generate Test and Coverage Artifacts
on:
  push:
    branches: [ "main", "develop" ]
  pull_request:
    branches: [ "main", "develop" ]
  workflow_dispatch:
 
jobs:
  test:
    name: Run MATLAB Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Set up MATLAB
        uses: matlab-actions/setup-matlab@v2
        with:
          release: R2024a
      - name: Run tests
        uses: matlab-actions/run-tests@v2
        with:
          source-folder: src
          test-results-junit: test-results/results.xml
          code-coverage-cobertura: code-coverage/coverage.xml
      - name: Upload coverage reports to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: code-coverage/coverage.xml
          token: ${{ secrets.CODECOV_TOKEN }}
```
:::

This workflow uses Codecov to analyse the coverage report (free service for public repositories). 

⮕ Learn more about [Codecov](https://about.codecov.io/)

:::

### Automating documentation generation
[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website.

In order to deploy the documentation generated by the workflow below, you need to navigate to **Settings -> Pages** in your repository and set:

1. Source: "Deploy from a branch"
1. Branch: `gh-pages` from `root`

It is a best practice to only deploy new documentation to the `gh-pages` branch upon a Pull Request to the `main` branch. This avoids mismatches between the available source code and the documentation.

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa file-code >}} Sphinx building with `gh-pages` from branch

```yaml
name: Sphinx documentation

on: [push, pull_request, workflow_dispatch]

permissions:
  contents: write

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install -r docs/requirements.txt
      - name: Sphinx build
        run: |
          sphinx-build docs/ docs/_build/
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        if: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
        with:
          publish_branch: gh-pages
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/
          force_orphan: true
```
:::

::: {.callout-note appearance="simple" icon="false"}
## {{< fa circle-check >}} Customizing the workflow
This example assumes you have a separate `requirements.txt` in the `/docs` folder. Update the location of the `requirements.txt` if you store the Sphinx dependencies in the root.
:::


::: {.callout-warning appearance="simple" icon="false"}
## {{< fa triangle-exclamation >}} Warning

- With the GitHub Free plan, Pages cannot be deployed from a private repository.
- GitHub Pages sites are publicly available on the internet, even if the repository for the site is private.
:::

### Workflows for building Python packages

You can automate publishing a new version of your Python package with a GitHub Action. Notice that in the workflow below, the trigger is the creation of a new release on GitHub.

::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa info-circle >}} Building a Python package

```yaml
name: Upload Python Package

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build
      - name: Build package
        run: python -m build
      - name: Publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          password: ${{ secrets.PYPI_API_TOKEN }}

```
:::

This action should only run after all other workflows (such as testing and building) have passed.


### Additional concepts

#### Variables and secrets
Secrets are variables that you create in an organization, repository, or repository environment. The secrets that you create are available to use in GitHub Actions workflows. GitHub Actions can only read a secret if you explicitly include the secret in a workflow.

⮕ More information on [using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

#### Matrix strategy

A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables. For example, you can use a matrix strategy to test your code in multiple versions of a language or on multiple operating systems.

A job will run for each possible combination of the variables. In the example below, the workflow will run 12 jobs, one for each combination of the `os` and `python-version` variables.

```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.10', '3.11', '3.12', '3.13']       
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

⮕ More information on [using a matrix for your jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).

::: {.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
If you want deterministic runner environments, specify exact versions (e.g., `macos-15`) instead of `latest`, since the `latest` aliases will migrate over time.
:::

#### Artifacts
[Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts) are files or sets of files that are produced during the execution of a workflow and need to be stored or shared between jobs in a workflow.

To upload an artifact, you typically add a step in your workflow:
```yaml
steps:
  - name: Upload build output
    uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: <path/to/build/output>

```

Artifacts can be downloaded in subsequent jobs of the same workflow run using the `actions/download-artifact` action. This is done with a step like:
```yaml
steps:
  - name: Download build output
    uses: actions/download-artifact@v4
    with:
      name: build-output
      path: <path/to/download>

```
By default, artifacts are retained for 90 days, but this can be configured per workflow or at the repository/organization level.

### Sonar

To automate checking your code quality, you can also make use of a third-party service. [SonarQube Cloud (previously known as SonarCloud)](https://docs.sonarcloud.io/) is a cloud-based code analysis service designed to detect coding issues in many different programming languages. The [free plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans/) allows you to analyze an unlimited number of **public repositories**. Private projects will not be importable on this plan.

1. Make your repository public.
1. Link your GitHub repository via their [login page](https://sonarcloud.io/login).
1. Follow the [instructions](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github/) to set up the code analysis.

You can also integrate [SonarQube Cloud code analysis in GitHub Actions](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud/). Typically, you would create a new workflow file, for example `.github/workflows/sonar.yml`, and configure triggers to your needs. You will need to set up a token in GitHub Secrets and configure what needs to be analyzed in `sonar-project.properties`. 


::: {.callout-note appearance="simple" icon="false" collapse="true"}
## {{< fa circle-check >}} Example of SonarQube Cloud GitHub Action
```
name: SonarQube Cloud Workflow
on:
  push:
    branches:
      - main
  pull_request:
      types: [opened, synchronize, reopened]

jobs:
  sonarqube:
    name: SonarQube
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  
      - name: SonarQubeScan
        uses: SonarSource/sonarqube-scan-action@v4
        env: 
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```
:::

The basic usage step-by-step is described in their [GitHub repository](https://github.com/SonarSource/sonarqube-scan-action). 

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Possible analysis parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/)
:::