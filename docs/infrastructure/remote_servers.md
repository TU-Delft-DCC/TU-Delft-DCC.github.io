---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-29

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-12-02

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Remote Servers

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
maintainer_1: Raúl Ortiz Merino
maintainer_2: Yasel Quintero

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Raúl Ortiz Merino

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - Infrastructure
 - Servers

---

A *server* is a computer that handles *requests* (data, services, or programs) from other computers, known as *clients*, over a network. Servers are often a critical component of architectural solutions for data management and software deployment. There are many reasons why you as a researcher may need to use a server, for example:

* You need a machine to handle large amounts of requests 
* You want to outsource the maintenance of a server to TU Delft ICT
* You would like to rely on safety and security administrated by the university, including backups
* A part of your analysis should be running continuously, and cannot do it with your own machine 

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
It is not recommended to use servers to set up services that are already provided by the ICT department. When in doubt, you can always contact your Faculty ICT Manager (FIM) and/or Faculty Data Steward.
:::

#### **Virtual vs physical servers**

All servers are a physical computer sitting somewhere. However, there is a common distiction between virtual and physical servers, where a virtual server is an independent instance provided by a larger physical server. Virtual servers are provided free of charge and can be requested via TOPdesk. Physical server placement can be requested by contacting the faculty's IT manager, and any associated costs are paid by the purchasing researcher and/or department.

In most cases, a virtual server is the most suitable option. However, a physical server may be necessary when it is intended for specific use cases (e.g., laboratory equipment, sensor data acquisition, image processing).

TU Delft offers its employees the use of physical or virtual servers, these servers are referred as faculty managed servers which are therefore *private* to the university network by default. *Virtual Private Servers* (VPS) can be requested as described in the next guide [*Request a VPS*](vps_request.md), whereas physical server placement follow a different procedure for which we strongly encourage you to consult your FIM.

#### **Relevant considerations**

Having a Faculty Managed Server (either virtual or physical) can poise several advantages:

* ICT provides the server, operating system, and network access. 
* ICT provides daily backups, restoration services, and virus scanning for Windows servers.
* ICT ensures that the server operating system remains up to date (e.g., security patches), except for Linux systems.
* Access can be granted to both TU Delft members and external users.
* Users are granted administrator privileges, allowing them to install any required software, provided it complies with the conditions specified in the request form.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Detailed information on managing the server, including network and firewall settings, is provided in the TOPdesk application form.
:::

#### **Example use cases** 

- Performing computational or data processing tasks that require a dedicated server environment.
- Running an instance of a service, application, or other specialized tools for a lab or research group not currently centrally provided by the university.
- Hosting a static website, a web application, or an API for a project.
- Hosting databases, such as MySQL, PostgreSQL, MongoDB, or other database management systems.

