# Request a Virtual Private Server

## Background
This page describes the essentials for requesting and setting up a TU Delft managed server. A server is a computer that can handle requests. Servers are often a critical component of architectural solutions for data management. There are many reasons why you as a researcher may need to request a server, for example:
* Automation of a process in your data collection
* A part of your analysis should be running continuously, and you cannot do it with your machine 
* Specific functionality (web server)
* You need a machine to handle large amounts of requests 
* You want to outsource the maintenance of the server to TU Delft ICT
* Rely on safety and security administrated by the University
* Securing/controlling access
* Mounting storage drive

## What this documentation will help achieve
This documentation helps researchers to request a VPS and data storage on the Project Drive. There are other forms of storage available, (see here _____) but Project Drive storage is often recommended for expandable and secure data preservation.

## Prerequisites
* TU Delft netID
* Basic knowledge of Linux (if requesting Linux server, recommended)

## Tools/Software
* For Windows users, you will need a programming and runtime environment like Cygwin or SSH client like PuTTY in order to access the VPS running Linux

## Steps
1. Navigate to the TU Delft server request form
2. Fill and send the form according to your preferences and needs
3. Receive confirmation of server deployment from TU Delft ICT 
4. Login to your server for the first time

### Step 1: Navigate to the TU Delft server request form
You can make a request for a server via the [TopDesk self service portal](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34).

### Step 2: Fill and send the form according to your preferences and needs
The form is divided into three sections: **Caller Details**, **General Questions**, and **Technical Questions**.

**Caller Details** should contain the contact information of the main administrator of this server. If you select your name, the fields below should be auto-populated with your building, phone number, email, department/program, organizational unit, and (sometimes) room. 

<img width="547" alt="MicrosoftTeams-image" src="https://user-images.githubusercontent.com/70262847/124608876-65778580-de6f-11eb-9c45-edd730417203.png">

The last question in the **Caller Details** section refers to access to the server by external users. Generally speaking, granting access to TU Delft-managed servers is not recommended, but if it is necessary there is an option to add the contact details of the external party and the reason(s) for which they should have access. You will need to provide a company-affiliated email address for the external user, and the request may or may not be granted by ICT. **Note:** Keep in mind that this access is to the backend of things, so if for example you want to deploy a web server to share your data widely, users **do not** need direct access to the server in order to access the data itself.

________

The next section contains **General Questions** about the name and purpose of your server. In the field of "Expiration Date," if you plan to use this server ongoing into the future, you can either leave the field blank or add a date in 10+ years. TU Delft ICT should alert you when the expiration date you select is near. 

![436ab820-8194-4212-8622-93758ba56f56](https://user-images.githubusercontent.com/70262847/124609178-b1c2c580-de6f-11eb-8e33-0dfcbf79226e.jpg)

Here you can also add the netIDs of your collaborators who should have read/write access to the server, as well as the netID of your faculty Data Steward if you would like their help (optional). You can find your faculty Data Steward contact information [here](https://www.tudelft.nl/en/library/current-topics/research-data-management/r/support/data-stewardship/contact/).

____________

The **Technical Questions** section asks you to specify an operating system and some other technical details about your server configuration. You can choose between four basic configuration options - you can of course consider which one best fits your needs. If you are new to working with servers, probably the best choice is Basic configuration 4.

The next question deals with opening ports to the server through the TU Delft firewall. Ports are essentially gateways to the server that are specific to different purposes. For example, port 80 is opened to handle HTTP requests, port 20 is opened to handle SSH requests, port 3306 is opened to allow access to a MySQL database, and port 443 is opened to handle HTTPS requests. If you are planning to use your VPS as a webserver, ports 80 and 443 should be open. You can use this space to ask ICT to do so. 

The next section, FQDN, is the way you can refer to your server on the internet. The recommendation is a format like `<servername>.<facultyabbreviation>.tudelt.nl`. In general, it's best to keep names relatively short and informative to make it easy to reference and remember.

You should also be sure to check the instructions in the form and contact your faculty [Data Steward](https://www.tudelft.nl/en/library/current-topics/research-data-management/r/support/data-stewardship/contact/) if you need further explanation.

## Initial Configuration of your VPS
A few days after submitting the request, you will receive an email from ICT with login details. You can connect to your VPS via ssh. If you are in the windows environment, it is recommended to install Cygwin and its packages to be able to use the ssh command in a non-unix environment. The unix based systems (e.g., mac) contain ssh by default. In order to login to your VPS, you need to first ssh to the bastion server (ssh <username>@linux-bastion-ex.tudelft.nl) and then from there login to your server (ssh <servername>). The first thing to do after logging into the server is to update the packages:

(For Debian distributions such as Ubuntu)
`sudo apt update`
`sudo apt upgrade`


(For RedHat distributions)
`sudo yum update`

It would be also useful to set a password for the VPS when you log in. You can do that by passwd command. 


## Next Steps
Common next steps after obtaining a VPS and storage include initial configuration steps like establishing a connection via SSH and mounting Project Drive storage; and also software installation steps for tools like Docker, and setting up Apache Web Server. We will add more documentation when common installations come to our attention, so please reach out to dcc@tudelft.nl with questions or suggestions. 
- [Install Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04)
- [Configure Docker for use as non-root](https://docs.docker.com/engine/install/linux-postinstall/)
- [Apache Web Server](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/Setting-up-an-Apache-Server)
- [Configuring VM connection via SSH](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/Configuring-VM-Connection). 