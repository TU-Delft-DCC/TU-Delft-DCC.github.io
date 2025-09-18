---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-01-31

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
title: Online services

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Overview of code quality and security tools and practices
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
categories: 
  - Software
  - Code Quality
  - Code Coverage
---

### Sonar
[Sonar](https://www.sonarsource.com/products/sonarcloud/) is a cloud-based service that provides inspection of code quality to perform automatic reviews with static code analysis to detect bugs, code smells and security vulnerabilities in a project. It supports many programming languages and integrates with GitHub (and GitLab and Bitbucket) as part of the Continuous Integration workflows. Sonar is particularly useful for projects that require compliance with coding standards or need regular feedback on the quality of the code. 

{{< fa arrow-right >}} [Learn more: SonarQube Cloud documentation](https://docs.sonarsource.com/sonarqube-cloud/)

::: {.callout-tip appearance="simple"}
## Consideration
While Sonar offers valuable features for code quality analysis, be aware that for **non open-source projects it is a paid service**, and pricing model depends on how many lines of code you want to check.
:::

### GitHub CodeQL
GitHub CodeQL is a semantic code analysis engine that allows you to write queries to find security vulnerabilities in your codebase. It is particularly useful for identifying security vulnerabilities in open-source projects, and it can be integrated into your GitHub Actions workflow to automatically scan your code for vulnerabilities. CodeQL is available for a variety of programming languages, and it can help you identify and fix security issues before they become a problem.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa link >}} Learn more
- [GitHub CodeQL](https://securitylab.github.com/tools/codeql)
- [Introduction to code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)
:::

### Code coverage
Code coverage quantifies the proportion of source code that is run by a software program’s (unit) test suite. It helps to identify which parts of the codebase have been tested, and achieving a high code coverage generally indicates a lower likelihood of hidden bugs. However, it is important to note that high code coverage does not necessarily translate to high code quality - it simply tells us how much of the codebase is being tested.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa link >}} Learn more
- [Sonar - Test coverage](https://docs.sonarsource.com/sonarcloud/enriching/test-coverage/overview/)
- [Codecov - Test coverage](https://about.codecov.io/)
:::

### Dependabot
Dependabot is a GitHub app that helps you keep your dependencies up to date. It checks for outdated dependencies in your project and automatically creates pull requests to update them. This can help you stay on top of security vulnerabilities and ensure that your project is using the latest features and bug fixes.

{{< fa arrow-right >}} [Enabling Dependabot for your repository](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository)

### OpenSSF
The Open Source Security Foundation (OpenSSF) Best Practices badge provides a way for Free/Libre and Open Source Software (FLOSS) projects to demonstrate their adherence to best practices. Projects can choose to self-certify for free. Inspired by the numerous badges available on GitHub, the OpenSSF Best Practices Badge allows to quickly identify which FLOSS projects are committed to best practices and are therefore more likely to deliver high-quality and secure software.

The criteria for earning the passing badge and additional details about the OpenSSF Best Practices Badging program can be found on GitHub.

::: {.callout-note appearance="simple" icon="false"}
## {{< fa link >}} Learn more
- [OpenSSF - Best Practices](https://www.bestpractices.dev/en)
- [GitHub - Best Practices Badge](https://github.com/coreinfrastructure/best-practices-badge)
:::