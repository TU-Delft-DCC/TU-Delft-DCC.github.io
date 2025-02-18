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
title: Creating GitLab groups

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
Groups and subgroups are similar to directories in the operating systems. In windows or Mac, we create directories to organise files or other directories. For example, imagine a scenario where you want to keep your photos in an organised manner. To this end, you may organise your photos on multiple levels. In the first level, perhaps you broadly classify them and then in the next levels you narrow it down to more specific subjects. Similarly, in the GitLab, a group is used as a binder to put together projects or even other groups. For example, if three themes are researched in a lab, each of those themes could be a group, and all the research in a certain theme fall into its corresponding group. Sometimes there are also sub-themes. For every sub-theme you can create a subgroup (within the group corresponding to the broader theme) and assign the research close to the sub-theme there. 


## What this documentation will help achieve
This documentation helps researchers to set up a group and assign contributors to the projects within the GitLab. 


## Prerequisites
* TU Delft netID


## Steps
1. Log-in to the GitLab with your netid and password.
2. Enter to the _Groups_ section.
3. Create a group.
4. Assign contributors to the group.


### Step 1. Log-in to the GitLab with your netid and password
To create a group in GitLab, first you need to log in to the [TU Delft's instance of GitLab](https://gitlab.tudelft.nl/). 

![AA](https://user-images.githubusercontent.com/70349945/125589301-b69555cd-2e96-455c-b129-4ba155d44685.png)
*Figure 1: The login page of TU Delft’s GitLab.*


### Step 2. Enter to the _Groups_ section
After the log-in, from the top bar click on groups and then Your groups. I

![BB](https://user-images.githubusercontent.com/70349945/125589314-e173ad4c-f607-4ff5-8886-d2a80cd6eecb.png)
*Figure 2: The Group section of the GitLab.* 

### Step 3. Create a group
In the new web page, click on the New group and then fill in the form by choosing a suitable group name and then selecting the visibility level. You can later on change both group name and visibility level.  

![CC](https://user-images.githubusercontent.com/70349945/125589330-26e7788a-fdf8-4b99-a1d8-00e3e4f0344e.png)
*Figure 3: Creation of a new Group in the GitLab.* 


### Step 4. Assign contributors to the group.
After creating a group, it appears in the Groups tab. The group owner can add different people to the projects. This can be done by entering a project and then clicking on the Members on the left panel and filling in the form (Figure 4). A very important part of this form is permissions which are explained here in detail. 

![DD](https://user-images.githubusercontent.com/70349945/125589349-c1e84563-4578-421c-8535-f16cd7732825.png)
*Figure 4: Assigning members to a project.*


You can also create subgroups within a group. To create a subgroup, you need to enter an existing group and press the New subgroup button. Then, similar to creating a group, you fill in the subgroup name and select the degree of visibility for the subgroup. The subgroup visibility level is always a subset of its (parent) group visibility, hence if the parent visibility is private, there is no choice except private for the subgroup visibility but if the parent visibility is public, subgroup visibility could be either public, internal, or private. The same logic applies when you create a subgroup within another subgroup. 

![image](https://user-images.githubusercontent.com/70349945/125596041-94a273ab-8685-4231-bbdf-1bbc42580acc.png)
*Figure 5: Creating a subgroup.*


After setting up the group, (sub groups,) projects, and assigning the collaborators to the projects, they can start working with the remote repository and transfer their scripts there. 
