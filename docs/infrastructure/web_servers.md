---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-01

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
date-modified: 2025-08-27

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
- infrastructure
- web server 
- Apache
- Nginx

---

If you want to host a website or a web application of some sort, you are going to need to work with a webserver. 
The job of a web server is to serve content on the internet. To achieve that goal, it acts as a middleman between two machines.
The *client machine*  requests content or tasks to the   *server machine*.  A web server typically sits on the *server manchine*, although not necessarly,  and manage requests from multiple clients.   Two of the most popular web servers are **Apache** and **Nginx** (pronounced "Engine-X").

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
- **RAM**: At least 2 GB of RAM is recommended for small applications (e.g., website with a few web pages). For larger applications (e.g., dashboards, data processing platforms, geoportals) or those with high traffic (e.g., 100's of users per day), consider 4 GB or more.
- **Storage**:
  SSDs are preferred for faster data access. The storage capacity depends on the size of your web application and the amount of data you expect to store. A minimum of 20 GB is recommended for small applications, while larger applications may require 100 GB or more.

### Web Server Software

The two most popular web servers are **Apache** and **Nginx**. Sometimes, the choice of web server software is determined by you web application. For example, a web application built with PHP is typically served by Apache, while a web application built with Node.js is typically served by Nginx. 

The tables below compare Apache and Nginx on various features and performance aspects. The comparions were generated by an AI assistant, and reviewed by our team for accuracy.


| Feature                            | Apache HTTP Server                     | NGINX                                       |
| ---------------------------------- | -------------------------------------- | ------------------------------------------- |
| **Architecture**                   | Process/thread-based (prefork, worker) | Event-driven, asynchronous                  |
| **Performance**                    | Slower under high load or concurrency  | High-performance with many concurrent users |
| **Static File Serving**            | Good                                   | Excellent (very fast & lightweight)         |
| **Dynamic Content**                | Built-in via modules (e.g., mod\_php)  | Delegates to upstream (e.g., via FastCGI)   |
| **Configuration Syntax**           | Verbose, flexible `.htaccess`, complex | Simpler, consistent, but less flexible      |
| **.htaccess Support**              | Yes (per-directory overrides)          | No `.htaccess`; central config only         |
| **Reverse Proxy / Load Balancing** | Basic                                  | First-class support, efficient              |
| **TLS/SSL Handling**               | Full support                           | Full support, plus modern config tools      |
| **Resource Usage**                 | Heavier (more RAM per connection)      | Lightweight, better under heavy load        |
| **Modules**                        | Many built-in or loadable modules      | Fewer, but more focused                     |
| **Platform**                       | Cross-platform                         | Mostly Linux/Unix (Windows support exists)  |

: Key differences between Apache and Nginx web servers, source: ChatGPT.


| Feature                | Apache                         | NGINX                              |
| ---------------------- | ------------------------------ | ---------------------------------- |
| **Performance**        | Slower for static file serving | Faster, optimized                  |
| **Resource Usage**     | Higher memory per request      | Efficient, low memory              |
| **TLS, gzip, caching** | Supported                      | Built-in, highly optimized         |
| **Best Use Case**      | Low traffic, legacy sites      | Modern frontends, high-concurrency |

: Comparison between Apache and Nginx web servers for the case of *statics* web applications. Source: ChatGPT.



:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Static vs Dynamic Web Applications
Static web applications serve exactly the same content, such as HTML, CSS, JS. images, to all of its users.
Dynamic web applications serve content that must be generated based a user specific input or choice, therefore, they depend on technologies like PHP, Python, NodeJS, Django, etc., to adapts the content been server.
:::

 

| Feature                    | Apache                                 | NGINX                                            |
| -------------------------- | -------------------------------------- | ------------------------------------------------ |
| **Dynamic handling**       | Built-in via modules (e.g., `mod_php`) | Delegates via FastCGI/Reverse proxy              |
| **Configuration**          | Flexible with `.htaccess`              | Centralized, consistent                          |
| **Performance under load** | May slow down with many threads        | Scales better with async model                   |
| **Language support**       | Good for PHP                           | Good for proxying to Django, Node, Flask, etc.   |
| **Reverse proxy features** | Basic                                  | Advanced** (load balancing, buffering, failover) |

: Comparison between Apache and Nginx web servers for the case of *dynamic* web applications,  source: ChatGPT.


### Security

Security is a critical aspect of web server management. You should keep in mind that a web server is typically open to anyone on the Internet, and therefore, expose to many cyber attacks. Here are some key security measures to consider:

* **Firewall**: Configure a firewall to restrict access to the web server. Only allow necessary ports (e.g., 80 for HTTP, 443 for HTTPS).
* **SSL/TLS**: Use SSL/TLS certificates to encrypt data in transit. This ensures that data exchanged between the client and server is secure.
* **Regular Updates**: Keep the web server software and operating system up to date with the latest security patches.
* **Access Control**: Implement strict access controls to limit who can access the server and its resources. Use SSH keys for secure remote access instead of passwords.
* **Hardening**: Follow best practices for hardening your web server, such as disabling unnecessary modules, using secure configurations, and limiting user permissions, such as [SSL configurations recomended by the Mozilla organisation](https://ssl-config.mozilla.org/)
* * **Monitoring**: Regularly monitor server logs for suspicious activity and set up alerts for potential security breaches.
* **Backup**: Regularly back up your web server data and configurations to recover from potential data loss or security incidents.

### Maintainance

To ensure optimal performance and security of a web server, you need to perform regular maintenance tasks. This includes:

* **Monitoring**: Regularly check server logs for errors or unusual activity. 
* **Updates**: Apply security patches and updates to the web server software and operating system.
* **Backups**: Regularly back up server configurations and data to prevent data loss.
* **Renewal of SSL Certificates**: Ensure that SSL/TLS certificates are renewed before they expire to maintain secure connections.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Do not overlook maintenance
The time, cost and effort of maintaining a web server is often overlooked. Setting up a web server is relatively straightforward, but maintaining it requires ongoing effort and vigilance because you want you web application to be available and secure at all times. Unmaintained web servers are vulnerable to security and data privacy threats.  
:::
