---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-26

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-08-26

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Accessing and requesting *Project Data Storage* space

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Ashley Cryan
author_2: Raúl Ortiz Merino
author_3: Elviss Dvinskis

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Raúl Ortiz Merino
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Raúl Ortiz Merino

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - data
 - storage

---

## Accessing the *Project Data Storage (U:)* drive 

TU Delft network drives are automatically mounted on TU Delft-managed computers (running Windows) when connected to the TU Delft network (dastud, [eduVPN](https://intranet.tudelft.nl/en/-/openvpn?p_l_back_url=%2Fen%2Fgroup%2Fguest%2Fsearch%3Fq%3Dvpn&p_l_back_url_title=Search)).

On macOS and Linux, there are a few additional steps needed to access *Project Drives*. The instructions can be found [here](https://filelist.tudelft.nl/Calendar/2024/08%20August/Project%20storage%20instructions.pdf). *(Last updated: August 2024)*

It can also be accessed through [webdata.tudelft.nl](https://webdata.tudelft.nl/) using a WebDAV web link [staff-umbrella](https://webdata.tudelft.nl/staff-umbrella). To mount on a TU Delft Virtual Private Server, first follow the instructions [here](/docs/infrastructure/VPS_request.md), and then the instructions in the next guide [Mount *Project Drive* on server](project_drive_mounting.md).

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Reminder

If you are accessing the *Project Data Storage (U:)* drive from outside the TU Delft network (e.g., from home), you need to connect to eduVPN beforehand.
:::

## Requesting *Project Data Storage (U:)* space

### Prerequisites
* TU Delft NetID
* (Optional) A list of TU Delft collaborators who should have read/write access to it

### Steps
1. Request the storage via the TU Delft ICT form on TopDesk.
2. Fill out and send the form according to your data storage preferences and requirements.
3. Access your data storage.

#### **Step 1. Request storage via the TU Delft ICT form on TopDesk**
You can make a request for data storage via a form available on the [TopDesk self-service portal](https://tudelft.topdesk.net/) (requires NetID sign-in); navigate to:

> HOME ⇾ ICT SERVICES ⇾ IT WORKSPACE ⇾ DATA STORAGE ⇾ PROJECT DATA STORAGE - APPLICATION FORM

#### **Step 2. Fill out and send the form according to your data storage preferences and requirements**
The form has six main sections: "_**Caller**_", "_**Application**_", "_**Access for third parties**_", "_**Storage type**_", "_**Storage Requirements**_", and "_**Backup Retention**_".

The _**Caller**_ section should be auto-populated with your name, building, phone number (if you have a work phone number), email, department/program, organizational unit, and (sometimes) room. You will then be considered as main administrator of this server.  

In the next part, _**Application**_, you can input:

1. (Short) **Description of the research project** for which you are requesting the storage. This will help ICT to understand your needs and provide you with the best possible service.
2. A **proposed name for the Project Data Storage**. This name will be used as the folder name for your storage (e.g., U:/your_project_name). Even if not required, we strongly advise to keep it as short as possible, yet descriptive, and without spaces or special characters. For example, use underscores ( _ ) or hyphens ( - ) to separate words, or use CamelCase (dividing words using capital letters).
3. **Who should have access**. Here you can add the full name, NetID, and email address of your collaborators and which type of access they should have (read or write). You can always add or remove users later by contacting the ICT Servicedesk. You can also choose to have no other users with access apart from yourself. If you have a few collaborators, you can also add their details using an attachment file using the box below.

In _**Access for third parties**_, you can indicate if you want to allow external users (i.e., non-TU Delft users) to access the data. If you choose "Yes", you will need to provide the names and email addresses of the external users in the text box below (referred in step 3 above, only difference is the lack of NetID for external users).

_**Storage type**_ allows you to ask for high availability. This choice depends on your I/O (Input/Output) operations. For example, large/long simulations, and real time data processing may require high availability, especially if you mount it to a server as described in the section [Mount *Project Drive* on server](../data_storage/project_drive_mounting.md). If you are unsure about the availability needed, contact your faculty Data Steward for advice before submitting you application. 

_**Storage Requirements**_ allows you to specify the amount of storage you need. The minimum (upper limit) is 250 GB, and the maximum is 5 TB. If you need 5 TB or more, your request will be forwarded to the Faculty IT Manager (FIM) for further review.

Finally, in _**Backup Retention**_, you can choose how long you want your data to be backed up. For the default option, a backup is made on a daily basis and is stored for two weeks. This means a data loss of a maximum of one day can occur. After two weeks, a back-up is made every week and saved for a year. This means a data loss of maximum one day can occur. An extended option is also available to keep data stored from 53 weeks.

#### **Step 3. Access your data storage**

After submitting the request, you will receive a response from ICT. Once approval is granted, you can access your *Project Data Storage* as described [above](#accessing-the-project-data-storage-u-drive).