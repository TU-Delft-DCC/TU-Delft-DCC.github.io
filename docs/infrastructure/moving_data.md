---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2026-01-27

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2026-01-27

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Transferring data to and from remote servers

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Secure data transfer to and from TU Delft virtual servers using scp (Linux) or Network Drives (Windows).
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
 - SCP
 - Network Drives

---

This section describes how to transfer data to and from a TU Delft virtual private server (VPS). Common scenarios in which you might need to transfer data between hosts include uploading scripts, downloading results, or transferring configuration files. The procedure is different depending on whether the server runs a Windows or Linux-based operating system.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Off-Campus Access
When working off-campus you must be connected to eduVPN to access your VPS. Please refer to the TU Delft manuals for [working remotely](https://www.tudelft.nl/en/it-manuals/working-remotely) and [configuring eduVPN](https://www.tudelft.nl/en/it-manuals/applications/vpn).
:::

## Linux servers

The `scp` utility is the standard tool for secure file transfers on Linux and macOS. It uses the Secure Shell (SSH) protocol, which means that if you can connect to a server using `ssh`, you can also transfer files to and from it using `scp`.

The `scp` command is executed from a command-line interface on your local computer:

* **Linux, macOS and WSL**: open the Terminal application
* **Windows**: open PowerShell or use the Windows Subsystem for Linux (WSL)

The general syntax of the `scp` command is:

```bash
# Copy TO remote server
scp <path-to-local-file> <target-username>@<remote-server>:<full-path/remote-directory>/

# Copy FROM remote server
scp <target-username>@<remote-server>:<full-path/remote-file> <path-to-local-directory>/
```

**Connecting via the Bastion Host**

All connections to TU Delft Linux VPS, including data transfers, must be routed through an intermediary server called the Bastion Host. There are two supported ways to route `scp` connections through the Bastion Host:

1. **ProxyJump**: explicitly routes each `scp` command through the bastion host
2. **SSH tunneling**: uses a pre-configured SSH setup that allows direct access via a host alias

The following sections describe both approaches.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Moving large data batches

If you need to transfer large files or a multitude of small files, consider using tools like [rclone](https://rclone.org/) or [rsync](https://rsync.samba.org/) instead. The instructions below are for transferring small files or a few files at a time.
:::

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Overwriting files

Notice that `scp` will overwrite files in the destination directory without prompting if they already exist. Always double-check the paths and filenames to avoid accidental data loss.
:::

::: {.callout-warning appearance="simple" icon="false"}
## {{< fa info-circle >}} Permissions

Some directories on the remote host may require elevated permissions to write files. If you encounter a "Permission denied" error, you may need to use `sudo` to copy files to those directories. However, using `scp` with `sudo` directly is not supported. Instead, you can copy the file to a temporary directory `/tmp` where you have write access and then move it to the desired location using `sudo` after connecting to the remote host.
:::

### Transferring files using ProxyJump

When using ProxyJump, the bastion host is specified directly in the `scp` command via the `-o` option. This approach requires no prior SSH tunneling configuration and is suitable for occasional file transfers.

**Transfer TO remote server**

```bash
# If using default SSH key name, for example, id_ed25519 or id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" <path-my-local-file> \ 
<target-username>@<remote-host>:<full-path/remote-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp  -i <path-to-custom-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<path-my-local-file>  <target-username>@<remote-host>:<full-path-remote-directory>/
```

**Transfer FROM remote server**

```bash
# If using default SSH key name, for example, id_ed25519 or id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp -i <path-to-custom-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/
```

### Transferring files using SSH tunneling

If SSH tunneling has been configured, file transfers can be performed without explicitly referencing the bastion host. This method is recommended for frequent use, as it simplifies commands and reduces repetition.

Instructions for establishing an SSH connection to a Linux VPS and configuring SSH tunneling are provided in our [Server Connection guide](vps_ssh.md).

```bash
# Copy TO remote server
$ scp <path-to-local-file> <host-nickname>:<full-path-remote-directory>/

# Copy FROM remote server
$ scp <host-nickname>:<full-path-remote-file>/ <path-to-local-directory>/ 
```

## Windows servers

Transferring data to and from a TU Delft Windows server is most easily managed using TU Delft Network Drives. These drives provide a central storage space that is accessible from both your local machine and your virtual server. There are many different drives which are used for different purposes; refer to the [Data Storage for Researchers](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=846ebb16181c43b5836c063a917dd199) page in TopDesk for more details.

The process of transferring data to and from your server involves two main stages: mounting the drive locally to "upload" your files, and accessing them once you are logged into the server.

**Step 1: Add network drives to your local computer**

First, you must connect your local computer to the TU Delft network drives:

* For Windows users: follow the [TU Delft Guide for Windows](https://tudelft.selfguide.com/instruction/d01933ea-5030-42ce-bf46-08dddbccce29) which shows how to add network drives to your File Explorer.
* For macOS users: follow the [TU Delft Guide for macOS](https://tudelft.selfguide.com/instruction/52b28376-51ad-4e80-5dfe-08dde60b89ae) which shows how to access network drives via Finder.

Once added, you can simply drag and drop files from your computer into the drives. 

**Step 2: Access files on the Windows server**

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
