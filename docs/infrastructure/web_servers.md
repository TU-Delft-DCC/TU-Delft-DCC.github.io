---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-01

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Web Servers

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Ashley Cryan
author_2: Manuel G. Garcia

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Manuel G. Garcia

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
- web server 
- infrastructure
- Apache
- Ubuntu
- Nginx

---

If you want to host a website or a web application of some sort, you are going to need to work with a webserver. 
The job of a web server is to serve content on the internet. To achieve that goal, it acts as a middleman between two machines.
The *client machine*  requests content or tasks to the   *server machine*.  A web server typically sits on the *server manchine*, although not necessarly,  and manage requests from multiple clients.   Two of the most popular web servers are **Apache 2** and **Nginx**.

This guide provides you with a list of general considerations to take into account when setting up a web server. Links to step-by-step guides are provided for the most popular web servers, Apache and Nginx.

## Considerations when setting up a web server

* **Operating System**: The choice of operating system can affect the performance and security of your web server. 
* **Hardware Requirements**: Ensure that the s1erver hardware meets the requirements for your web application. 
* **Web Server Software**: Choose between popular web server software like Apache, Nginx.
* **Security**: Implement security measures  to protect your server from vulnerabilities.
* **Maintainance**: Regularly update your web server software and operating system to ensure security and performance. Monitor server logs for any unusual activity.

### Operating System
     
The operating system you choose for your web server can significantly impact its performance, security, and compatibility with various software. You need a server-grade operating system because web servers often run on enterprise-grade hardware and require robust performance and security features.
Linux-based systems are commonly used for web servers due to their stability and security features. Some of the most popular distributions include:

* [Ubuntu Server](https://ubuntu.com/download/server), 
* [CentOS](https://www.centos.org/download/), and 
* [Debian](https://www.debian.org/).

For Windows-based servers, you can use [Windows Server](https://www.microsoft.com/en-us/windows-server). A license is required for Windows Server, while Linux distributions are typically free to use. 
At TU Delft, you can request a Personal Virtual Server (VPS) preinstalled with Ubuntu Server or Windows Server. Which one you choose depends on your familiarity with the operating system and the specific requirements of your web application. However, Linux-based servers are generally preferred for web hosting due to their lower resource requirements, free licensing, and strong community support.

### Hardware Requirments

Consider what type of hardware you need for your web server. This includes the CPU, RAM, and storage capacity. 
The hardware requirements depend a mix of factors, including the expected traffic (number of user per day, number of request per user), the complexity of the web application, and the type of content being served.

It is difficult to exactly estimate the hardware requirements for a web server without knowing the details of a web application and performing perfomance tests, but here are some general guidelines:

- **CPU**: A multi-core processor is recommended for handling multiple requests simultaneously. For small to medium-sized applications, a quad-core CPU should suffice.
- **RAM**: At least 2 GB of RAM is recommended for small applications (e.g., website with a few web pages). For larger applications (e.g., dashboard, data processing platforms) or those with high traffic (e.g., 100's of user per day), consider 4 GB or more.
- **Storage**:
  SSDs are preferred for faster data access. The storage capacity depends on the size of your web application and the amount of data you expect to store. A minimum of 20 GB is recommended for small applications, while larger applications may require 100 GB or more.

### Web Server Software
 or Lighttpd. Each has its own strengths and weaknesses.


### Security
 such as firewalls, SSL/TLS encryption, and regular updates


add hardening hints like https://ssl-config.mozilla.org/

### Maintainance
  to ensure optimal performance and security. This includes monitoring server logs, applying security patches, and optimizing configurations.