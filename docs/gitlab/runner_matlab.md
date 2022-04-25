---
section: gitlab
title: GitLab runner for MATLAB
author_1: Maurits Kok 
author_2: 
---

# Gitlab runner for MATLAB

## Background
With the continuous method of software development, you continuously build, test, and deploy iterative code changes. This iterative process helps reduce the chance that you develop new code based on buggy or failed previous versions. With this method, you strive to have less human intervention or even no intervention at all, from the development of new code until its deployment.

### Purpose of this guide
With this guide, you will create a Continuous Integration Pipeline on a repository within the [TU Delft Gitlab](https://gitlab.tudelft.nl) to use a Matlab environment.

## Prerequisites
- TU Delft netID
- Matlab account 
- Basic knowledge of Linux (for setting up a server)
- Basic knowledge of Docker (for creating a custom Matlab image)
  ```{tip}
  To learn more about Docker containers, please look at the [Reproducible Computational Environments Using Docker lesson](https://carpentries-incubator.github.io/docker-introduction/) from the Software Carpentries.
  ```

## Glossary of terms
**CI/CD pipeline**  
_A CI/CD pipeline automates your software delivery process. The pipeline builds code, runs tests (Continuous Intergation), and safely deploys a new version of the application (Continuous Delivery). See this [introduction](https://semaphoreci.com/blog/cicd-pipeline)._

**Docker**  
_We use a Docker container to run the Gitlab runner and initialise the CI/CD pipeline._

**Gitlab runner** (from GitLab documentation)  
_Runners are the agents that run the CI/CD jobs that come from GitLab. When you register a runner, you are setting up communication between your GitLab instance and the machine where GitLab Runner is installed. Runners usually process jobs on the same machine where you installed GitLab Runner._

**Gitlab jobs**  
_Pipeline configuration begins with jobs. Jobs are the most fundamental element of a `.gitlab-ci.yml` file. Each job is executed by a Gitlab runner. See Gitlab documentation for more [info](https://docs.gitlab.com/ee/ci/jobs/)._

## Steps
1. Request a TU Delft Virtual Private Server
1. Set up a Gitlab runner
1. Create a Docker image with a custom Matlab installation
1. Register a gitlab runner for the Matlab container
1. Obtain a Matlab license file
1. Configure the CI/CD pipeline
1. Add a job to test the pipeline
1. Optional: Updating the Matlab version

### Step 1. Request a TU Delft VPS
If you want to work with the TU Delft Gitlab instance and you want to implement CI/CD pipelines, then you need to install a Gitlab runner on your own. Runners are the agents that run the CI/CD jobs that come from GitLab. Currently, the TU Delft instance does not provide this feature out-of-the-box. Therefore, we need a separate (virtual) server to run the Gitlab runners and execute the jobs in the CI/CD pipeline.

The TU Delft offers Virtual Private Servers (VPS) for researchers through the [TopDesk selfservice portal](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34). If you don't have a VPS already, please follow this guide to [request a Virtual Private Server](https://tu-delft-dcc.github.io/01_Computing/02_Working_with_servers/01_VPS_request.html)

**VPS requirements**
- 50Gb disk space (the Matlab installation in this guide requires ~10 Gb, but this depends on the size of the installed addons)

### Step 2. Setting up Gitlab runners
To set up a gitlab runner on the VPS, please follow this [guide for setting up GitLab runners](https://tu-delft-dcc.github.io/03_Software/06_Advanced%20code%20management/02_CI_GitLab_Docker.html).

**TLDR**
1. Install docker with

    ```{code-block} bash
    sudo apt install docker.io
    ```
1. Verify installation with  
    ```{code-block} bash 
    sudo docker --version
    ```
1. _Optional: Move default storage location to larger drive_  
    If the file space in the Docker Root directory is not adequate, we must relocate the Docker Root. Please consult this [guide for instructions](https://www.ibm.com/docs/en/z-logdata-analytics/5.1.0?topic=compose-relocating-docker-root-directory).
1. Deploy the gitlab-runner with
    ```{code-block} bash
    docker run -d --name gitlab-runner --restart always \
    -v /srv/gitlab-runner/config:/etc/gitlab-runner \
    -v /var/run/docker.sock:/var/run/docker.sock \
    gitlab/gitlab-runner:latest
    ```
1. Verify deployment with  
    ```{code-block} bash
    sudo docker ps -a
    ```    


### Step 3. Create a Docker image containing a custom Matlab installation
In order for a Gitlab runner to execute Matlab code, it needs to be able to access a container with Matlab installed. The aim of this step is to create a Docker image with Matlab installation that can be used by a Gitlab runner. By building our own Docker image, we can specify the Matlab version and customize the installed toolboxes.

```{note}
We have looked into using the Docker images developed by [Mathworks](https://hub.docker.com/r/mathworks). When running these images, you are prompted to supply your Matlab's account username and password to activate the instance. Although it is possible to create a new image from such an activated container and use it on the VPS, we have so far not been able to get this solution working with Gitlab runners. We thus rely on downloading a license file (step 6) and storing it as a Variable on Gitlab (step 7).
```

This Dockerfile is based on Matlab's [Dockerfile template](https://github.com/mathworks-ref-arch/matlab-dockerfile). We will make the following modifications to this template:
- set `bash` as the default run command (Gitlab runners need to access a shell)
- add additional Matlab products with the flag `--products`. In this example, we have added the Parallel Computing Toolbox and the Mapping Toolbox.

In your user folder on the VPS (/home/username), create a file called `Dockerfile`

```{code-block} bash
sudo nano Dockerfile
```
and copy the content below in the Dockerfile. Make sure to update the Matlab release and installed addons to your requirements (see highlights).


```{code-block} docker
---
emphasize-lines: 5, 28
---
# Copyright 2019 - 2021 The MathWorks, Inc.

# To specify which MATLAB release to install in the container, edit the value of the MATLAB_RELEASE argument.
# Use lower case to specify the release, for example: ARG MATLAB_RELEASE=r2020a
ARG MATLAB_RELEASE=r2021b

# When you start the build stage, this Dockerfile by default uses the Ubuntu-based matlab-deps image.
# To check the available matlab-deps images, see: https://hub.docker.com/r/mathworks/matlab-deps
FROM mathworks/matlab-deps:${MATLAB_RELEASE}

# Declare the global argument to use at the current build stage
ARG MATLAB_RELEASE

# Install mpm dependencies
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && \
    apt-get install --no-install-recommends --yes \
    wget \
    unzip \
    ca-certificates && \
    apt-get clean && apt-get autoremove

# Run mpm to install MATLAB in the target location and delete the mpm installation afterwards
RUN wget -q https://www.mathworks.com/mpm/glnxa64/mpm && \ 
    chmod +x mpm && \
    ./mpm install \
    --release=${MATLAB_RELEASE} \
    --destination=/opt/matlab \
    --products MATLAB Parallel_Computing_Toolbox Mapping_Toolbox && \
    rm -f mpm /tmp/mathworks_root.log && \
    ln -s /opt/matlab/bin/matlab /usr/local/bin/matlab

# Add "matlab" user and grant sudo permission.
RUN adduser --shell /bin/bash --disabled-password --gecos "" matlab && \
    echo "matlab ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/matlab && \
    chmod 0440 /etc/sudoers.d/matlab

# Set user and work directory
USER matlab
WORKDIR /home/matlab
CMD ["bash"]
```

To build a Docker image with the name `matlab-gitlab`, run the following command in the folder containing the Dockerfile:

```{code-block} bash
sudo docker build . -t matlab-gitlab:latest
```

You can verify the presence of the image with
```{code-block} bash
sudo docker images
```

This image is now available locally on the VPS. 

```{tip}
You can also [upload your Docker image to Dockerhub](https://docs.docker.com/engine/reference/commandline/push/) and have it available from there. This removes the need to build the image on the VPS as it can be pulled directly from DockerHub.
```

### Step 4. Register the Matlab runner
After deploying the gitlab-runner in step 2, we need to register a new runner for our `matlab-gitlab` image. Run the following command to register your runner and configure it to deploy in a Docker container on your server.

```{code-block} bash
docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register
```

In response to this command you will be prompted to answer a series of questions. You can find the required gitlab-ci token in your Gitlab repository under **Settings -> CI/CD -> Runners**:


```{code-block} bash
sudo docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register \
  --non-interactive \
  --url "https://gitlab.tudelft.nl/" \
  --registration-token "REPOSITORY_TOKEN" \
  --executor "docker" \
  --docker-image matlab-pvmd:r2021b \
  --description "matlab-runner" \
  --tag-list "matlab" \
  --docker-privileged=true \
  --docker-cap-add "NET_ADMIN" \
  --docker-pull-policy "if-not-present" \
```

For the changes to take effect, restart the gitlab-runner with

```{code-block} bash
sudo docker restart gitlab-runner
```

The runner configurations are stored in `/srv/gitlab-runner/config/config.toml`. If you would like to view or or modify the Matlab runner, run

```bash
sudo nano /srv/gitlab-runner/config/config.toml
```

After registering the runner, the configuration file should contain:

````{toggle}
```{code-block}
concurrent = 4
check_interval = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "matlab-gitlab"
  url = "https://gitlab.tudelft.nl"
  token = "<token>"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "matlab-gitlab:latest"
    privileged = true
    disable_entrypoint_overwrite = false
    cap_add = ["NET_ADMIN"]
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    pull_policy = "if-not-present"
    shm_size = 0
```
````

### Step 5. Obtain a Matlab license file
Every TU Delft employee has access to an Individual Matlab license. Normally, you would activate Matlab only once after installation through an online activation step. However, this does not work for a Docker container as it is relaunched for each CI trigger. 

The following steps for activating Matlab on an offline machine are adapted from the [Matlab Forum](https://nl.mathworks.com/matlabcentral/answers/259627-how-do-i-activate-matlab-or-other-mathworks-products-without-an-internet-connection):

1. Obtain your Host ID
1. Obtain your computer login name or username
1. Activate the license through the License Center to obtain license file

**1. Obtain your Host ID**  
The Matlab license can only be activated for a specifc computer. In the Docker container, we will set the hostID of the container to **0242ac11ffff**.

```{note}
Docker automatically assigns an IP address to each running container, starting from 172.17.0.2 until 172.17.0.255. These IP addresses determine the container's MAC address (see [here](https://docs.gz.ro/modify-linux-hostid.html) for more details), which in turn needs to match with our license. To prevent the MAC address of the Matlab container from switching and thereby invalidating the license, we will set it to 02:42:ac:11:ff:ff in the `.gitlab-ci.yml` file.
```

**2. Obtain your computer login name or username**  
The Matlab license is created for a specific user. In the Docker container, we will set the username to **matlab**.

**3. Activate the license through the License Center to obtain license file**
1. Go to the License Center: https://www.mathworks.com/mwaccount
1. Under My Software, click the license number you want to activate. If you do not see your license number, in the bottom right hand corner, click View Additional Licenses or Trials. 
1. Click the Install and Activate tab
1. Click Activate to Retrieve License File and/or Activate a Computer
1. Enter the following information: 
    - the release you are activating = **r2021b** (same version as in the Dockerfile)
    - the operating system = **Linux**
    - the host ID = **0242ac11ffff**
    - your user or login name = **matlab**
    - the Activation Label = **matlab-gitlab**  
1. Download the `license.lic` file 


### Step 6. Configure the CI/CD pipeline on Gitlab
Before we can run a CI job, we need to configure a few settings in our Gitlab repository

**1. Add tag to matlab runner**    
    Under **Settings -> CI/CD -> Runners** we can find the available specific runners. Press the edit button on the matlab-gitlab runner and add the tag `matlab-gitlab`. With this, we can call more easily call this specific runner within our CI pipeline.

**2. Add license as Variable**  
    Under **Settings -> CI/CD -> Variables** add a new variable called `MATLAB_LICENSE`, past the content of the downloaded `license.lic` file and set `type` to `file`. Having the license available as a Gitlab variable allows us to update it without having to change the Matlab image.

````{note}
Alternatively, we could have added the license file directly to the Docker image. With the license file in the same folder as the Dockerfile and adding the following command to the Dockerfile, we can build a Docker image with an activated Matlab:

  ```{code-block} docker
  COPY license.lic /opt/matlab/licenses/
  ```
Here, we opted to have it accessible through the Gitlab settings together with the accompanying hostid.

  ```{warning}
  Never share any Docker images that contain license files or other confidential information.
  ```

````

### Step 7. Add a job to test the pipeline
To test the pipeline, add the following content to `.gitlab-ci.yml` via **CI/CD -> Editor** in your repository. 

```{code-block} yaml
variables:
  MAC_ADDRESS: 02:42:ac:11:ff:ff

check_matlab:
  tags: 
    - matlab-gitlab
  before_script:
    # Change the mac-address to match the Matlab license
    - sudo ifconfig eth0 hw ether "$MAC_ADDRESS"

    # Add the Matlab license to the Matlab installation in the container
    - sudo mkdir /opt/matlab/licenses
    - sudo mv ${MATLAB_LICENSE} /opt/matlab/licenses/license.lic   
  script:    
    # Run a Matlab function/script through the -batch argument
    - matlab -batch "disp('hello world!')"
```
After commiting, the pipeline should run and execute the job `check_matlab`. You can check the status of the pipeline via **CI/CD -> Pipelines**.

If all went well, you have successfully setup a Gitlab runner to run Matlab code. Congrats! 

### Step 8. Optional: Updating the Matlab version
If you need to update the Matlab version of the Docker container, you will need to go throught the following steps:

1. Update the Matlab version in the Dockerfile
1. Build the docker image with
   `sudo docker build . -t matlab-pvmd:<version>`
1. Download a new `license.lic` file (see step 5 of this guide)
1. Update the CI Variable `MATLAB_LICENSE` with the new license content
1. Update the image names (not the tags) in `.gitlab-ci.yml` to use the new image.
    ```{note} 
    If you want to test your code with multiple Matlab versions to ensure backward compatibility, please look at this [example](https://forum.gitlab.com/t/testing-with-all-version-combinations-of-python-django/7408) to use multiple docker images.
    ```

## References
- [Activating Matlab without an internet connection](https://nl.mathworks.com/matlabcentral/answers/259627-how-do-i-activate-matlab-or-other-mathworks-products-without-an-internet-connection)
- [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)
- [Register a Gitlab runner](https://docs.gitlab.com/runner/register/)
