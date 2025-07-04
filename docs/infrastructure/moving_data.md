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
 
::: {.callout-warning appearance="simple" icon="false"}
## {{< fa info-circle >}} Warning

TU Delft Windows servers have a limited amount of disk space in the C: drive. ICT instructs users to install applications and store data in the D: drive of the server to avoid running out of memory. Alternatively, you can use your personal TU Delft drive, which is also connected to the server. More information can be found at the bottom of the [TOPdesk form](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34&openedFromService=true) to request a new VPS.
:::

### Using the clipboard

TU Delft Windows servers do not allow to directly copy or paste text from the clipboard. Instead, you must use Citrix's clipboard functionality. To do so, open the Citrix's menu located at the center-top of the window and click on the _Clipboard_ button. A pop-up window will open on which you can copy or paste the text you wish to transfer. Note that it is only possible to transfer text via the clipboard; images or files are not supported.

# Linux Servers

To connect to a Linux VPS, TU Delft uses a proxy server know as bastion. Unless **SSH tunneling** is configured, to transfer data from your local computer to the Linux VPS, you must first transfer the data to bastion, and from there transfer it to your VPS. The same applies when transfering data from the VPS to your local computer.

Data transfer is done with the `scp` command:

```bash
scp <options> <data-source> <data-destination>
```

::: {.callout-warning appearance="simple" icon="false"}
## {{< fa info-circle >}} Warning

The bastion is solely intended for connecting to a VPS and storing SSH keys. It is not designed for storing large amounts of data. Therefore, user home directories have limited storage capacity. Don't forget to delete the files you transfer to or from your VPS.
:::

## Transfering data to the VPS

To copy a file from your local computer to your Linux VPS:

1. If your local computer is running on Linux or MacOS, open the terminal. Alternatively, if it runs on Windows, open the Windows PowerShell by seaching for it in the start menu.

2. Copy your local file to the bastion by executing the command:
```bash
scp <path-to-local-file> <netid>@linux-bastion-ex.tudelft.nl:/<bastion-directory>/

# For example:
# scp C:/Users/janedoe/Desktop/file.zip janedoe@linux-bastion-ex.tudelft.nl:/home/janedoe/Documents/
```
3. Login to the bastion (you need to be connected to eduVPN if working off-campus):
```bash
ssh <netid>@linux-bastion-ex.tudelft.nl
```

4. Copy the file from the bastion to your Linux VPS. Note that an SSH key is required to access the VPS.
```bash
scp -i ~/.ssh/<your-ssh-key> <path-to-bastion-file> <username>@<server-name>.tudelft.nl:/<vps-directory>

# For example:
# scp -i ~/.ssh/id_rsa /home/janedoe/Documents/file.zip janedoevps.ict.tudelft.nl:/home/janedoe/
```
5. Delete the file on the bastion and logout:
```bash
rm <path-to-bastion-file>
logout
```

## Transfering data from the VPS

To copy a file from your Linux VPS to your local computer:

1. If your local computer is running on Linux or MacOS, open the terminal. Alternatively, if it runs on Windows, open the PowerShell by seaching for it in the start menu.

2. Login to the bastion (you need to be connected to eduVPN if working off-campus):
```bash
ssh <netid>@linux-bastion-ex.tudelft.nl
```

3. Copy the file from your Linux VPS to the bastion. Note that an SSH key is required to access the VPS. Logout of the bastion.
```bash
scp -i ~/.ssh/<your-ssh-key> <username>@<server-name>.tudelft.nl:/<path-to-vps-file> <bastion-directory>
logout

# For example:
# scp -i ~/.ssh/id_rsa janedoe@janedoevps.ict.tudelft.nl:/home/janedoe/Documents/file.zip /home/janedoe/ 
```

4. Copy the file from the bastion to your local computer:
```bash
scp <netid>@linux-bastion-ex.tudelft.nl:/<path-to-bastion-file> <local-path>

# For example:
# scp janedoe@linux-bastion-ex.tudelft.nl:/home/janedoe/file.zip C:/Users/janedoe/Desktop/
```  

5. Login to the bastion, delete the file and logout.
 ```bash
ssh <netid>@linux-bastion-ex.tudelft.nl
rm <path-to-bastion-file>
logout
```

## Transfering data with SSH tunneling

When SSH tunneling is configured, data can be transferred directly between your local computer and the Linux VPS, without needing to temporarily store it on the bastion.

```bash
# Copy file TO Remote Host
$ scp <path-to-local-file> <host-name>:/<remote-directory>/
```

```bash
# Copy file FROM Remote Host
$ scp <host-name>:/<path-to-remote-file> /<local-directory>/ 
```