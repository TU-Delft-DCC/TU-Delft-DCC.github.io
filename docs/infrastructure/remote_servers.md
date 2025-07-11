---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2024-12-07

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
title: Servers

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: Name Surname
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Yasel Quintero
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Yasel Quintero

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
 - servers
 - infrastructure

---

TU Delft offers its employees the use of physical or virtual servers. These servers are known as Faculty Managed Servers and can be requested to conduct work related to a specific project within a Faculty. 

:::{.callout-note}
It is not possible to use the servers to set up services that are already provided by the ICT department.
:::

**Virtual vs Physical Servers**

There is a choice between virtual and physical servers. Virtual servers are provided free of charge and can be requested via TOPdesk. Physical servers can be requested by contacting the Faculty's IT Manager and any associated costs are paid by the purchasing department.

In most cases, a virtual server is the most suitable option. However, a physical server may be necessary when it is intended for use as a GPU or computing cluster.

**Server Configuration**

When requesting a virtual server, users can choose from a range of predefined hardware and operating system configurations. The following operating systems are available: Windows Server 2019, Windows Server 2022, Red Hat Enterprise Linux (latest supported version), and Ubuntu (latest LTS version).

If additional capacity is needed, it can be requested via the 'ICT malfunction' or 'request ICT service' forms in TOPdesk. This includes options such as increasing the number of processors, cores per processor, RAM, or disk storage.

Some considerations:

* ICT provides the server, operating system, and network access. 
* Users are granted administrator privileges, allowing them to install any required software, provided it complies with the conditions specified in the request form.
* Access can be granted to both TU Delft members and external users.
* ICT provides daily backups, restoration services, and virus scanning for Windows servers.
* ICT ensures that the server operating system remains up to date (e.g. security patches), except for Linux systems.

::: {.callout-tip}
Detailed information on managing the server, including network and firewall settings, is provided at the bottom of the TOPdesk application form.
:::

**Example Use Cases** 

- Performing computational or data processing tasks that require a dedicated server environment.
- Running an instance of a service or application, such as ABAQUS, COMSOL or other specialized tools for a lab or research group.
- Hosting a static website, a web application, or an API for a project.
- Hosting databases, such as MySQL, PostgreSQL, MongoDB or other database management systems.
- Deploying and managing TU Delft GitLab runners for CI/CD pipelines.

**Relevant links**  

- [Intranet page](https://intranet.tudelft.nl/en/-/hosting-servers?p_l_back_url=%2Fen%2Fgroup%2Fguest%2Fsearch%3Fq%3Dvirtual%2Bprivate%2Bserver) for faculty managed servers
- [TOPdesk form](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34&openedFromService=true) to request a new virtual server
- [Intranet page](https://intranet.tudelft.nl/-/faculty-it-manager) for Faculty IT Managers.