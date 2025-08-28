[index](README.md)
# streams
RHEL8 uses streams. A lot of the streams are disabled by default.
If you need software that is not available you can check if there is a stream for the wanted software
```bash
dnf module list
```


# PHP7.2 
```bash
  dnf module enable php
  yum install php
```

# PHP7.3
Red Hat Enterprise Linux 8 is distributed with PHP 7.2. One can run below commands to update from 7.2 to 7.3:

```bash
  dnf module disable php
  dnf module enable php:7.3
  dnf update php
```

In case there is no php7.2 present, one can install it as below:

```bash
  dnf module enable php:7.3
  yum install php
```

# PHP7.4 
Red Hat Enterprise Linux 8 is distributed with PHP 7.2. One can run below commands to update from 7.2 to 7.4:

```bash
  dnf module disable php
  dnf module enable php:7.4
  dnf update php
```
In case there is no php7.2 present, one can install it as below:

```bash
  dnf module enable php:7.4
  yum install php
```
