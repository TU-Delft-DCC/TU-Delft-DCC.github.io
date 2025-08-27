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

If you want to host a website or a web application, you will need to work with a web server. The job of a web server is to serve content on the internet by acting as a middleman between client machines and server machines. When a client requests content, the web server processes that request and delivers the appropriate response. Popular web server software includes **Apache** and **Nginx**.

This guide provides general considerations to take into account when setting up a web server, along with links to resources for the most commonly used web server platforms. For specific implementation guidance, consult the official documentation for your chosen web server software and operating system.

## Considerations when setting up a web server

* **Operating system**: Choose an operating system that provides appropriate performance, security, and compatibility for your needs.
* **Hardware requirements**: Ensure that the server hardware meets the requirements for your web application and expected traffic levels.
* **Web server software**: Select web server software that aligns with your application requirements (e.g. Apache or Nginx).
* **Security**: Implement security measures to protect your server from vulnerabilities.
* **Maintenance**: Regularly update your web server software and operating system to ensure security and performance. Monitor server logs for any unusual activity.

### Operating system

The choice of operating system significantly impacts your web server's performance, security, and maintenance requirements. Server-grade operating systems are designed for continuous operation and provide robust performance features needed for web hosting environments.

**Linux-based systems** are widely used for web servers due to their stability, security features, and cost-effectiveness. Popular distributions include:

* **Ubuntu Server**: Offers long-term support (LTS) versions with regular security updates and extensive community resources
* **Debian**: Known for stability and security
* **Enterprise Linux distributions**: Include commercially supported options like Red Hat Enterprise Linux (as well as community-driven alternatives)

**Windows Server** provides an alternative for environments requiring Windows-specific technologies or where teams have existing Windows expertise. Commercial licensing is required for Windows Server installations.

At TU Delft, you can request a VPS preinstalled with Ubuntu Server or Windows Server. Which one you choose depends on your familiarity with the operating system and the specific requirements of your web application. However, Linux-based servers are generally preferred for web hosting due to their lower resource requirements, free licensing, and strong community support.

### Hardware requirements

Hardware requirements depend on multiple factors including expected traffic volume, application complexity, data processing needs, and performance requirements. Without performance testing specific to your application, exact requirements can be difficult to determine.

**General guidelines** for basic web server hardware:

- **CPU**: Multi-core processors handle concurrent requests more effectively. Current-generation processors with adequate cores are recommended for most applications.
- **RAM**: Memory requirements vary significantly based on type and expected load. Start with sufficient RAM for your base operating system and application stack, then monitor and adjust based on actual usage patterns.
- **Storage**: SSDs provide better performance than traditional hard drives. Storage capacity should account for your application files, data, logs, and future requirements.

### Web server software

Different web servers excel in different scenarios. The two most popular web servers are **Apache** and **Nginx**. Sometimes, the choice of a web server software is determined by your web application. For example, PHP applications can be served by either Apache (using mod_php) or Nginx (using PHP-FPM), while Node.js applications are commonly served by Nginx as a reverse proxy

The following table provides a general comparison of key characteristics:

| Characteristic | Apache | Nginx |
|----------------|--------|-------|
| **Architecture** | Process/thread-based | Event-driven, asynchronous |
| **Configuration** | Extensive options, flexible | Simpler syntax, centralized |
| **Static Content** | Good performance | Excellent (very fast & lightweight) |
| **Dynamic Content** | Built-in module support | Typically uses external processors |
| **Resource Usage** | Higher memory per connection | Lightweight, better under heavy load |
| **Learning Curve** | Moderate | Varies by use case |
| **Platform** | Cross-platform | Mostly Linux/Unix (Windows support exists)  |

Modern web applications often use **application servers** or **runtime environments** (such as PHP-FPM, Node.js, or Python WSGI servers) in conjunction with web servers to handle dynamic content generation.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Static vs Dynamic Applications
*Static web applications* serve the same content (HTML, CSS, JavaScript, images) to all users. *Dynamic web applications* generate content based on user input, database queries, or other variables, requiring server-side processing.
:::

### Security

Security is a critical aspect of web server management. You should keep in mind that a web server is typically open to anyone on the internet, and therefore, exposed to many cyber attacks. Here are some key security measures to consider:

* **Firewall**: Configure a firewall to restrict access to the web server. Only allow necessary ports (e.g., 80 for HTTP, 443 for HTTPS).
* **SSL/TLS**: Use SSL/TLS certificates to encrypt data in transit. This ensures that data exchanged between the client and server is secure.
* **Regular Updates**: Keep the web server software and operating system up to date with the latest security patches.
* **Access Control**: Implement strict access controls to limit who can access the server and its resources. Use SSH keys for secure remote access instead of passwords.
* **Hardening**: Follow best practices for hardening your web server, such as disabling unnecessary modules, using secure configurations, and limiting user permissions, such as [SSL configurations recommended by the Mozilla organisation](https://ssl-config.mozilla.org/)
* **Monitoring**: Set up logging and monitoring to detect unusual activity or potential security issues.
* **Backup**: Regularly back up your web server data and configurations to recover from potential data loss or security incidents.

### Maintenance

To ensure optimal performance and security of a web server, you need to perform regular maintenance tasks. Plan for regular maintenance activities:

* **Monitoring**: Regularly check server logs for errors or unusual activity. 
* **Updates and patches**: Establish procedures for applying security updates and software patches in a timely manner.
* **Backups**: Regularly back up server configurations and data to prevent loss.
* **Renewal of SSL Certificates**: Ensure that SSL/TLS certificates are renewed before they expire to maintain secure connections.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Do not overlook maintenance
The time, cost and effort of maintaining a web server is often overlooked. While initial setup may be straightforward, maintaining security, availability, and performance requires continuous attention and resources. Unmaintained web servers are vulnerable to security and privacy threats.  
:::