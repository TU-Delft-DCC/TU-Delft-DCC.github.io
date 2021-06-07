[index](../README.md)

# Winscp
need images!

prerequisites: putty private key ( ppk )

click Session->new->new site

Setting | value
--- | --- 
File protocol | SFTP
Host name | my-vm.tudelft.nl
Port number | 22
Username | netid ( or user on my-vm )

click Advanced->SSH->Authentication

Setting | value
--- | --- 
Private key file | browse for your putty private key file

click __display public key__

click __Copy Key__ and
place this key text in ~/.ssh/authorized_keys on my-vm.

Be sure not to remove other lines in authorized_keys.

click __OK__

### Direct
If direct connection is possible you can skip the tunneled section

### Tunneled
Most VM's are not directly accessible but need to connect through a bastion or proxy.

click Advanced->Connection->tunnel

check __Connect through SSH tunnel__

Setting | value
--- | --- 
host name| mybastion.tudelft.nl (replace with your bastion)
port|22
user name| netid (or user on bastion)
Private key file| [optional] browse for your private key file (ppk) for bastion connection

click __OK__

### Save and test

click __Save__

click __Login__

If you used a bastion notice for which connection the password/passphrase is requested.
Normally the first is for the bastion, the second for my-vm

