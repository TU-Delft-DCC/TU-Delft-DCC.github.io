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
title: Mount Project Drive on Server

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Raúl Ortiz Merino
author_2: Maurits Kok

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

## What this documentation will help achieve
Project drive storage from TU Delft ICT can be mounted and made accessible in your (TU Delft) Virtual Private Server.

## Prerequisites
- A (TU Delft) [Virtual Private Server](../infrastructure/VPS_request.md)
- (TU Delft) [Project Drive](./project_drive_request.md)

## Steps
1. Locate the URL of your project storage
1. Connect to your TU Delft VPS via SSH
1. Create a new directory as a mounting point
1. Retrieve your Linux user and group details
1. Edit the fstab file to include project storage technical details
1. Mount the project drive

### Step 1. Locate the URL of your project storage
The URL for your project drive can be obtained from either 
- the email from TU Delft ICT with the confirmation of your project drive request, or 
- by navigating to https://webdata.tudelft.nl/, and then through **WebDav Web Links > Staff-Umbrella > "Enter your netID and password"** to retrieve a list of your project drives. 

Copy everything after "https://webdata.tudelft.nl/" (this will be staff-umbrella/`<your_project_name>`)

### Step 2. Connect to your TU Delft VPS via SSH 
Follow instructions in TU Delft ICT email from initial server setup or [configure a 1-step connection via SSH](../infrastructure/VPS_SSH.md).

### Step 3. Create a new directory as the mounting point
The convention is to create mounting points in the folder `/media`. Navigate to the folder and create a new folder with

```bash
cd /media
mkdir <server_mount_point>
```
Replace `<server_mount_point>` with the name of your choice. This will be the name of the folder where your project drive will be mounted.

### Step 4. Find and save your user and group details

In the terminal, you can retrieve your local user and group details with:

```bash
id -u <your_netID> # User ID
id -g <your_netID> # Group ID
```

You may need the values for `uid` and `gid` for step 5.

:::{.callout-note}
These commands are server-specific, so make sure to execute them on the server where the project drives will be mounted.
:::

### Step 5. Edit the fstab file to include project storage technical details
The fstab file containes a list of the addresses of external file systems. In this file, the details of your project drive will need to be added in a single line. This line consists of four parts: 
1. *filesystem* - the address of the project drive
2. *mount point* - the location in the VPS where you want to mount the project drive
3. *type* - the type of the filesystem
4. *options* - additional option such as user privileges


The fstab file must be in the `/etc/` directory and can be opened with the `vi` or `nano` editor:

::: {.panel-tabset}

### vi

In the terminal, enter the following command to open the fstab file in the vi editor:  
`sudo vi /etc/fstab`  
Then, switch to the insert mode (hit "i" to switch to insert mode and be able to type)


### nano
In the terminal, enter the following command to open the fstab file in the nano editor:  
`sudo nano /etc/fstab`

:::

Add the following line to the file:

```bash
<your_netID>@sftp.tudelft.nl:/staff-umbrella/<project_drive_name>  /media/<server_mount_point> fuse.sshfs  rw,noauto,users,_netdev  0  0
```

replacing the values between `<` and `>` with your NetID, the name of your project drive, and the name of the folder you created in step 3.

:::{.callout-note}

If this configuration throws a permission error during mounting, try: 

```bash
//tudelft.net/staff-umbrella/<project_drive_name>/ /media/<server_mount_point> cifs username=<your_netID>,noauto,uid=<your_uid>,gid=<your_gid>,forcegid,rw,_netdev

```
Use the values for `uid` and `gid` from step 4.
:::

Close the file editor and save the changes:

::: {.panel-tabset}

### vi

Use `Control`+`C` followed by `:wq` to save the file and close it to get back to your terminal.

### nano

As indicated by the nano interface, use `Control`+`O` to write the file. Then, confirm your choice of filename by hitting `enter`. Finally, exit the file with `Control`+`X`

:::

### Step 6. Mount the project drive
To mount the project drive execute the command

```bash
sudo mount /media/<server_mount_point>
```

You can also unmount the drive with
```bash
fusermount -u /media/<server_mount_point>
```

The project drive will not mount automatically, so you will need to remount it manually each time you restart the server.

:::{.callout-note}
If the step above does not work, it probably means that the packages for mounting cifs-type filesystems haven't been installed. Depending on your linux flavour you will need to install them using:

::: {.panel-tabset}
### Ubuntu/Debian
`sudo apt install cifs-utils`

### Redhat/Centos/Fedora  
`sudo yum install cifs-utils`
:::
:::

## Notes and next steps
The steps above can also be used to mount any storage offered by TU Delft with a WebDav link (staff-homes, staff-groups, staff-bulk, student-homes, student-groups and apps). Simply use the latter half of the URL from the WebDav web link of your storage drive, which will change from staff-umbrella (project drive) to something else depending on the storage drive you would like to mount.
