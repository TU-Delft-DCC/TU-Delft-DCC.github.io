---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-07-09

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Moving data to remote servers

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Securely transfer data to and from TU Delft virtual servers using SCP or Citrix.
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Yasel Quintero
author_2: Manuel G. Garcia

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
 - SCP
 - Citrix
 - infrastructure

---

This section describes how to transfer data to and from a TU Delft virtual server.
The procedure is different depending on whether the server runs a Windows or Linux-based operating system. Although there are many ways to transfer data from one machine to another, TU Delft servers only support a few of them.


## Linux servers

The `scp` command is a secure file transfer utility that allows you to copy files between Linux-based hosts (this includes macOS) on a network. It uses SSH for data transfer, providing the same authentication and security as SSH. Common scenarios in which you might need to transfer data between hosts include uploading scripts, downloading results, or transferring configuration files.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Moving large data batches

If you need to transfer large files or a multitude of small files, consider using tools like [rclone](https://rclone.org/) or [rsync](https://rsync.samba.org/) instead. The instructions below are for transferring small files or a few files at a time.
:::

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Overwriting files

Notice that `scp` will overwrite files in the destination directory without prompting if they already exist. Always double-check the paths and filenames to avoid accidental data loss.
:::

### Prerequisites
Before starting, you need:

* SCP (Secure Copy Protocol) installed on your local machine. SCP is a command-line utility that allows you to securely transfer files between hosts on a network.
* SSH access to the remote host (e.g., VPS) you want to connect to.

### Moving data via SCP
To copy data to and from a remote host using the `scp` command, you can use the following syntax:

```bash
# Copy TO Remote Host
scp <path-my-local-file> <target-username>@<remote-host>:<full-path/remote-directory>/
```

```bash
# Copy FROM Remote Host
scp <target-username>@<remote-host>:<full-path/my-remote-file> <path-my-local-directory>/
```

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Moving files to restricted directories

Some directories on the remote host may require elevated permissions to write files. If you encounter a "Permission denied" error, you may need to use `sudo` to copy files to those directories. However, using `scp` with `sudo` directly is not supported. Instead, you can copy the file to a temporary directory `/tmp` where you have write access and then move it to the desired location using `sudo` after connecting to the remote host.
:::

### Transferring files using `ProxyJump`

In the case of a VPS hosted by TU Delft, you need to copy data to a remote host via a bastion host (an intermediary server). Therefore, you must use the `-o` option of `scp` to specify a `ProxyJump` that will connect to the bastion host first. Alternatively, you can choose to transfer files using [SSH tunneling](#transferring-files-using-ssh-tunneling).

#### Transfer to remote host

```bash
# If using default SSH key name, for example, id_ed25519 or id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" <path-my-local-file> \ 
<target-username>@<remote-host>:<full-path/remote-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp  -i <path-to-custom-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<path-my-local-file>  <target-username>@<remote-host>:<full-path-remote-directory>/

```

#### Transfer from remote host

```bash
# If using default SSH key name, for example, id_ed25519 or id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp -i <path-to-custom-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/
```

### Transferring files using SSH tunneling

If [SSH tunneling](VPS_SSH.md) has been configured correctly for the remote host, you can copy files to and from a remote host as follows:

```bash
# Copy TO remote host
$ <path-my-local-file> <host-nickname>:<full-path-remote-directory>/
```

```bash
# Copy FROM remote host
$ scp <host-nickname>:<full-path-remote-file>/ <path-my-local-directory>/ 
```

## Windows servers

Transferring data to and from a TU Delft Windows server is done via the Citrix platform, using the app's built-in menu shown in the image below.

![Citrix Menu. Buttons from left to right: *Download*, *Upload*, *Multimonitor*, *Clipboard*, and *Settings*.](../img/citrix_menu.png){fig-align="left"}

### Transferring files

1. Open a web browser and log into your Windows server as usual via the [Citrix portal](https://weblogin.tudelft.nl/Citrix/TUDAppsWeb/).
2. Open the Citrix menu located at the center-top of the server window and click on the _Upload_ or _Download_ button, as shown in the image above.
3. A pop-up window will open on where you can select the files you wish to transfer to the server.

It is not possible to directly transfer files to or from the server's C: or D: drives. Instead, you upload or download files to your personal TU Delft drive which is connected to the server. Using the Windows File Explorer and standard copy/paste or drag-and-drop operations, you can transfer the data from your personal drive to the server's C: or D: drives.
 
::: {.callout-warning appearance="simple" icon="false"}
## {{< fa info-circle >}} Warning

TU Delft Windows servers have a limited amount of disk space in the C: drive. ICT instructs users to install applications and store data in the D: drive of the server to avoid running out of memory. Alternatively, you can use your personal TU Delft drive, which is also connected to the server. More information can be found at the bottom of the [TOPdesk form](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34&openedFromService=true) to request a new VPS.
:::

### Using the clipboard

TU Delft Windows servers do not allow to directly copy or paste text from the clipboard. Instead, you must use Citrix's clipboard functionality. To do so, open the Citrix's menu located at the center-top of the window and click on the _Clipboard_ button. A pop-up window will open on which you can copy or paste the text you wish to transfer. Note that it is only possible to transfer text via the clipboard; images or files are not supported.

