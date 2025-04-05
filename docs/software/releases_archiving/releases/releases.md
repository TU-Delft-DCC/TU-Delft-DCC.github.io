---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-04-04

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Releases

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
 - package
 - release
 - r
 - python

---

Once you have your software packaged, you can release it to platforms like PyPI or CRAN. While your software might be already publicly available on GitHub, releasing it to a package repository allows easy access and installation for users. The most common platforms for releasing software packages are PyPI for Python packages and CRAN for R packages.

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa box >}} Release your Python package
Publish your Python package on PyPI.

::: {.learn-more}
[Learn more »](./releases_pypi.md)
:::
:::

::: {.feature}
### {{< fa box >}} Release your R package
Publish your R package on CRAN.

::: {.learn-more}
[Learn more »](./releases_cran.md)
:::
:::

:::
:::

## Changelog

Maintaining a changelog provides a clear history of changes made to your software and version information. It helps users and developers understand what has changed between versions, what modifications, fixes, and enhancements have been made. 

- [How do I make a good changelog?](https://keepachangelog.com/en/1.1.0/)
- [Example from eScience Center](https://github.com/matchms/matchms/blob/master/CHANGELOG.md)

## Semantic versioning

[Semantic Versioning](https://semver.org) (SemVer) is a versioning scheme that reflects changes in your software systematically. It consists of three numbers: major, minor, and patch (e.g., 1.9.1).

- **Major version** increments are meant for significant changes that may make backward-incompatible changes.
- **Minor version** increments add functionality in a backward-compatible manner.
- **Patch version** increments are for backward-compatible bug fixes only.

Adopting this practice helps both users and developers anticipate the impact of updating the software. It clearly communicates the nature of the changes.

## Release notification

After a release, it is important to communicate what has changed. Release notes are detailed descriptions of the new changes, fixes, and sometimes known issues. They are usually published alongside the changelog in repositories. You could use [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), it is a feature that allows you to present your software, along with the corresponding source code, changelog, and release notes.

It is typical for a release on PyPI or CRAN to mirror what was put under a GitHub release. This is not a requirement, but it is a good practice to keep the information consistent across platforms.

### Automatically generated release notes
GitHub provides a useful feature to [automatically generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) for new versions of your software. It scans the commits between your releases and compiles a summary of the changes, fixes, and enhancements made. This can not only save time but also help to avoid undocumenting changes.

How to enable automatic release notes:

1. Go to your repository on GitHub and navigate to the releases section.
2. Draft a new release. When you select a tag, GitHub will offer an option to auto-generate the release notes based on the commits since the last release.
3. Customize the release notes. You can edit the auto-generated content to add more details or format it according to your preferences.
4. When publishing, the release notes will be attached to your release.

This feature is particularly helpful for maintaining accurate and up-to-date release documentation.