# Moving data to your server

## Copy Data from Client to Host using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <my-local-file>  <target-username>@<target-host>:/<remote-directory>/
```
## Copy Data from Host to Client using ProxyCommand

```bash
$ scp -o "ProxyCommand ssh -W %h:%p <bastion-username>@linux-bastion-ex.tudelft.nl" <target-username>@<target-host>:/tmp/<my-remote-file> /<my-local-directory>/
```

## Copy Data using SSH Tunneling

If a default [ssh tunneling](VPS_SSH.md) was configured correctly. Data can be copied to and from a remote host as follows:

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

```bash
ssh source.tudelft.nl sudo tar cf - -C /tmp/a . | ssh target.tudelft.nl  sudo tar xvf - -C /tmp/b/
```
