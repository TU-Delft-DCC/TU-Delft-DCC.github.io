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
title: Set Up SSH Tunneling for a VPS

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: how to set up a single-step SSH connection to a VPS using SSH tunneling
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Manuel Garcia
#author_2:

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

## Overview

The default login procedure to a VPS (a remote *Virtual Private Server*) from TU Delft requires to connect to your VPS via a Bastion Host (an intermediary server that control access). Therefore, it is a **two-step** process: to reach a remote host, a user has to connect first to the **bastion host** and from there to the VPS. However, a user connect to a VPS and other remote hosts in a single step using what it is called *ssh tunneling* and *ssh keys*.

Setting up a connection as decribed below simplifies the process of accessing a VPS considerably and allows for secured transfer of files to and from a remote server and a local machine. 

:::{.callout-important}
## Accessing a VPS
Depending on your geogaphic location, access to a VPS via SSH may be blocked by the TU Delft firewall. In such cases, you must use a VPN connection via [eduVPN](https://www.eduvpn.org/). Access if usally blocked if you are connecting from your home network. 
:::

## What will you accomplish?
This guide explains how to set up a single-step SSH connection to a VPS using SSH Tunneling. As a result, you will be able to connect to your VPS from you local machine without the need to log in to the Bastion Host. This also enables the transfering of files between a local machine and the VPS.

## Prerequisites
Before starting, you need:

* TU Delft netID
* Access to a VPS provided by TU Delft ICT, including username and password.
* SSH client installed on your local machine. This is usually the case for most Linux and MacOS distributions. For Windows, you can use a third-party SSH client like [PuTTY](https://www.putty.org/).
* Linux or MacOS terminal

## Steps: Linux and MacOS

:::{.callout-tip}
## Steps in a nutshell
1. Create SSH keys.
2. Copy SSH keys to bastion host and remote server.
3. Create a new host for SSH connection.
4. Test connection
:::


### Set a  SSH Tunneling for a Host (Linux Terminal)

1. If you do not have an SSH key-pair, create one on the local machine. Go to the terminal and enter the following command. Replace `<my-keyname>` with a name of your choice for the SSH key, e.g., `id_rsa` or `id_ed25519`.

```bash
$  ssh-keygen -t ed25519 -f ~/.ssh/<my-keyname>
```


You will be promted to crate a *passphrase*, we recommend you to add one to make the connection more secure. The passphrase will be asked every time you connect to the VPS. To  skip the passphrase, press `Enter` when prompted. You should see something like this:

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
| . ...           |
|o.oEo            |
|*. +.            |
|=*+  .           |
|o*=o+   S        |
|..+=.. .         |
|.+o.. o          |
|*+oo.o.o.        |
|B*oo*B*o..       |
+----[SHA256]-----+
```

A private and public keys will be added to `~/.ssh`. 

The **public key is the file with the `.pub` extension**, e.g., `<my-keyname>.pub`

:::{.callout-tip}
## Pro Tip
Similarly to passwords, it is adviced to rotate your SSH keys regularly, e.g., every 6 months. You can do this by generating a new key pair and replacing the old one on your local machine and VPS.
:::


2. Log in to your VPS and, copy the **content** of your **public key** into the VPS `~/.ssh/authorized_keys` file. You can achieve this by copying the content of the public key file to the clipboard and pasting it into the `authorized_keys` file on the VPS. Be mindful of now removing anything form this file or other SSH connection might stop working. Finally, save the file.



3. Create a new host for SSH connection. On your local machine, edit the `~/.ssh/config` file and add the following configuration. If the file does not exist, create it.

```bash 
Host <host-nickname>
    HostName <target-host>
    User <target-username>
    ProxyJump <target-username>@linux-bastion-ex.tudelft.nl
    IdentityFile ~/.ssh/<my-keyname>
```

Replace:
**<host-nickname>:** a name for you choice for the targe host, e.g., `my-server`
**<target-host>:** the actual name of the target host (FQDM), e.g, `server.tudelft.nl`
**<target-username>:**  the username used to login to the target host, usually your NetID
**<bastion-username>:** the username used to login to the bastion server
**<my-keyname>:** the name of the SSH private key you created, e.g., `id_rsa`. If your private key is stored in a different location, replace the path accordingly.


4. Test the SSH Tuneling connection. Connect to the VPS using *ssh tunneling* by typing the command below. Use your *bastion-password* when asked. That is usually the password associate to your NetID.

```bash
$ ssh <host-nickname>
```

If you encounter problems with the connection. Use the debug mode `ssh -vvv <host-nickname>` to find out what might have gone wrong. This command will provide detailed information about the connection process and can help you troubleshoot any issues.
