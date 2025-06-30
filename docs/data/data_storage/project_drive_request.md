---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-06-30

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Request Project Drive space

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Ashley Cryan
author_2: Raúl Ortiz Merino

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

## Background
TU Delft offers several options for researchers to store their data. One of the most commonly recommended options is the Project Drive (Project Data, U:) for its  storage capacity and secure backups from the University. 

## What this documentation will help achieve
This documentation will walk through the steps needed to request Project Drive storage from TU Delft ICT. 

This storage is automatically mounted on TU Delft managed computers when connected to the TU Delft network (dastud, [eduVPN](https://intranet.tudelft.nl/en/-/openvpn?p_l_back_url=%2Fen%2Fgroup%2Fguest%2Fsearch%3Fq%3Dvpn&p_l_back_url_title=Search)). It can also be accessed through [webdata.tudelft.nl](https://webdata.tudelft.nl/) using a WebDAV protocol, through a client like [WebDrive](https://webdata.tudelft.nl/) on your local machine (click on the link and then the WebDrive heading to download and install this software for your operating system), or mounted to a TU Delft Virtual Private Server following the instructions [here](/docs/infrastructure/VPS_request.md). 

## Prerequisites
* TU Delft netID
* (Optional) A list of TU Delft collaborators who should have read/write access to the Project Drive storage space you are requesting 

## Tools/Software
* (Optional) [WebDrive](https://webdata.tudelft.nl/)
* (Optional) [eduVPN](https://intranet.tudelft.nl/en/-/openvpn?p_l_back_url=%2Fen%2Fgroup%2Fguest%2Fsearch%3Fq%3Dvpn&p_l_back_url_title=Search) (link to intranet page, requires netID sign in)

## Steps
1. Request Project Drive storage via the TU Delft ICT form on TopDesk
2. Fill and send the form according to your data storage preferences and requirements
3. Access your data storage on Project Drive

### Step 1. Request Project Drive storage via the TU Delft ICT form on TopDesk
You can make a request for data storage via a form available on the [TopDesk self service portal](https://tudelft.topdesk.net/) (requires netID sign in). Home  > ICT services > IT for Research  > Data storage for Research: Project data (U:) >  ICT: Request Research Data Storage.

### Step 2. Fill and send the form according to your data storage preferences and requirements
The form is divided into three sections: "Caller", "Information about Requester and Data", and "Data for a Research Project".

The **Caller** section should contain the contact information of the main administrator of this server. If you select your name, the fields below should be auto-populated with your building, phone number, email, department/program, organizational unit, and (sometimes) room.

<img width="547" alt="blurred3" src="https://user-images.githubusercontent.com/70349945/124717195-2e53b380-df05-11eb-914f-0f451a427e73.png">

________

In the next part you choose your preferences about data preservation. The first question asks whether you are setting up new storage on the Project Drive, or want to change existing storage. The next question is about the availability - see below for more information. The usual choice here is "Standard".

![](https://user-images.githubusercontent.com/70349945/124719093-12511180-df07-11eb-894b-827ca86613fd.png)

For the next question, you need to determine if your data is critical, sensitive, or standard, using these criteria:

![](https://user-images.githubusercontent.com/70349945/124718801-c4d4a480-df06-11eb-9e48-5579640ba2a9.png)

There are two options for backup retention: standard and high. Data are backed up by ICT on a daily basis, so the retention time refers to the period for which these backups are stored. The standard option refers to 14 days of retention while in the other one the retention period is one year. In other words, if the retention time is set to 14 days (Standard) and you delete a file, you can restore it within those two weeks. If retention time is 1 year (High), you can restore it anytime within the year. For most situations, a Standard backup retention time is suitable.

________

In the final section, you need to provide some information about your research project. Depending on your research needs, you should specify how much space you will need on the Project Drive to hold all your data, initially and into the planned future. It is important to know that the Project Drive storage is able to expand as your data grows, but you should make your best guess when requesting the space. 

At the bottom of this section you can attach an Excel file that contains the netIDs of TU Delft affiliated employees that should have read/write access to the storage you are requesting on the Project Drive.  

