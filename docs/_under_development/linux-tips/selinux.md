[index](README.md)

# SE Linux
On newer RHEL systems SE linux is enabled by default.

### File context
A path is labeled with a context to avoid abuse.

Most common is a non default directory for a webserver or database.

```bash
  ls -ldZ /var/www/html
  drwxr-xr-x. root root system_u:object_r:httpd_sys_content_t:s0 /var/www/html
```
Here the context is httpd_sys_content_t.

Set the context on the directory and all below (/.*)? in the selinux database.
```bash
  semanage fcontext -a -t httpd_sys_content_t '/data/html(/.*)?'
```
Restore the context according the selinux database.
```bash
  restorecon -vRF /data/html
```

You can see examples in all current file contexts
```bash
  semanage fcontext -l
```

### booleans
SE Linux uses booleans for complexer operations. 

For example:"May the httpd connect the database?"

NO: httpd_can_network_connect_db --> off

To enable database connections from httpd (-P is persistent over reboots):
```bash
  setsebool -P httpd_can_network_connect_db=1
```

to list all booleans:
```bash
  getsebool -a
```

### Docker
The audit logs on docker systems can give false paths. Be aware.

## Trouble shooting
Install setroubleshoot if not already installed.

In /var/log/audit/audit.log are cryptic messages.
```bash
  sealert -a /var/log/audit/audit.log
```
Can be used to decode them.

In /var/log/messages there can be hints:
```bash
  grep "SELinux is preventing" /var/log/messages
```
A "helpfull" line can be like
  Feb 1 12:34:50 server setroubleshoot: SELinux is preventing postgres from unlink access on the file db_0.stat. For complete SELinux messages  run: sealert -l fbc0c113-8ba8-4de6-a0a2-f2628687b6c3

If a program still doesn't work as expected you can disable selinux temporary.
```bash
  setenforce 0
```
Test the program. Record if the behaviour changed.
```bash
  setenforce 1
```
If the behaviour changed probably selinux is to blame.

