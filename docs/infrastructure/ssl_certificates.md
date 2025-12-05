---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-12-02

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-12-02

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Configure SSL/TLS certificates

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
description: Requesting and configuring SSL certificates on TU Delft VPS
hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Manuel G. Garcia
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Manuel G. Garcia
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Manuel G. Garcia

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - Infrastructure
 - Servers
 - VPS
 - Cybersecurity

---

In web servers, SSL/TLS certificates are used to encrypt the communication between a web server and the client (e.g. web browser). In a web server, this is what makes it possible to have HTTPS connections instead of HTTP connections. HTTPS connections are secure, meaning that the data exchanged between the server and the client is encrypted and cannot be intercepted or read by third parties.
In order to do this, you need an SSL certificate from a certificate signing authority.

When a webserver certificate is expired or invalid, a web browser will show you a warning saying it is risky to access a website. This is because the browser cannot verify the identity of the web server, and therefore cannot ensure that the connection is secure. If you are a website owner, it is important to ensure that your SSL certificate is valid and up-to-date to avoid these warnings and maintain the trust of your users. 

This guide shows how to request and prepare an SSL/TLS certificate from HARICA, a Certification Authority trusted by TU Delft ICT. TU Delft staff can request SSL/TLS certificates using the **Academic login** option on the [HARICA website](https://cm.harica.gr/Login). You can opt to use [Let's Encrypt](https://letsencrypt.org/how-it-works/) certificates via Certbot instead, which also provides free SSL certificates, but these certificates need to be renewed every 90 days. The HARICA certificates are valid for up to one year.

:::{.callout-warning appearance="simple" icon="false"}
## {{< fa exclamation-circle >}}  Unsecure connections
Using unsecure HTTP connections can expose sensitive information, such as login credentials and personal data, to potential attackers. It can also make it easier for attackers to intercept and manipulate the data being exchanged between the client and server. Therefore, avoid accessing and deploying websites that do not use HTTPS, especially when transmitting sensitive information. 
:::

## Request Certificate

To request SSL/TLS certificates via HARICA, follow these steps:

1. Log in to the [HARICA website](https://cm.harica.gr/Login) using your TU Delft credentials.
2. Follow the [instructions on the HARICA website to create an SSL certificate](https://guides.harica.gr/docs/Guides/Server-Certificate/Request-for-Domain-Validated-DV/). You need to do so for the qualified domain name associated with your server (e.g. `my-site.tudelft.nl`).

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Private key and passphrase
When creating an SSL/TLS certificate HARICA will prompt you to set **passphrase** and download a private key file. This file is essential for using the SSL/TLS certificate. Ensure that you securely store this private key file and do not forget the passphrase. If either the private key file or the passphrase is lost, you will need to request a new SSL/TLS certificate.
:::

3. Once the new certificates are issued, you will be notified by email. Log in to the HARICA website and download the certificate as a **PEM bundle** file.

### Prepare Certificate on the Server

For configuring the web server, you typically need two specific files: `fullchain.pem` and `privkey.pem` (the private key file you downloaded when requesting the certificate).
You need to upload these files to the server, decrypt the private key file, and place them in the appropriate directory with the correct permissions. The instructions below assume you have a remote server running a Linux-based OS, you have SSH access to it, and have set a [host nickname](./vps_ssh.md#set-up-ssh-tunneling).

1. Rename the PEM bundle file as `fullchain.pem`, and the private key file as `privkey.pem`. The names do not have to be exactly these, but it is a common convention.
2. Upload the new `fullchain.pem` and the `privkey.pem` using `scp` to your home directory on the server. 

    ```bash
    # From the directory where you downloaded the certificate and private key files:
    scp ./fullchain.pem <host-nickname>:~/ 

    scp ./privkey.pem <host-nickname>:~/
    ```

3. Log in to the server via SSH, and check the files have been uploaded correctly:

    ```bash
    ssh <host-nickname>

    ls ~/
    # You should see the files 'fullchain.pem' and 'privkey.pem' listed.
    ```

4. Decrypt the private key file. Before using it on the web server, you need a decrypted copy of it. 

    ```bash
    openssl rsa -in ~/privkey.pem -out ~/decrypted_privkey.pem 
    # You will be prompted to enter the passphrase you set during the initial certificate creation.
    ```

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Encryption algorithms
The command above uses the `openssl rsa` tool to decrypt the private key file. This command works for RSA-encrypted private keys. If your private key uses a different encryption algorithm, consult the OpenSSL documentation. The encryption algorithm is decided when creating the private key during the certificate request. 
:::

5. Copy the certificate and private key files to the appropriate directory for your web server. This is dictated by the web server you are using.

    ```bash
    sudo cp ~/fullchain.pem <web-server-directory>/fullchain.pem
    sudo cp ~/decrypted_privkey.pem <web-server-directory>/privkey.pem
    ```

6. Set the correct permissions for the certificate files. This ensures that only the root user can read the private key file, while the fullchain file can be read by others as needed:

    ```bash
    sudo chown root:maintainers <web-server-directory>/fullchain.pem <web-server-directory>/privkey.pem
    sudo chmod 644 <web-server-directory>/fullchain.pem
    sudo chmod 600 <web-server-directory>/privkey.pem
    ```

7. Configure the webserver to use HTTPS, and restart the web server. The configuration steps depend on the web server you are using (e.g., Apache, Nginx). Consult the documentation for your specific web server for instructions on how to enable HTTPS.

8.  Delete the temporary certificate files and decrypted private key from your home directory to maintain security:

    ```bash
    rm ~/decrypted_privkey.pem  ~/fullchain.pem ~/privkey.pem
    ```

## Renew Certificate

SSL/TLS certificates have a validity period, after which they expire and need to be renewed. HARICA certificates are valid for up to one year. To renew your certificate, you need to follow the same steps as [requesting a new certificate](#request-certificate). Make sure to do this before the current certificate expires to avoid any disruptions in your website's HTTPS availability.

Let's Encrypt certificates, on the other hand, are valid for 90 days. If you are using Let's Encrypt certificates, consider setting up automatic renewal using tools like [Certbot](https://certbot.eff.org/) to ensure your certificates are always up-to-date.


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
- [Domain validation and certificate issuance by Let's Encrypt](https://letsencrypt.org/how-it-works/)
- [SSL secutiry protocol by GeekforGeeks](https://www.geeksforgeeks.org/computer-networks/secure-socket-layer-ssl/)
:::