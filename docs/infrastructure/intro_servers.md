---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
#date: MM/DD/YYYY

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Remote servers

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: Name Surname
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - 
# - 

---

TU Delf offers employees the use of Faculty Managed Servers. The only condition is that it is not possible to use these servers to set up services that are already provided by the basic services of SSC ICT. All Faculty Managed Servers available as standard are virtual. 

Hosting Faculty Managed Servers includes:

* ICT provides the server, operating service (Windows, Linux  (Redhat Enterprise Linux (preferred), Ubuntu (LTS) and CentOS)) and network access. 
* The user manages the server and can install whatever he wants within the given conditions (see form …) and is therefore provided with admin rights.
* ICT provides backup, restore and virus scanning (Windows).
* ICT ensures that the Operating System (OS) of the Server (e.g. security patches) is up to date except for Linux. 
* User has the freedom to concentrate on his own applications that are needed for research.

**Some use cases and examples**  

- You might want to run an instance of a service. For example an ftp-server or a PostgreSQL database for your lab or research group, others.
- You want to setup a server to host a static website or web application. 
- You need a server to execute Gitlab-runners


**General required skills**  

- Working with the command line, shell scripting and linux
- Working remotely and securely using ssh
- Transfer files from one computer to another
- Working with containers