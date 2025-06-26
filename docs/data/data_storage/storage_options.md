---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-06-25

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Storage options

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Data storage options at TU Delft
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Raul Ortiz Merino
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Raul Ortiz Merino
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Raul Ortiz Merino

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - data
 - storage

---

Storing your data in a secure location is a key element of a successful project with a data component. As a TU Delft researcher, you have several options. Below you can find an overview of the available storage options, depending on whether they are local, networked, or cloud-based, how secure they are, whether they can be shared with internal or external partners, and whether they are automatically backed up or not. Please visit the sections on [Data Security](../data_storage/security.md), [Data Sharing](../data_storage/sharing.md) and [Data Backup](../data_storage/backup.md) for more information on these topics.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Options listed in this guide refer to research data in its *active* phase. For long-term preservations, please refer to the [Archive and Publish](../data_publishing/archival_publishing_index.md) section.
:::

## Overview of storage options

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Important
These options have been curated from:

- The intranet section on [Data Storage](https://intranet.tudelft.nl/-/data-storage-1)
- The [topdesk](https://tudelft.topdesk.net/) "Overview of data storage and file sharing" (Home > ICT services > IT for Research > Overview of data storage and file sharing)
- And the [Storage Finder](https://storagefinder.tudelft.nl/) tool
- [SURF](https://www.surf.nl/en/)

Please note that the information is subject to change, and you should always refer to the official TU Delft documentation for the most up-to-date information.
:::

| Storage Option                      | Location         | Security | Sharing                        | Backup                                               | Size                        | Aditional info                                                                                                      |
| :---------------------------------: | :--------------: | :------: | :----------------------------: | :--------------------------------------------------: | :-------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| Private laptop                      | Local            | Low      | Defined by owner               | Defined by owner                                     | Check device specifications | Security listed as low as the device is prone to loss and theft, among other incidents                              |
| Private desktop                     | Local            | Medium   | Defined by owner               | Defined by owner                                     | Check device specifications | Same as above, perhaps more secure than a laptop as it is not necessarily mobile                                    |
| TU Delft managed laptop             | TU Delft network | Medium   | Internal to TU Delft           | Defined by owner (unless using options listed below) | Check device specifications | All TU Delft managed devices are password protected. Security is therefore slightly higer than private counterparts |
| TU Delft managed desktop            | TU Delft network | Medium   | Internal to TU Delft           | Defined by owner (unless using options listed below) | Check device specifications | All TU Delft managed devices are password protected. Security is therefore slightly higer than private counterparts |
| TU Delft Personal Data Storage (H:) | TU Delft network | High     | Internal to TU Delft           | Yes                                                  | 8 GB                        | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| TU Delft Group Data Storage (M:)    | TU Delft network | High     | Internal to TU Delft           | Yes                                                  | 50 GB                       | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| TU Delft Project Data Storage (U:)  | TU Delft network | High     | Internal to TU Delft           | Yes                                                  | > 250 GB                     | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| Microsoft Teams                     | Cloud            | High     | Internal to TU Delft           | Yes                                                  | < 250GB                     | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| Microsoft Sharepoint                | Cloud            | High     | Internal to TU Delft           | Yes                                                  | < 250GB                     | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| Microsoft OneDrive for Business     | Cloud            | High     | External access can be enabled | Yes                                                  | 1 TB                        | [Storage Finder](https://storagefinder.tudelft.nl/)                                                                 |
| SURF drive                          | Cloud            | High     | External access can be enabled | Yes                                                  | 500 GB                      | [SURF drive documentation](https://www.surf.nl/en/services/storage-data-management/surfdrive)                       |

## Project Drive operations

A Project Drive is a TU Delft managed network drive that allows you to store and share data with your project team members. It is a secure and reliable option for storing research data, and it is automatically backed up. Below you can see how to request a Project Drive, and how to mount it on a server (please refer to the section on [Remote Servers](../../infrastructure/intro_servers.md) for more details).

::: {.content-block}
::: {.features}

::: {.feature}
### {{< fa hard-drive >}} Request Project Drive space

::: {.learn-more}
[Learn more »](./project_drive_request.md)
:::
:::

::: {.feature}
### {{< fa server >}} Mount Project Drive on server

::: {.learn-more}
[Learn more »](./project_drive_mounting.md)
:::
:::

<!--

::: {.feature}
### {{< fa rotate >}} Sync Project Drive and SURFDrive with Unison

Update coming soon! 🛠️

::: {.learn-more}
[Learn more »](./sync_unison.md)
:::
:::

:::
:::

## Cloud

Coming soon!


-->