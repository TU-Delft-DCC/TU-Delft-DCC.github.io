---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-28

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Transfering data to and from a VPS

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Yasel Quintero
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
 - data
 - infrastructure

---

This section describes how to transfer data to and from a TU Delft managed server. The procedure is different depending on whether the server runs a Windows or Linux-based operating system. Although there are many ways to transfer data from one machine to another, TU Delft servers only support a few of them.

# Windows Servers

Tranfering data to and from a TU Delft Windows server is done via the Citrix platform, using the app's built-in menu shown in the image below.

![Citrix Menu. Buttons from left to righ: Download, Upload, Multimonitor and Clipboard and Settings.](../img/citrix_menu.png){fig-align="left"}

### Transfering files

1. Open a web browser and log into your Windows server in the usual way, using the [Citrix portal](https://weblogin.tudelft.nl/Citrix/TUDAppsWeb/).
2. Open the Citrix menu located at the center-top of the server window and click on the _Upload_ or _Download_ button as shown in the image above.
3. A pop-up window will open on which you can select the files you wish to transfer to the server.

It is not possible to directly transfer files to or from the server's C: or D: drive. Instead, you upload or download files to your personal TU Delft drive which is connected to the server. Using the Windows File Explorer and standard copy-paste or drag-and-drop operations you can transfer the data from your personal drive to the server's C: or D: drives.
 
::: {.callout-warning}
TU Delft Windows servers have a limited amount of disk space in the C: drive. ICT instructs users to install applications and store data in the D: drive of the server to avoid running out of memory. Alternatively, you can use your personal TU Delft drive, which is also connected to the server. More information can be found at the bottom of the [TOPdesk form](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34&openedFromService=true) to request a new VPS.
:::

### Using the clipboard

TU Delft Windows servers do not allow to directly copy or paste text from the clipboard. Instead, you must use Citrix's clipboard functionality. To do so, open the Citrix's menu located at the center-top of the window and click on the _Clipboard_ button. A pop-up window will open on which you can copy or paste the text you wish to transfer. Note that it is only possible to transfer text via the clipboard; images or files are not supported.

# Linux Servers

### Copy Data from Client to Host using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <my-local-file>  <target-username>@<target-host>:/<remote-directory>/
```
### Copy Data from Host to Client using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <target-username>@<target-host>:/tmp/<my-remote-file> /<my-local-directory>/
```

### Copy Data using SSH Tunneling

If a default [ssh tunneling](VPS_SSH.md) was configured correctly. Data can be copied to and from a remote host as follows:

```bash
# Copy TO Remote Host
$ scp <my-local-file> <host-nickname>:/<remote-directory>/
```

```bash
# Copy FROM Remote Host
$ scp <host-nickname>:/<my-remote-file> /<my-local-directory>/ 
```

### scp with sudo files from a remote host to another remote host
"-C /tmp/a" can be used when you wanted to "cd /tmp/a"

```bash
ssh source.tudelft.nl sudo tar cf - -C /tmp/a . | ssh target.tudelft.nl  sudo tar xvf - -C /tmp/b/
```
