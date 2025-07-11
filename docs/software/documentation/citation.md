---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2024-11-14

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-07-11

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: CITATION.cff

# Short description of the document, will be used in the listing
description: How to cite software
hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Elviss Dvinskis
author_2: Maurits Kok

# Maintainers of the document, will not be parsed [manual entry]
#maintainer_1:
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
categories: 
 - documentation
 - software
 - FAIR

---

It's straightforward to cite research papers, but with software sometimes it's not as obvious. It is recommended to place a `CITATION.cff` file in the root of your repository to inform others about the preferred way to cite the software. GitHub can automatically parse the `.cff` file to create citation snippets in APA or BibTeX format. If you'd prefer the software to be cited through a journal publication, you can mention this in the README and in the `CITATION.cff` file.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
### {{< fa lightbulb >}} An example of a `CITATION.cff`

```
cff-version: 1.2.0
message: "If you are using this software, please cite it as shown below."
authors:
- family-names: "Doe"
  given-names: "Jane"
  orcid: "https://orcid.org/9999-9999-9999-9999"
title: "Name of your software"
version: 1.0.1
doi: "11.1111/11111"
date-released: 2024-12-31
license: MIT
url: "https://github.com/your_repo"
```
:::

When citing a paper that is linked to the software you can use `preferred-citation` argument.

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
### {{< fa lightbulb >}} An example of a `CITATION` file citing a research article

```
cff-version: 1.2.0
message: "If you are using this software, please cite it as shown below."
authors:
- family-names: "Doe"
  given-names: "Jane"
  orcid: "https://orcid.org/9999-9999-9999-9999"
title: "Name of your software"
version: 1.0.1
doi: "11.1111/11111"
date-released: 2024-12-31
license: MIT
url: "https://github.com/your_repo"
preferred-citation:
    type: article
    authors:
    - family-names: "Doe"
      given-names: "Jane"
      orcid: "https://orcid.org/9999-9999-9999-9999"
    doi: "11.1111/11111"
    journal: "The title of the journal"
    month: 12
    start: 19 # the first page number
    end: 29 #the last page number
    title: "Name of your submitted paper"
    issue: 9
    volume: 2
    year: 2024
    
```
:::

:::{.callout-tip appearance="simple" icon="false" collapse="true"}
### {{< fa lightbulb >}} How the citation would look on GitHub
On GitHub, it will show in either APA or BibTeX formatting, as they are the currently supported formats. If you add a `CITATION.cff` file to your repository, then a label for citing will automatically be generated and will show up on the right sidebar of the repository.

**APA**

> Doe, J. (2024). Name of your software (Version 1.0.1) [Computer software]. https://doi.org/11.1111/11111

**BibTeX**

> @software{Joe_Name_of_your_software_2024,
      author = {Doe, Jane},
      doi = {11.1111/11111},
      month = {12},
      title = {{Name of your software}},
      url = {https://github.com/your_repo},
      version = {1.0.1},
      year = {2024}
}

This is an example of software citation.  
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [CITATION.cff documentation](https://citation-file-format.github.io)
- [GitHub documentation on CITATION files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) - this resource also includes how to cite something other than software or a journal article.
- [Generate CITATION.cff files](https://citation-file-format.github.io/cff-initializer-javascript/#/)
- [Citation File Format GitHub](https://github.com/citation-file-format/citation-file-format)
:::
