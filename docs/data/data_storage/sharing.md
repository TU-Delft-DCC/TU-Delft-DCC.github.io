---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-07-01

# We use this key to indicate the last modified date [manual entry]
date-modified: 2025-07-09

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Data sharing

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

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
 - Data
 - Storage
 - Data Sharing
---

This section covers aspects of data sharing, for *ongoing work*, throughout the *active* phase of a research project. The use of data repositories, the importance of data licenses, and the significance of metadata in sharing *completed work* are discussed in the section on [Archiving and publishing data](../data_publishing/archival_publishing_index.md).

Both sections are closely related, as data sharing is a key component of the broader data management lifecycle. As such, these sections include shared concepts of [security](../data_storage/security.md) and [privacy](../planning/privacy.md) also covered in sections of their own.

As shown in the [overview of storage options](../data_storage/storage_options.md#overview-of-storage-options) section, TU Delft provides several options for data storage, which can be used to share data with internal and external partners. The choice of storage solution depends on the nature of the data, the level of security required, and the intended audience for the shared data.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
Storing research data only on your personal laptop or desktop is discouraged. Devices can be lost, stolen, or damaged, leading to data loss. Additionally, local storage often lacks sufficient backup, access control, and security measures required for research data.
:::

## TU Delft internal 

### Networked storage

#### **Personal Data Storage (H:)**

This is the default storage location for personal data, such as documents, spreadsheets, and presentations. It is accessible only to the user and is not suitable for sharing with others. However, it enables *you* to share *your* data across TU Delft-managed devices connected to the TU Delft network.

#### **Group Data Storage (M:)**

The folder structure on this network drive follows a similar structure to that of the faculties, departments, and research groups at TU Delft. It is typically accessible to members of a research group and can be used to share data with colleagues within the same department and faculty. Access to this storage is managed by your department secretary and/or the Faculty ICT Manager.

#### **Project Data Storage (U:)**

Access to this storage is requested by a contact person "caller/owner" which can in turn provide access via a NetID. Its data can be accessed through CIFS and NFS (with kerberos authentication), meaning it can be mounted in different systems. Please visit the [project drive request](../data_storage/project_drive_request.md) and [project drive mounting ](../data_storage/project_drive_mounting.md) sections for more information.

### Cloud-based storage

Cloud services are not recommended as primary storage locations for research data. A critical drawback is that access to data stored on these platforms can be lost upon the creator's departure from TU Delft, posing a significant risk to data continuity and ownership. Furthermore, they "should not be used for highly confidential data such as state secrets, sensitive personal data or highly sensitive IP material".

TU Delft provides a few collaboration tools through the Microsoft Office 365 platform, including Microsoft Teams, SharePoint and OneDrive. 

#### **Microsoft Teams**

This platform is primarily used for communication and collaboration within research groups and projects. It allows for file sharing, real-time collaboration, and integration with other Microsoft 365 applications. However, it is not a dedicated data storage solution and should be used in conjunction with other storage options.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Find more details on [TopDesk](https://tudelft.topdesk.net/) Home ⇾ ICT services ⇾ Collaboration Tools ⇾ Microsoft Teams.
:::

#### **Microsoft SharePoint**

Considerations for this platform are similar to those for Microsoft Teams. It is primarily used for document management and collaboration within research groups and projects. SharePoint allows for file sharing, version control, and integration with other Microsoft 365 applications.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Find more details on [TopDesk](https://tudelft.topdesk.net/) Home ⇾ ICT services ⇾ Collaboration Tools ⇾ SharePoint 2016 support
:::

## External

#### **Microsoft OneDrive for Business**

OneDrive is installed by default on the laptops and desktops supplied by TU Delft. TU Delft OneDrive is recognisable by the name: "OneDrive - Delft University of Technology". Web based access within and outside TUDelft, sharing and working together is possible with TU Delft colleagues and also external users. OneDrive is suitable for sharing data with external partners, as it allows for controlled access and collaboration. However, it is important to ensure that sensitive data is not shared without proper security measures in place.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Find more details on [TopDesk](https://tudelft.topdesk.net/) Home ⇾ OneDrive for Business
:::

#### **SURFdrive**

SURFdrive is a personal cloud storage service for the Dutch education and research community, offering staff, researchers and students an easy way to store, synchronise and share files in the secure and reliable SURF community cloud. SURFdrive offers staff, researchers and students an easy way to share and synchronise files within a secure community cloud with ample storage capacity.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Find more details on [SURFdrive](https://www.surf.nl/en/surfdrive).
:::