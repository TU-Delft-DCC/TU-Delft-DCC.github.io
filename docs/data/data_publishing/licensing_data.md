---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-05-05

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Data licensing

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
author_2: Selin Kubilay

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
 - licenses

---

When depositing data, selecting an appropriate license cannot be overlooked, as it defines the permissions and restrictions for others using your data. Clear labelling of licensing terms ensures that data can be shared and reused legally and ethically. 

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Important
- If your data includes accompanying software (or vice versa), it is important to license the software separately to clearly define its usage rights distinct from the data! For more information, refer to our [Software Licenses](../../software/documentation/license.md) guide.
- For guidance on selecting appropriate data licenses, consult your faculty [data steward](https://www.tudelft.nl/library/research-data-management/r/support/data-stewardship/contact). 
- For more detailed information on data licenses, please visit the [4TU.ResearchData Licensing Guide](https://data.4tu.nl/info/en/use/publish-cite/upload-your-data-in-our-data-repository/licencing) or read on [Data Licenses](https://book.the-turing-way.org/reproducible-research/licensing/licensing-data) in The Turing Way book. You can also use [Creative Commons License Chooser](https://creativecommons.org/chooser/) to help you select a data license. 
:::

Similarly to software licenses, data licenses can be divided depending on their restrictiveness. The most common licenses are *Creative Commons* (CC) licenses, which are widely used for data and other creative works. These licenses can be categorized into permissive and restrictive types.

## CC licenses

Permissive licenses allow for broad reuse with minimal restrictions, while restrictive licenses impose limitations on how the data can be used. CC licenses are further divided into the following categories:

- **Public Domain (CC0):** No restrictions, data can be used for any purpose.
- **Attribution (CC-BY):** Requires attribution to the original creator, allows for sharing and adaptation with appropriate citations.
- **Attribution-ShareAlike (CC-BY-SA):** Requires attribution and allows for derivatives under the same license.
- **Non-Commercial (CC-BY-NC):** Allows use for non-commercial purposes only.
- **No Derivatives (CC-BY-ND):** No derivatives allowed.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Creative Commons Licenses](https://creativecommons.org/share-your-work/cclicenses/)
:::

## Other data licenses

In addition to CC licenses, Open Data Commons provides a set of licenses that are specifically designed for data. These licenses are similar to CC licenses but are tailored for data and databases. 

- **Public Domain Dedication and License (PDDL):** Similar to CC0, it allows for unrestricted use of the data.
- **Open Data Commons Attribution License (ODC-BY):** Requires attribution to the original creator, allows for sharing and adaptation with appropriate citations.
- **Open Data Commons Open Database License (ODbL):** Allows for sharing, modification, and use of the database, but requires attribution and share-alike for derivatives. Similar to CC-BY-SA, but specifically designed for databases.
- **Restrictive Licenses:** Limits usage, often prohibiting commercial use or modifications.

While Creative Commons and Open Data Commons license might seem similar, the difference between them is that CC licenses are more general and can be applied to any type of work, while Open Data Commons licenses are specifically designed for data and databases and therefore cover different rights.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Turing Way - Data Licenses](https://book.the-turing-way.org/reproducible-research/licensing/licensing-data)
:::