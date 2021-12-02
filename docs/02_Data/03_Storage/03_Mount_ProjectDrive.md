# Mount Project Drive on Server

## Background

## What this documentation will help achieve
Project drive storage from TU Delft ICT can be mounted and made accessible in your (TU Delft) Virtual Private Server.

## Prerequisites
A (TU Delft) Virtual Private Server and space on the (TU Delft) Project Drive

## Steps
1. Connect to your TU Delft VPS via SSH
2. Think of a mount point and create a new directory for it (It is a convention to mount external drives into /media) 
3. Locate the URL of your project storage
4.  Open the fstab file 
5. Edit the fstab file to include project storage technical details
6. Save the fstab file
7. Mounting the project drive

### Step 1. Connect to your TU Delft VPS via SSH 
Follow instructions in TU Delft ICT email from initial server setup or configure 1-step connection via SSH.

### Step 2. Create a new directory as the mounting point preferably in /media 
This is where you will mount the project drive. Use `cd /media` to enter the media directory, and `mkdir <yourprojectname>` to create a new directory where the TU Delft project drive will be mounted.

### Step 3. Locate the URL of your project storage
This can be found either in the email from TU Delft ICT confirming project drive storage setup, or by going to https://webdata.tudelft.nl/, and then WebDav Web Links > Staff-Umbrella > Enter your netID and password > "Your Project Name". Copy everything after "https://webdata.tudelft.nl/" (this will be staff-umbrella/yourprojectname)

### Step 4. Open the fstab file 
The fstab file is where you can list the addresses of external file systems you want to mount. Find it in the /etc/ directory by typing `sudo vi fstab`. The fstab file must be in the /etc/ directory.

### Step 5. Edit the fstab file to include project storage technical details

Basically you need to add one line to this file. This line consists of four parts: (i) filesystem, (ii) mount point, (iii) type, and (iv) options. The filesystem refers to the project drive address which is specified in the ICT email. The mount point is where you want to mount the project drive in the VPS. The third part determines the type of the filesystem and in the last part you specify some options such as privileges. 

To add the filesystem, open the /etc/fstab file with the sudo privilage and switch to the insert mode (hit "i" to switch to insert mode and be able to type), and write `//tudelft.net/` and paste the latter half of the URL you copied from the WebDav links. The full URL should be in this format: //tudelft.net/staff-umbrella/yourprojectname. 

For the mount point, add a space followed by the location in your VPS where you want to mount the Project Drive storage (where you created the folder previously, e.g., `/media/<server_mount_point>` ).

The full new record in the fstab file should be formatted like this: 

```
<your_netID>@sftp.tudelft.nl:/staff-umbrella/<Project_Drive_space>  /media/<server_mount_point> fuse.sshfs  rw,noauto,users,_netdev  0  0
```
If that throws a permissions error, try: 

```
//tudelft.net/staff-umbrella/ODCOR/ /media/odcor cifs username=acryan,noauto,uid=549192,gid=5004,forcegid,rw,_netdev
```

### Step 6. Save the fstab file
Use Control+C followed by `:wq` to save the file and close it to get back to your terminal.

### Step 7. Mounting the project drive
To mount the project drive use the `sudo mount /media/<server_mount_point>` command. You can also unmount it using `fusermount -u /media/<server_mount_point>`.

## Notes and next steps
The project drive will not mount automatically, so you will need to mount it manually each time you start the server. To do so, from the home (`/`) directory in your server run `mount /media/<server_mount_point>`. You should now be able to `cd /media/<server_mount_point>` and view your files stored on the project drive using `ls`.

Note, if the step above does not work, it probably means that the packages for mounting cifs-type filesystems haven't been installed. Depending on your linux flavour you will need to install them first using:

`sudo apt install cifs-utils`

on ubuntu/debian like linuxes, or

`sudo yum install cifs-utils`

on redhat/centos/fedora flavours.

The steps above can also be used to mount any storage offered by TU Delft with a WebDav link (staff-homes, staff-groups, staff-bulk, student-homes, student-groups and apps). Simply use the latter half of the URL from the WebDav web link of your storage drive (step 5), which will change from staff-umbrella (project drive) to something else depending on the storage drive you would like to mount.

