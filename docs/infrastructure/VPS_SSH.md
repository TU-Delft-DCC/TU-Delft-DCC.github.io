---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
#date: MM/DD/YYYY

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Set Up SSH Connection to VPS

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

The default login procedure to a VPS (a remote *Virtual Private Server*) from TU Delft requires to connect to your VPS via a Bastion Host (an intermediary server that control access). Therefore, it is a **two-step** process: to reach a remote host, a user has to connect first to the **bastion host** and from there to the VPS. However, a user can connect directly to the VPS and other remote hosts using what it is called *ssh tunneling* and *ssh keys*.

Setting up a connection as decribed below simplifies the process of accessing a VPS considerably and allows for secured transfer of files to and from a remote server and a local machine. 

## What will you accomplish?
This guide explains how to set up a single-step SSH connection to a VPS using SSH Keys. As a result, you will be able to connect to your VPS from you local machine, without the need to log in to the Bastion at TU Delft every time and transfer files between a remote server and a local machine.

## Prerequisites
Before starting, you need:

* TU Delft netID
* Access to a VPS provided by TU Delft ICT
* MacOS, Linux, or Windows


## Steps

### Linux and MacOS

:::{.callout-tip}
## Steps in a nutshell
1. Create SSH keys.
2. Copy SSH keys to bastion host and remote server.
3. Test connection
:::

CONTINUE HERE

## Set a Default SSH Tunneling for a Host (Linux Terminal)

1. On your local machine, edit the `~/.ssh/config` file and add the following configuration:

```bash 
Host <host-nickname>
    HostName <target-host>
    User <target-username>
    ProxyCommand ssh <bastion-username>@linux-bastion-ex.tudelft.nl -W %h:%p 
```

Replace:
**<host-nickname>:** a name for you choice for the targe host, e.g., `my-server`
**<target-host>:** the actual name of the target host (FQDM), e.g, `server.tudelft.nl`
**<target-username>:**  the username used to login to the target host
**<bastion-username>:** the username used to login to the bastion server

1. Create a key-pair on the local machine.

```bash
$ ssh-keygen -f ~/.ssh/<my-keyname> -t rsa -b 4096
```

You will be promted to crate a *passphrase*, we recommend you to add one to make the connection more secure. The passphrase will be asked every time you connect to the target host.

A private and public keys will be added to `~/.ssh`. The public key is in the `<my-keyname>.pub`

3. Copy the content of the public key to the `~/.ssh/authorized_keys` file in the target host.

4. Connect to the target host using *ssh tunneling*. Use your *bastion-password* when asked.

```bash
$ ssh <host-nickname>
```

If you encounter problems with the connection. Use the debug mode `ssh -vvv <host-nickname>` to find out what might have gone wrong.


## Tunneling with WinSCP

WinSCP is a GUI that makes it very easy to inspect, edit and transfer files on the webserver. Instructions for setting this up on a hypothetical server from the CiTG faculty are provided below. General documentation on tunneling with WinSCP are here: https://winscp.net/eng/docs/ui_login_tunnel

_These instructions were tested with an existing `id_ed25519` key, assume you already have WinSCP installed and can modify a text file on the server in your user directory using the terminal._

Do the following:

1. As explained above, log in to the server and add your public key to the file `/home/<username>/.ssh/authorized_keys` (this only needs to be done once).

It should look like this with your own keys `XXXXXXX` and NetID filled between the `<...>` (note the `<XXXXXXX>` is much longer in reality):

```bash
ssh-rsa <XXXXXXX> ICT-SYSTEMS-<NETID>
ssh-rsa <XXXXXXX> ICT-SYSTEMS-<NETID>
ssh-ed25519 <XXXXXXX> <NETID>@tudelft.nl
```

2. Using WinSCP, the following fields should be entered:

On the main login settings page:
- File protocol: `SFTP`
- Host name: `<server>.citg.tudelft.nl`
- User name: your NetID

3. Open the "Advanced..." window

4. On the page "Tunnel" (under heading "Connection," still in the Advanced window):
- Host name: `linux-bastion-ex.tudelft.nl`
- User name: your NetID

5. On the page "Authentication" (under heading "SSH," still in the Advanced window):
- Private key file: select your private key file, for example `C:..../<username>/.ssh/id_ed25519`
- Note that the app may ask you to convert your existing key to a Putty format (for example "Do you want to convert OpenSSH private key to PuTTY format?"). Click "OK" then make sure you select the new PuTTY file (e.g., `C:..../<username>/.ssh/id_ed25519.ppk`)

6. Save the setting and click "Login", using your NetID password to authenticate.

### Using WinSCP with sudo rights

If you have sudo rights on the webserver you can use this via WinSCP as follows:

1. Once agin go to the "Advanced..." window to the "SFTP" page under heading "Environment"
2. In field "SFTP server" enter the following: `sudo /usr/lib/openssh/sftp-server`
3. Save the changes
4. Use with caution!

Note that the path to `sftp-server` may be different but can be easily checked and arranged. This will not work if you change the setting and continue to use an open session.
