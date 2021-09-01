# One-step SSH to server

## Background
The default login procedure to VPS from TU Delft is to connect to the Bastion host (an intermediary server) and then to your server, so it is a two-step process.  Steps A and B are described by ICT admin in the email confirming deployment of your server.

Configuring a one-step SSH connection to a VPS (Virtual Private Server) from your local machine simplifies the process of accessing the VPS considerably and allows for secure transfer of files to and from the virtual and local environments. 

The directions below are written for Linux and Mac users. Windows users can configure a VPS connection via SSH using a third-party SSH client like [PuTTY](https://www.putty.org/). We are in the process of drafting documentation for this, its current state is at the bottom of this page.

## What this documentation will help achieve
This guide explains how to configure a one-step connection to a VPS from your local machine through the Bastion host managed by TU Delft. 

## Prerequisites
* TU Delft netID
* VPS provided by TU Delft ICT
* Mac or Linux OS (Windows users, please see the end of this page for instructions on using a client program to establish a direct SSH connection)

## Tools/Software
* If using Windows, PuTTY or cygwin (see bottom of page)

## Steps
1. Enter the `.ssh` directory on your local machine
2. Edit local `~/.ssh/config` file
3. Check that your local machine’s `known_hosts` file contains the SSH key for the tu-bastion-ex host 
4. Generate SSH key pair to store on local machine (if you already have an SSH key pair from another application, you can use this existing one)
5. Copy your public SSH key from your local machine to the Bastion host (tu-bastion-ex)
6. SSH to the Bastion host and check that your public key has been successfully copied
7. Copy contents of your public SSH key from your local machine
8. SSH from your local machine to the Bastion host and then to your VPS using its domain name 
9. Paste contents of public SSH key at the end of the `authorized_keys` file on the VPS
10. SSH into your VPS directly from your local machine using its alias

### Step 1: Enter the .ssh directory on your local machine

Open your terminal (click on the magnifying glass in the upper right toolbar and search "terminal") and enter: 
```
username@localmachine ~ % cd .ssh
```

### Step 2. Edit local `~/.ssh/config` file 
Use the in-terminal text editor vi to open and edit the ssh config file according your server details. In your terminal, type:

`username@localmachine .ssh % vi config`

And hit Enter. Customise fields by first hitting “i” to enter insert mode. You can choose any short term as the alias for your server, which will be used to access it via SSH after configuration. *Note:* Make sure to remove <> from all fields below. When you are finished, hit “escape” and then type `:wq` to save the file and quit the vi editor.

The file will look like this: 

```
Host tu-bastion-ex
    HostName linux-bastion-ex.tudelft.nl
    User <USERNAME>

Host <server alias>
    # comment about server
    HostName <server name>
    User <USERNAME>
    ProxyCommand ssh tu-bastion-ex nc %h %p 2> /dev/null
```

### Step 3. Check that your local machine’s `known_hosts` file contains the SSH key for the tu-bastion-ex host 

Back in your .ssh folder, use the `cat` command to display the contents of the known_hosts file. 

`username@localmachine .ssh % cat known_hosts`

The output will look something like this:

``` 
linux-bastion-ex.tudelft.nl,131.180.123.197 ssh-rsa <your ssh key - this will be a lot of numbers followed by your email address.>
```

### Step 4. Generate SSH key pair to store on local machine 
*Note:* if you already have an SSH key pair from another application, you can use this existing one

In your .ssh folder, type the following command:

`username@localmachine .ssh % ssh-keygen -t rsa -C <youremailaddress@tudelft.nl>`

You will see output in your terminal that looks like the text below. It will ask for your input in certain fields, including a filename (here we use id_rsa) and passphrase. 
```
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/username/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/username/.ssh/id_rsa.
Your public key has been saved in /Users/username/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:d90YAdXNXA5x8eolImyTF6B1ajUarxuv94a+4zbc0 youremailaddress@tudelft.nl
```
Check to see that the SSH key files are stored on your local machine using the `ls` command in the .ssh folder.

`username@localmachine .ssh % ls`

### Step 5. Copy your public SSH key from your local machine to the Bastion host (tu-bastion-ex)
In the .ssh folder of your local machine, type the following command:

`username@localmachine .ssh % ssh-copy-id tu-bastion-ex`

You will see output that looks like the following. Fill in your password for the Bastion host (provided by ICT) when prompted.

```                 
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: “/Users/username/.ssh/id_rsa.pub”
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed —— if you are prompted now it is to install the new keys
username@linux-bastion-ex.tudelft.nl’s password: 

Number of key(s) added:        1
```

### Step 6. SSH to the Bastion host and check that your public key has been successfully copied

SSH to the Bastion host: 

`username@localmachine .ssh % ssh tu-bastion-ex`

Move into the .ssh directory on the Bastion host and list the files there:

```
[username@bastionhost ~]$ cd .ssh
[username@bastionhost .ssh]$ ls

authorized_keys  config  id_rsa.username  id_rsa.username.pub  known_hosts
```

Check that the `authorized_keys` file contains your SSH key copied from your local machine using the `cat` command:

```
[username@bastionhost .ssh]$ cat authorized_keys
ssh-rsa <your ssh key ending in youremailaddress@tudelft.nl>
```

Exit the Bastion host:

```
[username@bastionhost .ssh]$ exit
Connection to linux-bastion-ex.tudelft.nl closed.
```
	
### Step 7. Copy contents of your public SSH key from your local machine
Navigate to the .ssh folder on your local machine. Use the `cat` command to display the contents of id_rsa.pub (your public SSH key). Copy this SSH key and store in a notepad temporarily - the SSH key includes everything from ssh-rsa to your email address.

```
username@localmachine .ssh % cat id_rsa.pub

ssh-rsa <your ssh key ending in youremailaddress@tudelft.nl>

```

### Step 8. SSH from your local machine to the Bastion host and then to your VPS using its domain name 

```
username@localmachine .ssh % ssh tu-bastion-ex 
[username@bastionhost ~]$ ssh externalserver.nl
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-42-generic x86_64)
```

### Step 9. Paste contents of public SSH key at the end of the `authorized_keys` file on the VPS

Move into the .ssh folder on your VPS:

`username@externalserver: ~ $ cd .ssh`

Open the authorized_keys file using vi:

`username@externalserver: ~/.ssh $ vi authorized_keys`

Paste the contents of your public SSH key copied from your local machine at the end of the file by hitting “o” and ctrl+V.

Exit first the VPS:

`username@externalserver: ~/.ssh $ exit`

and then the Bastion host
 
`[username@bastionhost ~]$ exit`

### Step 10. SSH into your VPS directly from your local machine using its alias

`username@localmachine .ssh % ssh <serveralias>`

## Windows using PuTTY

1. Open Putty
2. Paste <net_id>@linux-bastion-ex.tudelft.nl in the Host name field. An intermediary terminal appears
3. Enter your netID password (it will give you the prompt)
4. Write ssh followed by the full domain name of your server, for example `ssh mgmt-server-lib.tudelft.nl`
5. Congrats! You are in your server
