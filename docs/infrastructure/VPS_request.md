---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-29

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-08-29

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Request a VPS

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
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - infrastructure
 - servers 

---

## Background
This guide describes the essentials for requesting and setting up a TU Delft managed Virtual Private Server (VPS). 

Common use cases for VPSs covered in these guides include:

* [Set up a web server](../infrastructure/web_servers.md)
* [Set up runners for TU Delft GitLab](../software/automation/gitlab/gitlab_docker.md)
* [Mounting and handling storage drives such as a *Project Drive*](../data/data_storage/project_drive_mounting.md)

## Prerequisites
* TU Delft NetID
* Basic knowledge of Linux (if requesting a Linux server)

## Tools/Software
* For Windows users, you will need a programming and runtime environment like Windows Subsystem for Linux (WSL) or an SSH client like [PuTTY](https://www.putty.org/).

## Steps
1. Navigate to the TU Delft server request form
2. Fill and send the form according to your preferences and needs
3. Receive confirmation of server deployment from TU Delft ICT 
4. Login to your server for the first time

### Step 1: Navigate to the TU Delft server request form
You can make a request for a server via the [TopDesk self service portal](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=71ba4c9678e041fd99dad8e7e11dd0e2). If the link does not work, you can also navigate to the TopDesk portal homepage and type "Faculty managed Servers" in the search box. Alternatively, you can navigate to the form via:

> ICT SERVICES -> IT FOR RESEARCH -> FACULTY MANAGED SERVERS.

### Step 2: Fill and send the form according to your preferences and needs
The form is divided into three sections: **Caller**, **General Questions**, and **Technical Questions**.

**Caller** should contain the contact information of the main administrator of this server. If you select your name, the fields below should be auto-populated with your building, phone number, email, department/program, organizational unit, and (sometimes) room. If you are requesting the server on behalf of someone else, you can fill in their details instead.

The last question in the **Caller Details** section access to the server by external users. Generally speaking, granting access to TU Delft-managed servers is not recommended, but if it is necessary you can add the contact details of the external party and the reason(s) for which they should have access. You will need to provide a company-affiliated email address for the external user, and the request may or may not be granted by ICT. 

:::{.callout-note}
Keep in mind that a server provides access to the backend of your application. If for example you want to deploy a web server to share your data widely, users **do not** need direct access to the server in order to access the data itself. 
:::

The next section contains **General Questions** about the name and purpose of your server. If you plan to use this server ongoing into the future, you can either leave the field "Expiration Date" blank or add a date in 10+ years. TU Delft ICT will alert you when the expiration date you select is nearing. There you can also add the netIDs of your collaborators who should have access to the server

The **Technical Questions** section asks you to specify an operating system and some other technical details about your server configuration. 

When requesting a VPS, users can choose from a range of predefined hardware and operating system configurations. The following operating systems are available: Windows Server 2019, Windows Server 2022, Red Hat Enterprise Linux (latest supported version), and Ubuntu (latest LTS version). If you are new to working with servers, generally the best choice may be "Basic configuration 4" (Ubuntu). 

All configurations have rather limited internal memory, so if you need more memory you can always [mounting additional storage drive(s) such as a Project Drive](../data/data_storage/project_drive_mounting.md). If additional processing capacity is needed, it can be requested via the 'ICT malfunction' or 'Request ICT service' forms in TOPdesk. This includes options such as increasing the number of processors, cores per processor, RAM, or disk storage. It may also reveal a reason to consider a physical server instead of a VPS.

The next question deals with opening ports to the server through the TU Delft firewall. Ports are essentially gateways to the server that are specific to different purposes. For example, port 80 is opened to handle HTTP requests, port 20 is opened to handle SSH requests, port 3306 is opened to allow access to a MySQL database, and port 443 is opened to handle HTTPS requests. If you are planning to use your VPS as a webserver, ports 80 and 443 should be open. You can use this space to ask ICT to do so. 

The next section, FQDN, is the way you can refer to your server on the internet. The recommendation is a format like `<servername>.<facultyabbreviation>.tudelt.nl`. In general, it's best to keep names relatively short and informative to make it easy to reference and remember.

You should also be sure to check the instructions in the form and contact your faculty [Data Steward](https://www.tudelft.nl/en/library/current-topics/research-data-management/r/support/data-stewardship/contact/) or [Faculty IT Manager](https://intranet.tudelft.nl/en/-/faculty-it-manager) if you need further explanation.

## Initial Configuration of your VPS
A few days after submitting the request, you will receive an email from ICT with login details. You can connect to your VPS via ssh (secure shell) using a command line interface (CLI). If you are in a windows environment, it is recommended to install WSL or [PuTTY](https://www.putty.org/) to be able to use the ssh command in a CLI. The unix based systems (e.g., mac, ubunt) contain ssh by default in their "Terminal" application. In order to login to your VPS, you need to first ssh to the bastion server with `ssh <username>@linux-bastion-ex.tudelft.nl` and then from there login to your server `ssh <servername>`. The first thing we recommend to do after logging into the server is to update the pre-installed packages:

::: {.panel-tabset}

### Debian (Ubuntu)

```
sudo apt-get update && sudo apt-get upgrade
```

### RedHat

```
sudo yum update
```

:::

It would be also useful to set a password for the VPS when you log in. You can do that by `passwd` command. 

## Next Steps

* [Set up a web server](../infrastructure/web_servers.md)
* [Set up runners for the TU Delft Gitlab](../software/automation/gitlab/gitlab_docker.md)
* [Mounting and handling storage drives such as a Project Drive](../data/data_storage/project_drive_mounting.md)

We will add more documentation when other common cases come to our attention, so please [reach out to us](../../CONTRIBUTING.md) with your questions or suggestions.