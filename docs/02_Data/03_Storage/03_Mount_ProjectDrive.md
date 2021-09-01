# Mount Project Drive on Server

## Background

## What this documentation will help achieve
Project drive storage from TU Delft ICT can be mounted and made accessible in your (TU Delft) Virtual Private Server.

## Prerequisites
A (TU Delft) Virtual Private Server and a (TU Delft) project drive

## Tools/Software

## Steps
1. Connect to your TU Delft VPS via SSH
2. Think of a mount point and create a new directory for it (It is a convention to mount external drives into /media) 
3. Find your user ID (uid) and group ID (gid)
4. Locate the URL of your project storage
5.  Open the fstab file 
6. Edit the fstab file to include project storage technical details
7. Save the fstab file
8. Mounting the project drive

### Step 1. Connect to your TU Delft VPS via SSH 
Follow instructions in TU Delft ICT email from initial server setup or configure 1-step connection via SSH here _____

### Step 2. Create a new directory as the mounting point preferably in /media 
This is where you will mount the project drive. Use `cd /media` to enter the media directory, and `mkdir <yourprojectname>` to create a new directory where the TU Delft project drive will be mounted.

### Step 3. Find your user ID (uid) and group ID (gid)
This can be accomplished by the linux command `id` which should output both your user and group ids in your terminal. Alternatively, you can open /etc/passwd file by typing `sudo vi /etc/passwd` and scroll down until you see your netid. It will be followed by an `:x:` and some numbers separated by ':'. The first number is your uid, the second number is your gid. Copy and paste or record these numbers for use in a later step. Exit the vi editor by Control+C, then `:qa` and Enter.

### Step 4 Locate the URL of your project storage
This can be found either in the email from TU Delft ICT confirming project drive storage setup, or by going to https://webdata.tudelft.nl/, and then WebDav Web Links > Staff-Umbrella > Enter your netID and password > "Your Project Name". Copy everything after "https://webdata.tudelft.nl/" (this will be staff-umbrella/yourprojectname)

### Step 5. Open the fstab file 
The fstab file is where you can list the addresses of external file systems you want to mount) which is also in the /etc/ directory by typing `sudo vi fstab`. The fstab file must be in the /etc/ directory.

### Step 6. Edit the fstab file to include project storage technical details

Basically you need to add one line to this file. This line consists of four parts: (i) filesystem, (ii) mount point, (iii) type, and (iv) options. The filesystem refers to the project drive address which is specified in the ICT email. The mount point is where you want to mount the project drive in the VPS. The third part determines the type of the filesystem and in the last part you specify some options such as privileges. 

To add the filesystem, open the /etc/fstab file with the sudo privilage and switch to the insert mode (hit "i" to switch to insert mode and be able to type), and write `//tudelft.net/` and paste the latter half of the URL you copied from the WebDav links. The full URL should be in this format: //tudelft.net/staff-umbrella/yourprojectname. 

For the mount point, add a space followed by the location in your VPS where you want to mount the Project Drive storage (where you created the folder previously, e.g., `/media/yourprojectname` ).

The next component is the type of the filesystem, so add a space followed by the type of file system: `cifs`

After the filesystem type, the next component is the options. Different options are separated via a comma, so first add a space followed by the options: `username=<yournetid>`, `noauto`, `uid=<your_uid>,gid=<your_gid>`, `forcegid,rw,_netdev`

Make sure to replace <your_uid> and <your_gid> with the numbers you recorded in step 3. 

More specifically in this part, you determine which user and group can mount and get access to the project drive. It is highly recommended to read this file in order to fully understand what each element of every line in the /etc/fstab means. 

The full new record in the fstab file should be formatted like this: 

![fstab add example](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/uploads/9d3e9cc63f170665d486b541d531c8a1/Screenshot_2021-04-08_at_15.28.28.png)

### Step 7. Save the fstab file
Use Control+C followed by `:wq` to save the file and close it to get back to your terminal.

### Step 8. Mounting the project drive
To mount the project drive you use `sudo mount <mount_point>` command. You can also unmount it using `sudo umount <mount_point>`.


## Notes and next steps
The project drive will not mount automatically, so you will need to mount it manually each time you start the server. To do so, from the home (`/`) directory in your server run `sudo mount /media/yourprojectname`. You should now be able to `cd /media/projectname` and view your files stored on the project drive using `ls`.

Note, if the step above does not work, it probably means that the packages for mounting cifs-type filesystems haven't been installed. Depending on your linux flavour you will need to install them first using:

`sudo apt install cifs-utils`

on ubuntu/debian like linuxes, or

`sudo yum install cifs-utils`

on redhat/centos/fedora flavours.

The steps above can also be used to mount any storage offered by TU Delft with a WebDav link (staff-homes, staff-groups, staff-bulk, student-homes, student-groups and apps). Simply use the latter half of the URL from the WebDav web link of your storage drive (step 5), which will change from staff-umbrella (project drive) to something else depending on the storage drive you would like to mount.

