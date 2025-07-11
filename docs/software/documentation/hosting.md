---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2025-02-24

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Hosting

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
#categories: 
# - documentation
# 

---

Once you have created your documentation either in Sphinx, Jupyter Book, MkDocs or Quarto, you can host it online.

### GitHub Pages
GitHub Pages provides a simple way to host your documentation, especially if your project is already on GitHub. 

It is straightforward to set up GitHub Pages:

1. Within your repository, go to the repository settings and find the GitHub Pages section.
2. Choose your publishing source (you should have a docs folder or a dedicated branch).

GitHub Pages also supports custom domains, which might be relevant to you. You can configure this by adding a `CNAME` file to your directory.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [GitHub Pages](https://pages.github.com)
- [Configuring a custom domain for your GitHub Pages site]( https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Coderefinery - Deploying Sphinx documentation to GitHub Pages](https://coderefinery.github.io/documentation/gh_workflow/)
- [ Coderefinery - Hosting websites/homepages on GitHub Pages](https://coderefinery.github.io/documentation/gh-pages/)
:::

### Read the Docs
[Read the Docs]( https://readthedocs.org/) is a platform that simplifies the hosting of documentation. It integrates particularly well with Sphinx, allowing for the automatic building and hosting of your project documentation. Read the Docs supports automatic builds and version control, enabling users to switch between different versions of the documentation to match the version of the software they are using. Additionally, it offers support for custom domains. 

It offers a free service for open-source projects, which includes features like version control and automatic builds. However, for private or *commercial* projects, Read the Docs requires a paid subscription.

The setup is also straightforward:

1. Sign up and import your documentation repository.
1. Connect to your GitHub account.
1. Configure your project settings within their dashboard.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Read the Docs: documentation simplified](https://docs.readthedocs.io/en/stable/)
- [Read the Docs tutorial](https://docs.readthedocs.io/en/stable/tutorial/index.html)
:::