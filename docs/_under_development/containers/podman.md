---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
#date:

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Podman

# Authors of the document, will not be parsed [manual entry]
author_1:
author_2:

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1:
maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding:

# Meaningful keywords, newline separated [manual entry]
categories: 
 - 
 - 

---

Docker is not available on [RHEL8](https://www.redhat.com/en/enterprise-linux-8) systems anymore. You can use the replacement podman.
In most cases you can replace the "docker" command with "podman"
like:
```bash
docker ps -a
```
becomes:
```bash
podman ps -a
``` 

## Warnings
- You must be aware that the containers are stored in your home directory by default!
- Do not store containers on NFS

## rootless

A great advantage of podman is the ability to run without root permitions.
Like any other services you are not allowed to listen on ports below 1024 and you are not allowed to change the firewall.

The admin user can create an haproxy for example or allow the user to access priviledged ports.

> if the rootless containers fail most of the time /etc/subuid and /etc/subgid are not configured.
> A line is in the format "username:startuid:size" e.g. "username:10000000:65535"
> make sure uid/gid ranges do not overlap.

```
/etc/subuid:
--------------------------------------------------------------------------
user1:1000000:1000
user2:1010000:1000
--------------------------------------------------------------------------

/etc/subgid:
--------------------------------------------------------------------------
group1:1000000:1000
group2:1010000:1000
--------------------------------------------------------------------------
```

### Change storage location
The command:
```
podman info
```
gives the storage location for images and containers. (store: GraphRoot)

Change the container location in ~/.config/containers/storage.conf by setting the graphroot path to a local filesystem.

```
~/.config/containers/storage.conf:
--------------------------------------------------------------------------
[storage]
...
graphroot = "/work/{username}/containers/storage
...

~/.config/containers/libpod.conf
...
volume_path = "/work/{username}/containers/volumes"
...
```

Migrate the storage
```bash
podman system migrate
podman info
```

If there is an error removal of the .local/share/containers is needed. This wil remove all existing containers for this user!

## example
This should work as non-root user.

Create an empty directory and enter it:
```bash
mkdir podman-test
cd podman-test
```
Create a Dockerfile
```Dockerfile
#Dockerfile
FROM centos:7
RUN yum install -y httpd \
    && echo "hello!" > /var/www/html/index.html
EXPOSE 80
CMD [ "/usr/sbin/httpd", "-D","FOREGROUND"]
```
Build the image:
```bash
podman build -t hello:1 .
```
Start the testcontainer:
```bash
podman run --name hello-test -p 8080:80 hello:1
```
This wil be in the foreground.
Start another shell and test the container:
```bash
curl http://localhost:8080
# this should say: hello!
```
cleanup:
```bash
# stop container
podman stop hello-test
# delete container
podman rm hello-test
# delete image
podman rmi hello:1
```
Check containers and images
```bash
podman ps -a
podman images
```
