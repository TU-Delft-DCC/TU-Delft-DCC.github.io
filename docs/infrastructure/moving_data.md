---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-07-09

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

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
 - Infrastructure
 - Data
 - Servers
 - scp
 - Citrix

---

This section describes how to transfer data to and from a TU Delft virtual server. The procedure is different depending on whether the server runs a Windows or Linux-based operating system. 


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

If [SSH tunneling](vps_ssh.md) has been configured correctly for the remote host, you can copy files to and from a remote host as follows:

```bash
# Copy TO remote host
$ <path-my-local-file> <host-nickname>:<full-path-remote-directory>/
```

```bash
# Copy FROM remote host
$ scp <host-nickname>:<full-path-remote-file>/ <path-my-local-directory>/ 
```

## Windows servers

Transferring data to and from a TU Delft Windows server is most easily managed using TU Delft Network Drives. These drives provide a central storage space that is accessible from both your local machine and your virtual server. There are many different drives which are used for different purposes; refer to the [Data Storage for Researchers](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=846ebb16181c43b5836c063a917dd199) page in TopDesk for more details.

The process of tranfering data to and from your server involves two main stages: mounting the drive locally to "upload" your files, and accessing them once you are logged into the server.

**Step 1: Add network drived to your local computer**

First, you must connect your local computer to the TU Delft network drives:

* For Windows users: follow the [TU Delft Guide for Windows](https://tudelft.selfguide.com/instruction/d01933ea-5030-42ce-bf46-08dddbccce29) which shows how to add network drives to your File Explorer.
* For macOS users: follow the [TU Delft Guide for macOS](https://tudelft.selfguide.com/instruction/52b28376-51ad-4e80-5dfe-08dde60b89ae) which shows how to access network drives via Finder.

Once added, you can simply drag and drop files from your computer into the drives. 

**Step 2: Access files on the Windows Server**

The network drives are configured to mount automatically whenever you log into a TU Delft Windows server.

1. Connect to your Windows server as per usual.
2. Open File Explorer and navigate to This PC.
3. You will see your network drives listed under Network Locations.
4. To Upload: Copy files from the network drive and paste them onto the server’s local disk (e.g., the Desktop).
5. To Download: Move files from the server into the network drive. They will immediately become available on your local computer via the drive you mounted in Step 1.

::: {.callout-warning appearance="simple" icon="false"}
## {{< fa info-circle >}} Warning

TU Delft Windows servers have a limited amount of disk space in the C: drive. ICT instructs users to install applications and store data in the D: drive of the server to avoid running out of storage memory. Alternatively, you can use your personal TU Delft drive, which is also connected to the server. More information can be found at the bottom of the [TOPdesk form](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34&openedFromService=true) to request a new VPS.
:::
