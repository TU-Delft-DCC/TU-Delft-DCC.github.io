---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
#date: YYYY-MM-DD

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Moving Data to Remote Servers

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

## Overview

In many cases, you will need to transfer files between your local machine and a remote server (e.g., a Virtual Private Server, or VPS). This can include uploading scripts, downloading results, or transferring configuration files. The `scp` command is a powerful tool for securely copying files over SSH.

:::{.callout-important}
## Moving large data batches
If you need to transfer large files or a multititude of small files, consider using tools like [rclone](https://rclone.org/) or [rsync](https://rsync.samba.org/) instead. The  instructions below are for transferring small or few files one at the time.  
:::

## What will you accomplish?
This guide explains how to copy data to and from a remote server (e.g., VPS) using the `scp` command. The `scp` command is a secure file transfer utility that allows you to copy files between hosts on a network. It uses SSH for data transfer, providing the same authentication and security as SSH.


:::{.callout-important}
## Overwriting files
When using `scp`, be cautious about overwriting files. If you copy a file to a destination where a file with the same name already exists, it will be overwritten without warning.
Notice that `scp` will overwrite files in the destination directory if they already exist without prompting. Always double-check the paths and filenames to avoid accidental data loss.
:::

## Prerequisites
Before starting, you need:

* SCP (Secure Copy Protocol) installed on your local machine. SCP is a command-line utility that allows you to securely transfer files between hosts on a network.
* SSH access to the remote host (e.g., VPS) you want to connect to.


## Moving Data via Vanilla SSH
To copy data to and from a remote host using the `scp` command, you can use the following syntax:

```bash
# Copy TO Remote Host
scp <path-my-local-file> <target-username>@<remote-host>:<full-path/remote-directory>/
```

```bash
# Copy FROM Remote Host
scp <target-username>@<remote-host>:<full-path/my-remote-file> <path-my-local-directory>/
```

:::{.callout-tip}
## Moving files to restricted directories
Some directories on the remote host may require elevated permissions to write files. If you encounter a "Permission denied" error, you may need to use `sudo` to copy files to those directories. However, using `scp` with `sudo` directly is not supported. Instead, you can copy the file to a temporary directory `/tmp` where you have write access and then move it to the desired location using `sudo` after connecting to the remote host.
:::

## Transfering Files using ProxyJump

For the case of a VPS hosted by TU Delft, you need to copy data to a remote host via a bastion host (intermediary server). Thefore, you have to use the  `-o` option of the `scp` command to specify a  `ProxyJump`  that will connect to the bastion host first.  Alternatively, you can chose to transfer files using [SSH tunneling](#transfering-files-using-ssh-tunneling).


### Transfer to Remote Host

```bash
# If using default SSH key name, for example, id_ed25519 or  id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" <path-my-local-file> \ 
<target-username>@<remote-host>:<full-path/remote-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp  -i <path-to-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<path-my-local-file>  <target-username>@<remote-host>:<full-path-remote-directory>/

```

### Transfer from Remote Host

```bash
# If using default SSH key name, for example, id_ed25519 or  id_rsa
scp -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \ 
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/

# If using a custom SSH key name, for example, my_custom_key
scp -i <path-to-private-ssh-key> -o "ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl" \
<target-username>@<remote-host>:<full-path-remote-file>/ <path-my-local-directory>/
```

## Transfering Files using SSH Tunneling

If [ssh tunneling](VPS_SSH.md) was configured correctly for the remote host, files could be copied to and from a remote host as follows:

```bash
# Copy TO Remote Host
$ <path-my-local-file> <host-nickname>:<full-path-remote-directory>/
```

```bash
# Copy FROM Remote Host
$ scp <host-nickname>:<full-path-remote-file>/ <path-my-local-directory>/ 
```


<!-- 
## scp with sudo files from a remote host to another remote host

"-C /tmp/a" can be used when you wanted to "cd /tmp/a"

```bash
ssh source.tudelft.nl sudo tar cf - -C /tmp/a . | ssh target.tudelft.nl  sudo tar xvf - -C /tmp/b/
``` -->
