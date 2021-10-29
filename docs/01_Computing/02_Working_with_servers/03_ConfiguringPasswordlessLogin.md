# Configuring passwordless login

## Background

In general, when you ssh to your server, it asks you to enter your password. This process benefits symmetric encryption. There is another way to secure the access to the digital systems which is called asymmetric encryption. Let's elaborate each of those encryption methods. In the symmetric encryption, we use a key (or an algorithm or password) that can be used for both encryption and decryption of a message:

![first4](https://user-images.githubusercontent.com/70349945/124941824-63e2c480-e00b-11eb-89ac-f32532255442.png)

But in the asymmetric encryption, a key pair is generated where one of them is used for the encryption and the other one for the decryption. More precisely, when a message is encrypted with one of the keys in the pair, it can only be decrypted with the other key in the same pair. 

![second](https://user-images.githubusercontent.com/70349945/124941057-c9828100-e00a-11eb-8f9b-7fe73f56ecc8.png)

This means if individuals keep the decryption key (private/secret key) in a secure place and share the public key openly, then they would be able to use the public key of the recipient to encrypt the message (and since no one except the private key holder can decrypt the message), and send it without concern regarding the disclosure of the message content. In linux, the same mechanism enables us to log in into the server without entering the password.

In general when we ssh to a server for the first time, it returns a message containing the server fingerprint. We can verify the fingerprint with where we got the server to see whether we are connecting to the intended server or not. (After confirming the fingerprint ~/.ssh/authorized_keys file is created which contains the information of the server.). After the verification step, we need to enter the password of the server and by entering the correct password we connect to the server. But using password is not straightforward and also if we want to ssh to the server in the middle of a script, we should hard-code the server password which is not a secure practise whatsoever. To tackle this issue, we use a key pair.

## What this documentation will help achieve
It helps to set up a password-less login to the VPS over SSH.

## Prerequisites
VPS provided by TU Delft ICT.

## Tools/Software
If using Windows, PuTTY or cygwin.

## Steps
Step1. Generate the key-pair.
Step2. Transfer the public key to the VPS.

### Step 1. Generate the key-pair.
Use `ssh-keygen` command to generate a key pair. The keys are created in ~/.ssh/ path.

### Step2. Transfer the public key to the VPS.
Use `ssh-copy-id <server-address>` command to transfer the public key to the server. 
