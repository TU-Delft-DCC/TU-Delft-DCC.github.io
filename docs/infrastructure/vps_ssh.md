---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2026-01-27

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
date-modified: 2026-01-27

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Connecting to remote servers

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Secure connection to TU Delft virtual servers using SSH (Linux) or RDP (Windows).
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Manuel Garcia
author_2: Raúl Ortiz Merino
author_3: Yasel Quintero

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Manuel Garcia
maintainer_2: Yasel Quintero

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly

categories: 
 - Infrastructure
 - Servers
 - VPS
 - SSH Tunneling
 - SSH Keys
 - Bastion Host
 - SCP
 - Cybersecurity

---

This guide provides instructions for establishing a secure connection to your TU Delft Virtual Private Server (VPS). Connection methods vary based on your local operating system and whether your remote server runs Windows or Linux.

Before you begin, ensure you have the following:

* A valid TU Delft NetID.
* Access to a TU Delft VPS. If you do not have one, follow our [VPS Request](../infrastructure/vps_request.md) guide to request a new server. To access a server owned by a colleague, the owner must contact ICT to grant you permission.
* An SSH or RDP client application. More details are provided below.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Off-Campus Access
When working off-campus you must be connected to eduVPN to access your VPS. Please refer to the TU Delft manuals for [working remotely](https://www.tudelft.nl/en/it-manuals/working-remotely) and [configuring eduVPN](https://www.tudelft.nl/en/it-manuals/applications/vpn).
:::

## Connecting to a Windows server

The standard method for connecting to a Windows VPS is through a **Remote Desktop Protocol (RDP)** connection. An RDP connection allows you to access the remote machine using a visual "desktop" environment, where you can use your mouse and keyboard just as you would on your local computer.

To establish this connection, you require a Remote Desktop client on your local computer. The tool you will use depends on your local operating system:

* **Windows**: use the built-in Remote Desktop Connection (MSTSC) application and follow the [RDP Manual for Windows](https://filelist.tudelft.nl/ICT%20Handleidingen/2%20-%20Nieuwe%20handleidingen/Citrix%20Folder/RDP/RDP%20-%20Remote%20Access%20to%20Server%20-%20Windows%20-%20v1.0.pdf).
* **macOS**: download and install the [Windows App](https://apps.apple.com/us/app/windows-app/id1295203466?mt=12) from the Mac App Store and follow the [RDP Manual for MacOS](https://filelist.tudelft.nl/ICT%20Handleidingen/2%20-%20Nieuwe%20handleidingen/Citrix%20Folder/RDP/RDP%20-%20Remote%20Access%20to%20Server%20-%20macOS%20-%20v1.0.pdf).
* **Linux**: download and install the Remmina client and follow the [RDP Manual for Linux](https://filelist.tudelft.nl/ICT%20Handleidingen/2%20-%20Nieuwe%20handleidingen/Citrix%20Folder/RDP/RDP%20-%20Remote%20Access%20to%20Server%20-%20Linux%20-%20v1.0.pdf).


## Connecting to a Linux server

The standard method for connecting to a Linux VPS is through a Secure Shell (SSH) connection. This creates an encrypted "tunnel" between your computer and the server, allowing you to type commands directly into the remote machine. 

To establish this connection, you require an SSH client on your local computer. The tool you will use depends on the operating system of your local computer:

* **macOS and Linux**: You do not need to install additional software. You can use the built-in Terminal application already available on your system.
* **Windows**: While modern Windows versions include basic SSH support via cmd or PowerShell, it is often more user-friendly to use a dedicated application. We recommend [PuTTY](https://www.putty.org/). Alternatively, you may use the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/).

Connecting to a TU Delft Linux VPS requires first accessing a [Bastion Host](https://intranet.tudelft.nl/en/ict-en/linux-bastion-host) (an intermediary server controlling access). VPS can be accessed by two types of bastion hosts: `linux-bastion-ex.tudelft.nl` which provides a local `/home` directory, and `linux-bastion.tudelft.nl` which provides access to your central university `/home` directory. In this sense, `linux-bastion-ex.tudelft.nl` is a more secure option and recommended for the steps below. 


### Connecting from Linux, macOS or the WSL

Connecting to a VPS via a bastion host is typically a two-step process. However, by using **SSH tunneling** and SSH keys, you can establish a connection from your local machine to your VPS in a single step. This simplifies the connection process and makes secure file transfers between your local machine and the VPS much more efficient.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Summary of steps
1. Create SSH keys.
2. Copy SSH keys to bastion host and remote server.
3. Create a new host for SSH connection.
4. Test connection.
:::

**1. Create SSH keys**

If you do not have an SSH key-pair, create one on the local machine. Open the terminal and enter the following command. Replace `<my-keyname>` with a name of your choice for the SSH key, e.g., `id_rsa` or `id_ed25519`.

```bash
$  ssh-keygen -t ed25519 -f ~/.ssh/<my-keyname>
```

You will be prompted to create a *passphrase*. We recommend you to add one to make the connection more secure. The passphrase will be requested every time you connect to the VPS. To skip the passphrase, press `Enter` when prompted. You should see something like this:

``` bash
Generating public/private ed25519 key pair.
Enter passphrase for "ed25519" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in ~/.ssh/<my-keyname>
Your public key has been saved in ~/.ssh/<my-keyname>.pub
The key fingerprint is:
SHA256:6j06srvun06gJ5UCmD+MVq6RsPuytCO5mF4hTELnWTg root@local-machine
The key's randomart image is:
+--[ED25519 256]--+
<image cut for security reasons>
+----[SHA256]-----+
```

A private and public key pair will be created in `~/.ssh`. 

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Accessing `.ssh`
`~/` in `~/.ssh` refers to your `/home` directory. As stated above, this is different for the two bastion hosts at TU Delft. For `linux-bastion-ex.tudelft.nl`, it refers to the local `/home` directory of the bastion host, while for `linux-bastion.tudelft.nl`, it refers to your central `/home` directory.
`.` in `~/.ssh` refers to a hidden directory. To view hidden files and directories in the terminal, you can use the command `ls -a`.
:::

The **public key is the file with the `.pub` extension**, e.g., `<my-keyname>.pub`

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Similar to passwords, it is advised to rotate your SSH keys regularly (e.g., every 6 months). You can do this by generating a new key pair and replacing the old one on your local machine and VPS.
:::


**2. Copy SSH keys to bastion host and remote server**  

You must "authorize" your key on both the bastion and your VPS. The easiest way to do this is using the `ssh-copy-id` command:

```bash
# First, authorize the key in the bastion host
ssh-copy-id -i ~/.ssh/<my-keyname>.pub <netID>@linux-bastion-ex.tudelft.nl

# Second, authorize the key on your VPS (you will go through the bastion)
ssh-copy-id -i ~/.ssh/<my-keyname>.pub -o ProxyJump=<netID>@linux-bastion-ex.tudelft.nl <netID>@<vps-address>
```

You will be prompted to enter your password when executing both commands.

**3. Create a new host for SSH connection** 

On your local machine, edit the `~/.ssh/config` file and add the following configuration. If the file does not exist, create it.

```bash 
Host <host-nickname>
    HostName <target-host>
    User <target-username>
    ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl
    IdentityFile ~/.ssh/<my-keyname>
```

Replace:

- `<host-nickname>`: a name of your choice for the target host, e.g., `my-server`.
- `<target-host>`: the actual name of the target host (FQDN), e.g., `server.tudelft.nl`.
- `<target-username>`:  the username used to log in to the target host, usually your NetID.
- `<bastion-username>`: the username used to log in to the bastion server (often same as NetID, but keep separate in case it differs).
- `<my-keyname>`: the name of the SSH private key you created, e.g., `id_rsa`. If your private key is stored in a different location, replace the path accordingly.


**4. Test the SSH tunneling connection** 

Connect to the VPS using *SSH tunneling* by typing the command below. Use your *bastion-password* when asked. This is usually the password associated with your NetID.

```bash
$ ssh <host-nickname>
```

If you encounter problems with the connection, use the debug mode `ssh -vvv <host-nickname>` to find out what might have gone wrong. This command will provide detailed information about the connection process and can help you troubleshoot any issues.

