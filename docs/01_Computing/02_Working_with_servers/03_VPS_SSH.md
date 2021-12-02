[index](README.md)
# SSH Tunneling

To connect to a remote host, TU Delft uses a *proxy server*, know as  **bastion**. Thefore, to reach a remote host, a user has to connect first to the **bastion** and from there to the remote host, e.g., *my-vm.tudelft.nl*. However, a user can connect directly to the remote host using *ssh tunneling*.

## Set a Default SSH Tunneling for a Host (Linux Terminal)

1. On your local machine, edit the `~/.ssh/config` file and add the following confuration:

```bash 
Host <host-nickname>
    HostName <target-host>
    User <target-username>
    ProxyCommand ssh <bastion-username>@linux-bastion-ex.tudelft.nl -W %h:%p 
```
Replace:
**<host-nickname>:** a name for you choice for the targe host, e.g., *my-server*
**<target-host>:** the actual name of the target host (FQDM), e.g, *server.tudelft.nl*
**<target-username>:**  the username used to login to the target host, e.g., *wlodewijk*
**<bastion-username>:** the username used to login to the bastion server, e.g., *wlodewijk*

2. Create a key-pair on the local machine.

```bash
$ ssh-keygen -f ~/.ssh/<my-keyname> -t rsa -b 4096
```
You will be promted to crate a *passphrase*, we recommend you to add one to make the connection more secure. The passphrase will be asked every time you connect to the target host.

A private and public keys will be added to `~/.ssh`. The public key is in the `<my-keyname>.pub`

3. Copy the content of the public key to the `~/.ssh/authorized_keys` file in the target host.

4. Connect to the target host using *ssh tunneling*. Use your *bastion-password* when asked.

```bash
$ ssh <host-nickname>
```

If you encounter problems with the connection. Use the debug mode `ssh -vvv <host-nickname>` to find out what might have gone wrong.


## Tunneling with WinSCP
If using winscp, you will find detailed information here: https://winscp.net/eng/docs/ui_login_tunnel


# Moving Data Around

## Copy Data from Client to Host using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <my-local-file>  <target-username>@<target-host>:/<remote-directory>/
```
## Copy Data from Host to Client using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <target-username>@<target-host>:/tmp/<my-remote-file> /<my-local-directory>/
```

## Copy Data using SSH Tunneling

If a default [ssh tunneling](##ssh-tunneling) was configured correctly. Data can be copied to and from a remote host as follows:

```bash
# Copy TO Remote Host
$ scp <my-local-file> <host-nickname>:/<remote-directory>/
```

```bash
# Copy FROM Remote Host
$ scp <host-nickname>:/<my-remote-file> /<my-local-directory>/ 
```

## scp with sudo files from a remote host to another remote host
"-C /tmp/a" can be used when you wanted to "cd /tmp/a"
```
ssh source.tudelft.nl sudo tar cf - -C /tmp/a . | ssh target.tudelft.nl  sudo tar xvf - -C /tmp/b/
```
