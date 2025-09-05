---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-09-03

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
date-modified: 2025-09-03

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Set up SSH tunneling for a VPS

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: how to set up a single-step SSH connection to a VPS using SSH tunneling
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Manuel Garcia
author_2: Raul Ortiz Merino

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Manuel Garcia
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
- ssh tunneling
- ssh keys
- bastion host
- vps 
- scp

---

This guide explains how to set up a secure, single-step Secure Shell (SSH) connection to a Virtual Private Server (VPS) at TU Delft. SSH is a protocol that allows secure remote access to servers over an unsecured network. 

Commonly, connecting to a VPS requires first accessing a **Bastion Host** (an intermediary server controlling access). Faculty managed setup as VPSs at TU Delft can be accessed by two types of bastion hosts: `linux-bastion-ex.tudelft.nl` having a local /home directory, and `linux-bastion.tudelft.nl` having access to your own central /home directory. In this sense, `linux-bastion-ex.tudelft.nl` is a more secure option recommended for the steps below. 

Connecting to a VPS via a bastion host, is a two-step process. However, by using SSH tunneling and SSH keys, you will be able to connect directly from your local machine to your VPS. This setup bypassing the need to log in to the bastion host separately, for example, simplifies secure file transfers between your local machine and the VPS.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Accessing a VPS
Depending on your geographic location, access to a VPS via SSH may be blocked by the TU Delft firewall. For example, access is usually blocked if you are connecting from your home network. Therefore, before going through the following steps, please check the [TU Delft manuals for working remotely](https://www.tudelft.nl/en/it-manuals/working-remotely) for [eduVPN](https://www.tudelft.nl/en/it-manuals/applications/vpn) and [bastion host](https://www.tudelft.nl/ict-handleidingen/linux-bastion-host).
:::

### Prerequisites
Before starting, you need:

* A TU Delft NetID.
* Access to a VPS provided by TU Delft ICT. Check [this guide](../infrastructure/VPS_request.md) for more information on how to request a VPS.
* An SSH client installed on your local machine. This is usually included in most Linux and macOS distributions via a terminal or shell. For Windows, you can use a third-party SSH client like [PuTTY](https://www.putty.org/) or a windows subsystem for Linux (wsl).

### Steps for Linux (including wsl) and macOS

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Summary of steps
1. Create SSH keys.
2. Copy SSH keys to bastion host and remote server.
3. Create a new host for SSH connection.
4. Test connection.
:::


#### **Set up SSH tunneling**

1. If you do not have an SSH key-pair, create one on the local machine. Go to the terminal and enter the following command. Replace `<my-keyname>` with a name of your choice for the SSH key, e.g., `id_rsa` or `id_ed25519`.

```bash
$  ssh-keygen -t ed25519 -f ~/.ssh/<my-keyname>
```

You will be prompted to create a *passphrase*. We recommend you to add one to make the connection more secure. The passphrase will be asked every time you connect to the VPS. To skip the passphrase, press `Enter` when prompted. You should see something like this:

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

A private and public key will be added to `~/.ssh`. 

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Accessing .ssh
`~/` in `~/.ssh` refers to your /home directory. As stated above, this is different for the two bastion hosts at TU Delft. For `linux-bastion-ex.tudelft.nl`, it refers to the local /home directory of the bastion host, while for `linux-bastion.tudelft.nl`, it refers to your central /home directory.
`.` in `~/.ssh` refers to a hidden directory. To view hidden files and directories in the terminal, you can use the command `ls -a`.
:::

The **public key is the file with the `.pub` extension**, e.g., `<my-keyname>.pub`

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
Similar to passwords, it is advised to rotate your SSH keys regularly (e.g., every 6 months). You can do this by generating a new key pair and replacing the old one on your local machine and VPS.
:::


2. Log in to your VPS and, copy the **content** of your **public key** into the VPS `~/.ssh/authorized_keys` file. You can achieve this by copying the content of the public key file to the clipboard and pasting it into the `authorized_keys` file on the VPS. Be mindful and not remove anything from this file, or other SSH connections might stop working. Finally, save the file.



3. Create a new host for SSH connection. On your local machine, edit the `~/.ssh/config` file and add the following configuration. If the file does not exist, create it.

```bash 
Host <host-nickname>
    HostName <target-host>
    User <target-username>
    ProxyJump <bastion-username>@linux-bastion-ex.tudelft.nl
    IdentityFile ~/.ssh/<my-keyname>
```

Replace:

- `<host-nickname>`: a name of your choice for the target host, e.g., `my-server`.
- `<target-host>`: the actual name of the target host (FQDM), e.g, `server.tudelft.nl`.
- `<target-username>`:  the username used to log in to the target host, usually your NetID.
- `<bastion-username>`: the username used to log in to the bastion server (often same as NetID, but keep separate in case it differs).
- `<my-keyname>`: the name of the SSH private key you created, e.g., `id_rsa`. If your private key is stored in a different location, replace the path accordingly.


4. Test the SSH tunneling connection. Connect to the VPS using *SSH tunneling* by typing the command below. Use your *bastion-password* when asked. This is usually the password associated with your NetID.

```bash
$ ssh <host-nickname>
```

If you encounter problems with the connection, use the debug mode `ssh -vvv <host-nickname>` to find out what might have gone wrong. This command will provide detailed information about the connection process and can help you troubleshoot any issues.