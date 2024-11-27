---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
#date: MM/DD/YYYY

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Using a docker container with a GUI

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Maurits Kok
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - 
# - 

---

Docker is an open platform for developing, shipping, and running applications. Docker provides the ability to package and run an application in a loosely isolated environment called a container. Containers are lightweight and contain everything needed to run the application, so you do not need to rely on what is currently installed on the host system. You can easily share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

![](https://user-images.githubusercontent.com/15414938/123805382-52543b00-d8ee-11eb-8f76-ae598d6fdb83.png)

**Dockerfile** – is a text document that contains all the commands you would normally execute manually in order to build a Docker image. The instructions include a choice of operating system and all the libraries we need to install into it. Docker can build images automatically by reading the instructions from a Dockerfile.  
**Docker Images** – are the basis of containers. A Docker image is an immutable (unchangeable) file that contains the source code, libraries, dependencies, tools, and other files needed for an application to run.  
**Docker Container** – A container is, ultimately, just a running image.

## Docker installation

Docker can be installed on Windows, macOS, and Linux. Please visit the [Docker website](https://docs.docker.com/get-docker/) for downloading and installation instructions. Note, you will need admin access to your system. 

**Please check the Issues/troubleshooting session at the end of this page if you encounter some problems during installation. If your problem is not listed you can add it as an issue in the main repository.**

### Verify Docker installation
Run the following commands in the terminal (see below) to verify your installation:

- `docker --version`   
 Will output the version number
- `docker run hello-world`  
Will output a welcome message. If you haven't run this command before, you will receive the message _Unable to find image: 'hello-world:latest' locally_. Docker will then proceed by downloading and running the latest version from [DockerHub](https://hub.docker.com/_/hello-world).

## Terminal access

**Linux**  
The default Unix Shell for Linux operating systems is usually Bash. On most versions of Linux, it is accessible by running the [(Gnome) Terminal](https://help.gnome.org/users/gnome-terminal/stable/) or [(KDE) Konsole](https://konsole.kde.org/) or [xterm](https://en.wikipedia.org/wiki/Xterm), which can be found via the applications menu or the search bar. If your machine is set up to use something other than bash, you can run it by opening a terminal and typing `bash`.

**macOS**  
For a Mac computer, the default Unix Shell is Bash, and it is available via the Terminal Utilities program within your Applications folder. To open Terminal, try one or both of the following:

- Go to your Applications. Within Applications, open the Utilities folder. Locate Terminal in the Utilities folder and open it.
- Use the Mac ‘Spotlight’ computer search function. Search for: Terminal and press Return.

For more info: [How To use a terminal on Mac](https://www.macworld.co.uk/how-to/how-use-terminal-on-mac-3608274/)

**Windows**  
Computers with Windows operating systems do not automatically have a Unix Shell program installed. We encourage you to use an emulator included in [Git for Windows](https://gitforwindows.org/), which gives you access to both Bash shell commands and Git. To install, please follow these [instructions](https://coderefinery.github.io/installation/git-in-terminal/#git-in-terminal).


## X Windows System
Docker doesn't have any build-in graphics, which means it cannot run desktop applications by default. For this, we require the X Windows System. The X Window System (X11, or simply X) is a windowing system for bitmap displays, common on Unix-like operating systems. X provides the basic framework for a GUI environment: drawing and moving windows on the display device and interacting with a mouse and a keyboard.

If you are on a desktop Linux, you already have one. For macOS, you can download [XQuartz](https://www.xquartz.org/), and for Windows, we tested [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

Desktop applications will run in Docker and will try to communicate with the X server you’re running on your PC. They don’t need to know anything but the location of the X server and an optional display that they target. This is denoted by an environmental variable named `DISPLAY`, with the following syntax: `DISPLAY=xserver-host:0`. The number you see after the `:` is the display number; for the intents and purpose of this article, we will consider this to be equivalent to _0 is the primary display attached to the X server_.

In order to set up the environment variable, we need to add the following code to the `docker run` command in the terminal:

::: {.panel-tabset}

### Windows
`-e DISPLAY=host.docker.internal:0`

### macOS
`-e DISPLAY=docker.for.mac.host.internal:0`

### Linux
`--net=host -e DISPLAY=:0`
:::

With these commands (and an active X server on the host system), any graphical output inside the container will be shown on your own desktop. 

## Mount a volume

The docker image with which you can spawn a container contains all the software and general datafiles. However, we still need to give the container access to your dataset. To do so, we can mount a directory on your own system inside the container with the following command structure: `-v <abs_path_host>:<abs_path_container>`. Assuming your terminal is opened inside the data folder on your system, the specific commands for the different operating systems mount this folder as the `/data` folder inside the container, are:

For Windows in GitBash: `-v /$(pwd):/data`   
For Windows in cmd: `-v %cd%:/data`   
For Linux and macOS:  `-v $(pwd):/data`   

`$(pwd)` can be replaced with the absolute path of the datafolder, or be used to access subdirectories (e.g. `$(pwd)/data:/data`).

For more info about mounting volumes, check this [StackOverflow question](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10)

## Running a container with data and graphical output

To start a container from an image, we use the command `docker run <image_name>`. We also pass the additional flags `--rm` to delete the container after closing and `-it` to be able to interact with the container. Combining all arguments then leads to the following commands to run (and automatically close) the container:

::: {.panel-tabset}
### Windows
`docker run --rm -it -e DISPLAY=host.docker.internal:0 -v /$(pwd):/data <image_name>:<image_version> `

### macOS
`docker run --rm -it -e DISPLAY=docker.for.mac.host.internal:0 -v $(pwd):/data <image_name>:<image_version>`

### Linux
`docker run --rm -it --net=host -e DISPLAY=:0 -v $(pwd):/data <image_name>:<image_version>`
:::

## Issues/Troubleshooting

- For Linux users encountering the error _Unable to init server_, please run `xhost +` in the terminal and rerun the `docker run` command. For more info, see [here](https://www.thegeekstuff.com/2010/06/xhost-cannot-open-display/).
- **WSL 2 installation incomplete for Windows users** 
    - Enable the virtualization in the BIOS
    - Follow ALL the steps described in: https://docs.microsoft.com/en-us/windows/wsl/install-manual
- Failing to port a display in the docker container for Mac users.
    - Solution: Change the docker run command by this one , 
    `docker run --rm -it -e DISPLAY=IPADDRESS:0 -v $(pwd):/data <image_name>:<image_version>`
    - The *IPADDRESS* is gotten from typing `ifconfig` in the terminal. 
- Failing to run the pipeline once the GUI is open
    - Check that all documents are closed before run it , namely the *Getting started* and the *adapter files* documents. 
- Failing to mount an external hard drive in Windows when running a docker container 
    - Error:
```bash
        libGL error: No matching fbConfigs or visuals found
        libGL error: failed to load driver: swrast
```
    - Solution (noy yet found):
- Look into this links: 
    - https://stackoverflow.com/questions/46586013/glxgears-not-working-inside-of-docker
    

<!-- ## References
- https://medium.com/better-programming/running-desktop-apps-in-docker-43a70a5265c4
- https://coderefinery.github.io/installation/git-in-terminal/#git-in-terminal
- https://ucsbcarpentry.github.io/2019-10-24-gitbash/setup.html -->