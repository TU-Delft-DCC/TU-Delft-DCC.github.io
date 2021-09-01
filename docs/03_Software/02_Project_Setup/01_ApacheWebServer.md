# Deploy Apache Web Server

## Background
Apache Web Server is a software package that turns a computer into an HTTP server. That is, it sends web pages – stored as HTML files – to people on the internet who request them. It is open-source software, which means it can be used and modified freely.

## What this documentation will help achieve
This guide will help you install the Apache web server on Ubuntu Linux 18.04 and configure a HTTPS secure connection for all incoming web traffic.

The steps outlined below will ensure that all incoming web traffic to your server from port 80 (HTTP) will be redirected to port 443 (HTTPS). Port 80 is still accessible but redirects automatically. Redirection is configured after the SSL certificate is in place. 

## Prerequisites
* A system running Ubuntu 18.04 LTS (Bionic Beaver)
* An internet connection
* Access to a user account with sudo privileges

## Tools / Software
* A command-line utility (Use keyboard shortcut CTRL-ALT-T, or right-click the desktop and left-click Open Terminal)
* A firewall – the default UFW (Uncomplicated Firewall) in Ubuntu is fine
* The APT package manager, installed by default on Ubuntu

## Steps
1. Request a Virtual Private Server (VPS) from TU Delft ICT
2. Install Apache web server on the VPS
3. Request an SSL certificate from TU Delft ICT
5. Configure the SSL certificate file on your VPS 
6. Redirect all incoming web traffic to HTTPS

### Step 1. Request a Virtual Private Server from TU Delft ICT

You can make a request for a server via the [TopDesk self service portal](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34). If you would like more information, documentation can be found here ___

*Note:* to run a web server, ports 80 (HTTP) and 443 (HTTPS) must be opened.

### Step 2. Install Apache web server on the VPS 
[Apache](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview) is an open source web server that’s available for Linux servers. It is one of the most commonly used softwares for creating a web server. And, it's free!

[Installing Apache](https://phoenixnap.com/kb/how-to-install-apache-web-server-on-ubuntu-18-04) can be done using commands in the terminal. These instructions are documented with further information at the link in the beginning of this paragraph. First, make sure your local software packages are up to date by running:

`sudo apt-get update`

When that has finished, install the Apache package using:
 
`sudo apt-get install apache2`

The system prompts for confirmation – do so, and allow the system to complete the installation.

Find the IP address of your VPS by running:

`hostname -I | awk '{print $1}'`

Use this IP address to enter the following command in your terminal, replacing local.server.ip with the actual IP address of your server:

`http://local.server.ip`

If the installation was completed successfully, you should see the Apache2 Ubuntu Default page in your web browser. 

Although the Apache installation process is complete, there is one more additional step. Configure the default UFW firewall to allow traffic on port 80.

Start by displaying available app profiles on UFW:

`sudo ufw show app list`

Use the following command to allow normal web traffic on port 80:

`sudo ufw allow 'Apache Full'`

Verify the changes by checking UFW status:

`sudo ufw status`

At this point, your Apache web server is serving over HTTP, which is a good first step! But remember, we need to secure the connection over HTTPS. So, we still have a few more steps.

### Step 3. Request an SSL certificate from TU Delft ICT
Detailed directions on how to do this can be found here ___

You can create the .csr file directly on the VPS by first create a directory on /etc/apache2 called ssl:

`mkdir /etc/apache2/ssl`

Then, generate a CSR and private key using:

`openssl req -x509 -newkey rsa:4096 -keyout <server_domain>.key -out <server_domain>.csr -nodes`

After successfully running the command it will ask for the information of certificate request. Complete it using the appropriate information and then <server_domain>.key and <server_domain>.csr files will be generated.

The .csr file must be sent to TU Delft ICT using this TopDesk form: [TOPdesk SSL certificate server request](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=62aeef08314247f3aba7ff2297d011da). 

### Step 4. Configure the SSL certificate on your VPS 

When you receive SSL certificate files from the signing authority via TU Delft ICT, you need to put the information from this certificate in a specific place on your VPS in order to securely expose the web server. These instructions come from here: - [Configure ssl for https](https://hostadvice.com/how-to/configure-apache-with-tls-ssl-certificate-on-ubuntu-18/) 

Navigate to the default Apache site config directory using the following command:

`sudo nano /etc/apache2/sites-available/default-ssl.conf`

This config file tells the server where to find SSL certificate. It should look like this:

                <IfModule mod_ssl.c>
                <VirtualHost _default_:443>
                ServerAdmin webmaster@localhost

                DocumentRoot /var/www/html

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                SSLEngine on

                SSLCertificateFile    /etc/ssl/certs/ssl-cert-snakeoil.pem
                SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key

                <FilesMatch ".(cgi|shtml|phtml|php)$">
                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                SSLOptions +StdEnvVars
                </Directory>

                </VirtualHost>
                </IfModule>

Edit this: `ServerAdmin webmaster@localhost` to this: `ServerAdmin email@example.net`

Add this right below the ServerAdmin line:

                ServerName ADD_YOUR_IP_OR_DOMAIN_NAME_HERE

Now, edit these lines with our certificate location:

                SSLCertificateFile    /etc/apache2/ssl/apache.crt
                SSLCertificateKeyFile /etc/apache2/ssl/apache.key


Our file should look like this:

                <IfModule mod_ssl.c>
                <VirtualHost _default_:443>
                ServerAdmin email@example.net
                ServerName 203.0.113.122

                DocumentRoot /var/www/html

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                SSLEngine on

                SSLCertificateFile    /etc/apache2/ssl/apache.crt
                SSLCertificateKeyFile /etc/apache2/ssl/apache.key

                <FilesMatch ".(cgi|shtml|phtml|php)$">
                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                SSLOptions +StdEnvVars
                </Directory>

                </VirtualHost>
                </IfModule>

**Save the file**, and close it.

*Note: If you are using something other than Apache Web Server (like, nginx for example) you can also create the SSL config file from scratch. Each application will have different syntax that should be used in this file. You can see how the syntax is set up by using [this tool](https://ssl-config.mozilla.org/#server=apache&version=2.4.41&config=intermediate&openssl=1.1.1d&guideline=5.6)*

Enable the SSL module using following command:

`sudo a2enmod ssl`

Now enable the site we have just edited:

`sudo a2ensite default-ssl.conf`

Restart Apache:

`sudo service apache2 restart`

The website is now secure, access it using following address in the browser

`https://YOUR_SERVER_IP`


### Step 5. Redirect all incoming web traffic to HTTPS

`sudo a2enmod proxy`

`sudo a2enmod proxy_http`

`sudo a2enmod rewrite`

Add in apache conf:

                ProxyPass /thredds http://localhost:8080/thredds
                ProxyPassReverse /thredds http://localhost:8080/thredds
                RedirectMatch ^/$ /thredds/

## Notes and Next Steps
Test that your web server is secured by HTTPS by typing the Fully Qualified Domain Name (FQDN) of your server in a web browser. If HTTPS is enabled, the URL should begin with it - if it still says HTTP, something will need to be reconfigured.
