# Sync with Unison

## Background

From Unison website: "Unison is a file-synchronization tool for OSX, Unix, and Windows. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other." 

## What this documentation will help achieve
This documentation will help you create bi-directional backups between your local machine and a server (such as TU Delft project drive). Sync profiles can be customized so that, for example, shared folders on SurfDrive can be automatically synced with directories in the WebDAV links for TU Delft Staff and Students.

![Untitled_Document32](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/635e3939d32a78f12d693351fb910adb/Untitled_Document32.png)

## Prerequisites

## Tools/Software
* Unison
* GTK+ for Windows
* Desktop client for SURFDrive

# Steps for Windows
1. Unison requires .dll's from GTK+ for Windows Runtime Environment. Download it (from https://sourceforge.net/projects/gtk-win/) and install it (to C:\Program Files (x86)\GTK2-Runtime).
2. Install Unison 2.48.4 (from https://www.irif.fr/~vouillon/unison/) and extract it in a folder.
3. Download desktop client for SurfDrive https://www.surf.nl/en/surfdrive-store-and-share-your-files-securely-in-the-cloud/downloads-for-surfdrive?dst=n1463
4. If not already there, mount H: Drive or Project Drive folder in your local machine from WebDAV link https://webdav.io/webdav/webdav-clients/ 
5. Navigate to Unison folder via command prompt and then enter "unison 2.48.4 GTK.exe" to run the Unison GUI.
6. The GUI starts & asks you to set a Profile for your file syncing. The Profile Creation Wizard guides you through this. For the Synchronization kind choose Local. Set the First directory to your local SurfDrive and Second directory, to WebDAV folder. 
7. By pressing the Go button on the top menu, Unison start synchronizing both specified directories. 

# Steps for Mac (beta)
These steps should theoretically be feasible, but there is an issue with the configuration of mounted TU Delft drives and them disconnecting which interrupts automated backup and read/write access. We are working on this with TU Delft ICT.

1. Install Unison https://www.cis.upenn.edu/~bcpierce/unison/
2. Download desktop client for SurfDrive https://www.surf.nl/en/surfdrive-store-and-share-your-files-securely-in-the-cloud/downloads-for-surfdrive?dst=n1463
3. Mount H: drive or Project Drive folder in your local machine using these directions: https://help.dreamhost.com/hc/en-us/articles/216473527-Accessing-WebDAV-with-Mac-OS-X-and-Linux
4. Choose folders for sync from local machine or Surfdrive to WebDAV folder

