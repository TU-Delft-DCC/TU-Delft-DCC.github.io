## How to fix the error “host key verification failed”

When you connect to a server for the first time, the server prompts you to confirm that you are connected to the correct system. The following example uses the ssh command to connect to a remote host named host03:

```bash
# ssh host03
The authenticity of host 'host03 (192.0.2.103)' can’t be
established. ECDSA key fingerprint is ...
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'host03,192.0.2.103' (ECDSA) to the list of known hosts.
```

Host validation is one of OpenSSH’s major features. The command checks to make sure that you are connecting to the host that you think you are connecting to. When you enter yes, the client appends the server’s public host key to the user’s ~/.ssh/known_hosts file, creating the ~/.ssh directory if necessary. The next time you connect to the remote server, the client compares this key to the one the server supplies. If the keys match, you are not asked if you want to continue connecting.

## What causes host key verification failed error

If someone tries to trick you into logging in to their machine so that they can sniff your SSH session, you will receive a warning similar to the following:

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
dd:cf:50:31:7a:78:93:13:dd:99:67:c2:a2:19:22:13.
Please contact your system administrator.
Add correct host key in /home/testuser/.ssh/known_hosts to get rid of this message.
Offending key in /home/testuser/.ssh/known_hosts:3
RSA host key for 192.0.2.103 has changed and you have requested strict checking.
Host key verification failed.
```

If you ever get a warning like this, stop and determine whether there is a reason for the remote server’s host key to change (such as if SSH was upgraded or the server itself was upgraded). If there is no good reason for the host key to change, do not try to connect to that machine until you have resolved the situation.

## How to correct the “host key verification failed” error

### Method 1 - removing old key manually

1. On the source server, the old keys are stored in the file ~/.ssh/known_hosts.

2. Only if this event is legitimate, and only if it is precisely known why the SSH server presents a different key, then edit the file known_hosts and remove the no longer valid key entry. Each user in the client/source server has its own known_hosts in its home directory, just remove the entry in the file of a specific user for the destination server. For example:
  - If root wants to ssh to the server, just removing entry in the /root/.ssh/known_hosts file is all right.
  - If testuser wants to ssh to the server, then remove the entry in the file /home/testuser/.ssh/known_hosts.

3. In this case, we will remove the the third line for the destination server 192.0.2.103 from the file /home/testuser/.ssh/known_hosts.

```
$ sed -i '3d' /home/testuser/.ssh/known_hosts
```

### Method 2 - removing old key using the ssh-keygen command

You can also remove the old key using the ssh-keygen command as well. The syntax to use the command is below.

```
$ ssh-keygen -R [hostname|IP address]
```

For example, In our case we will use the IP address to delete the old key.

```
$ ssh-keygen -R 192.0.2.103
# Host 192.0.2.103 found: line 3
/home/testuser/.ssh/known_hosts updated.
Original contents retained as /home/testuser/.ssh/known_hosts.old
```

__Note : If you do not know precisely, why the SSH server presents a different key, either your known_hosts file is incorrect, or somebody must investigate this server and the network connections to understand the reason of the unexpected change.__

### Verify

If the remote servers asks for a confirmation to add the new key to the ~/.ssh/known_host file, it confirms that you have successfully removed the old key. If you confirm the request, the source machine adds the new key into the ~/.ssh/known_host file.

```
$ ssh root@192.0.2.103
The authenticity of host '192.0.2.103 (192.0.2.103)' can't be established.
ECDSA key fingerprint is SHA256:V+iGp3gwSlnpbtYv4Niq6tcMMSZivSnYWQIaJnUvHb4.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.0.2.103' (ECDSA) to the list of known hosts.
```

