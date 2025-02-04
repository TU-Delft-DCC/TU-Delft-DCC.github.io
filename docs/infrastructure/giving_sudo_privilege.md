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
title: Giving sudo privilege to a user

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

## Background

There are some tasks in Linux that requires superuser (sudo) permission. For instance editing the /etc/fstab file, rebooting the system, mounting a drive, viewing /etc/passwd file and many other tasks cannot be done without sudo privilege. 

## What this documentation will help achieve
This documentation helps you to give sudo privilege to a user. 

## Prerequisites
* TU Delft netID
* Basic knowledge of Linux 
* Those who grant sudo permission need to have sudo permission themselves.

## Tools/Software
* For Windows users, you will need a programming and runtime environment like Cygwin or SSH client like PuTTY in order to access the VPS running Linux.



## Steps
1. Getting the username(s) of sudo access candidates
2. Navigating to the **sudoers** directory
3. Create an access file for each of the candidates
4. Editing the access files


### Step 1. Getting the username(s) of sudo access candidates
You can get the usernames by checking the `/etc/passwd` file. This file contains all the usernames and their login information.  


### Step 2. Navigating to the **sudoers** directory
The list of users who posses the sudo permission is in the `/etc/sudoers.d/` folder, so navigate to that folder.

### Step 3. Create an access file for each of the candidates
If you use `ls` command to check the available files in this folder, you can see there are some files that their name start with a number and then a dash and then a user name (`<number>-<username>`).  In Linux for every user with a sudo permission, there is a file like that, so we duplicate one of the existing files and rename them for each of the sudo candidates (in fact, name of those file doesn't matter; however, it helps us to understand which users have sudo privilege without opening them). 

### Step 4. Editing the access files
In this step you need to open each of the newly duplicated files and replace the old username in the second line with the sudo candidate username. After the edit, you just save the changes and exit the file.
