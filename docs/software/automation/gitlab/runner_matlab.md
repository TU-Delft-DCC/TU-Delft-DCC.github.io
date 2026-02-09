---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2026-01-20

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2026-01-22

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Setting up a GitLab runner for MATLAB

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
maintainer_1: Maurits Kok
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
 - Software
 - Automation
 - MATLAB
 - GitLab
 - CI/CD

css: steps-style.css
---

## Introduction
With the continuous method of software development, you continuously build, test, and deploy iterative code changes. This iterative process helps reduce the chance that you develop new code based on buggy or failed previous versions. With this method, you strive to have less human intervention or even no intervention at all, from the development of new code until its deployment.

With this guide, you will create a Continuous Integration Pipeline on a repository within the [TU Delft GitLab](https://gitlab.tudelft.nl) to use a MATLAB environment.

:::{.callout-note appearance="simple" icon="false" collapse="true"}
## Glossary of terms
**CI/CD pipeline**  
_A CI/CD pipeline automates your software delivery process. The pipeline builds code, runs tests (Continuous Intergation), and safely deploys a new version of the application (Continuous Delivery)._

**Docker**  
_We use a Docker container to run the GitLab runner and initialise the CI/CD pipeline._

**GitLab runner** (from GitLab documentation)  
_Runners are the agents that run the CI/CD jobs that come from GitLab. When you register a runner, you are setting up communication between your GitLab instance and the machine where GitLab Runner is installed. Runners usually process jobs on the same machine where you installed GitLab Runner._

**GitLab jobs**  
_Pipeline configuration begins with jobs. Jobs are the most fundamental element of a `.gitlab-ci.yml` file. Each job is executed by a GitLab runner. See GitLab documentation for more [info](https://docs.gitlab.com/ee/ci/jobs/)._
:::

#### Prerequisites
- TU Delft NetID
- MATLAB account
- Basic knowledge of Linux (for setting up a server)
- Basic knowledge of Docker (for creating a custom MATLAB image)
- Know which MATLAB version and toolboxes you want to use in the CI/CD pipeline

:::{.callout .steps}
- [Step 1. Request a TU Delft Virtual Private Server](#step-1.-request-a-tu-delft-vps)
- [Step 2. Set up a GitLab runner](#step-2.-set-up-a-gitlab-runner)
- [Step 3. Create a Docker image with a custom MATLAB installation](#step-3.-create-a-docker-image-containing-a-custom-matlab-installation)
- [Step 4. Create a GitLab runner](#step-4.-create-the-gitlab-runner)
- [Step 5. Register a GitLab runner](#step-5.-register-the-matlab-runner)
- [Step 6. Obtain a MATLAB license file](#step-6.-obtain-a-matlab-license-file)
- [Step 7. Configure the CI/CD pipeline](#step-7.-configure-the-cicd-pipeline-on-gitlab)
- [Step 8. Add a job to test the pipeline](#step-8.-add-a-job-to-test-the-pipeline)
- [Step 9. (Optional) Update the MATLAB version](#step-9.-optional-update-the-matlab-version)
:::

## Step 1. Request a TU Delft VPS
The TU Delft GitLab instance does not have runners available by default. To set up a runner for the repository, we need to deploy one on a separate (virtual) server in order to execute the jobs in the CI/CD pipeline. In order to accomodate the size of MATLAB, ensure to request **50Gb of disk space** (the MATLAB installation in this guide requires ~10 Gb, but this depends on the size of the installed addons).

The TU Delft offers Virtual Private Servers (VPS) for researchers through the [TopDesk selfservice portal](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=418c986f186d4934848dc2712039ed34). If you don't have a VPS already, please follow this guide to [request a Virtual Private Server](../../../infrastructure/vps_request.md).

## Step 2. Set up a GitLab runner
To set up a GitLab runner on the VPS, please follow this [guide for setting up GitLab runners](./gitlab_docker.md).

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
For a general introduction into Docker containers, have a look at the [Reproducible Computational Environments Using Docker lesson](https://carpentries-incubator.github.io/docker-introduction/) from the Software Carpentries.
:::

In summary, the steps are:

1. Install docker with

    ```bash
    sudo apt install docker.io
    ```
2. Verify installation with  

    ```bash 
    sudo docker --version
    ```
3. _Optional: Move default storage location to larger drive_  
    If the file space in the Docker Root directory is not adequate, we must relocate the Docker Root. 

:::{.callout-note appearance="simple" icon="false" collapse=true}

  {{< include _docker_root.md >}}

:::

4. Deploy the gitlab-runner with

    ```bash
    sudo docker run -d --name gitlab-runner --restart always \
    -v /srv/gitlab-runner/config:/etc/gitlab-runner \
    -v /var/run/docker.sock:/var/run/docker.sock \
    gitlab/gitlab-runner:latest
    ```
5. Verify deployment with  

    ```bash
    sudo docker ps -a
    ```    

## Step 3. Create a Docker image containing a custom MATLAB installation
In order for a GitLab runner to execute MATLAB code, it needs to be able to access a container with MATLAB installed. The aim of this step is to create a Docker image with MATLAB installation that can be used by a GitLab runner. By building our own Docker image, we can specify the MATLAB version and customize the installed toolboxes.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
We have looked into using the Docker images developed by [Mathworks](https://hub.docker.com/r/mathworks). When running these images, you are prompted to supply your MATLAB's account username and password to activate the instance. Although it is possible to create a new image from such an activated container and use it on the VPS, we have so far not been able to get this solution working with GitLab runners. We thus rely on downloading a license file (step 6) and storing it as a Variable in the GitLab repository (step 7).
:::

The Dockerfile below is based on MATLAB's [MATLAB Dockerfile 2021](https://github.com/mathworks-ref-arch/matlab-dockerfile/blob/8bfb39430f3c26635b6147094ffbf139caa1cf62/Dockerfile). We will make the following (highlighted) modifications to this template:

- Update the MATLAB version to `r2025b`.
- Set `bash` as the default run command (GitLab runners need to access a shell)
- Add additional MATLAB products with the flag `--products`. In this example, we have added the `Parallel Computing Toolbox` and the `Mapping Toolbox`.

1. In your user folder on the VPS (/home/username), create a file called `Dockerfile`

  ```bash
  sudo nano Dockerfile
  ```
2. Copy the content below in the Dockerfile. 

::: {.callout-note collapse=true appearance="simple" icon="false"}
{{< include _matlab_dockerfile.md >}}
:::

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
This example uses MATLAB `r2025b` and includes the `Parallel Computing Toolbox` and the `Mapping Toolbox`. For a list of available product names, see [here](https://github.com/mathworks-ref-arch/matlab-dockerfile/tree/main/mpm-input-files).
:::

3. To build a Docker image with the name `matlab-gitlab` and the version reference `r2025b`, run the following command in the folder containing the Dockerfile:

  ```bash
  sudo docker build . -t matlab-gitlab:r2025b
  ```

  You can verify the presence of the image with

  ```bash
  sudo docker images
  ```

This image is now available locally on the VPS. 

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
You can also [upload your Docker image to Dockerhub](https://docs.docker.com/engine/reference/commandline/push/) and have it available from there. This removes the need to build the image on the VPS as it can be pulled directly from DockerHub.
:::

## Step 4. Create the GitLab runner
You can find the required gitlab-ci token in your GitLab repository under **Settings -> CI/CD -> Runners**. 

1. Press: **Create project runner**
2. Add a tag for the runner: `matlab`. This tag will be used to call this specific runner in the CI/CD config `gitlab-ci.yml`.
3. Press: **Create runner**
4. Under **Step 1**, the runner authentication token is shown. You will need this token during the next step.

### Step 5. Register the MATLAB runner
After deploying the gitlab-runner in step 2, we need to register a new runner for our `matlab-gitlab:r2025b` image. Run the following command to register your runner and configure it to deploy in a Docker container on your server.

```bash
sudo docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register 
```

In response to this command you will be prompted to answer a series of questions:

1. Enter the GitLab instance URL: `https://gitlab.tudelft.nl/`
2. Enter the registration token: <authentication token> (from step 4)
3. Enter a name for the runner: `matlab-runner`
4. Enter an executor: `docker`
5. Enter the default Docker image: `matlab-gitlab:r2025b` (name of the image created in step 3)

The runner configurations are stored in `/srv/gitlab-runner/config/config.toml`. 

To finish the setup of the MATLAB runner, we need to modify the configuration file to add some additional Docker settings.

Open the configuration file with

```bash
sudo nano /srv/gitlab-runner/config/config.toml
```

update the following line

```toml
privileged = true
```

and add the following line under `[runners.docker]`:

```toml
pull_policy = "if-not-present"
```

For the changes to take effect, restart the gitlab-runner with

```bash
sudo docker restart gitlab-runner
```

After registering the runner, the configuration file should contain:

:::{.callout-note collapse=true appearance="simple"}
### `config.toml`
```bash
concurrent = 1
check_interval = 0
shutdown_timeout = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "matlab-gitlab"
  url = "https://gitlab.tudelft.nl"
  id = <runner id>
  token = "<authentication token>"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "matlab-gitlab:r2025b"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
    network_mtu = 0
    pull_policy = "if-not-present"
```
:::

## Step 6. Obtain a MATLAB license file
Every TU Delft employee has access to an Individual MATLAB license. Normally, you would activate MATLAB only once after installation through an online activation step. However, this does not work for a Docker container as it is relaunched for each CI trigger. 

The following steps for activating MATLAB on an offline machine are adapted from the [MATLAB Forum](https://nl.mathworks.com/matlabcentral/answers/259627-how-do-i-activate-matlab-or-other-mathworks-products-without-an-internet-connection):

#### Obtain your Host ID
The MATLAB license can only be activated for a specific computer. In the Docker container, we will set the hostID of the container to **0242ac11ffff**.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
Docker automatically assigns an IP address to each running container, starting from 172.17.0.2 until 172.17.0.255. These IP addresses determine the container's MAC address (see [here](https://docs.gz.ro/modify-linux-hostid.html) for more details), which in turn needs to match with our license. To prevent the MAC address of the MATLAB container from switching and thereby invalidating the license, we will set it to 02:42:ac:11:ff:ff in the `.gitlab-ci.yml` file.
:::

#### Obtain your computer login name or username
The MATLAB license is created for a specific user. In the Docker container, we will set the username to **matlab**.

#### Activate the license through the License Center to obtain license file

1. Go to the License Center: <https://www.mathworks.com/mwaccount>
2. Under My Software, click the license for **Designated Computer**
3. Click the tab: **Install and Activate**
4. Under related tasks, click **Activate to Retrieve License File**
5. Enter the following information: 
    - the release you are activating = **r2025b** (same version as in the Dockerfile)
    - the operating system = **Linux**
    - the host ID = **0242ac11ffff**
    - the Computer Label = **matlab-gitlab**  
6. Select **Continue**
7. Download the `license.lic` file and save it to your local machine.


## Step 7. Configure the CI/CD pipeline on GitLab
Before we can run a CI job, we need to configure the license in our GitLab repository. Having the license available as a GitLab variable allows us to renew it without having to change the MATLAB image.

:::{.callout-warning appearance="simple" collapse=true}
## Warning: Keep the license private
Alternatively, we could have added the license file directly to the Docker image. With the license file in the same folder as the Dockerfile and adding the following command to the Dockerfile, we can build a Docker image with an activated MATLAB:

  ```bash
  COPY license.lic /opt/matlab/licenses/
  ```
Here, we opted to have it accessible through the GitLab settings together with the accompanying hostid.

**Never share any Docker images that contain license files or other confidential information.**
:::

Under **Settings -> CI/CD -> Variables**, scroll down to **Project variables** and select **Add variable**.

- Type: `File`
- Environments: `All (default)`
- Visibility: `Visible` (The license contains sensitive information, but its format is incompatible with the `masked` settings)
- Key: `MATLAB_LICENSE`
- Value: Paste the content of the downloaded `license.lic` file here

## Step 8. Add a job to test the pipeline
To test the pipeline, add the following content to `.gitlab-ci.yml` via **CI/CD -> Editor** in your repository. 

```yaml
variables:
  MAC_ADDRESS: 02:42:ac:11:ff:ff

check_matlab:
  tags: 
    - matlab
  # Optional : specify the docker image to use for this job if other than default in the runner config.toml
  image: matlab-gitlab:r2025b
  before_script:
    # Change the mac-address to match the MATLAB license
    - sudo ifconfig eth0 hw ether "$MAC_ADDRESS"

    # Add the MATLAB license to the MATLAB installation in the container
    - sudo mkdir /opt/matlab/licenses
    - sudo mv ${MATLAB_LICENSE} /opt/matlab/licenses/license.lic   
  script:    
    # Run a MATLAB function/script through the -batch argument
    - matlab -batch "disp('hello world!')"
```
After committing, the pipeline should run and execute the job `check_matlab`. You can check the status of the pipeline via **CI/CD -> Pipelines**.

If all went well, you have successfully setup a GitLab runner to run MATLAB code. Congrats! 

## Step 9. Optional: Update the MATLAB version
If you need to update the MATLAB version of the Docker container, you will need to go through the following steps:

1. Update the MATLAB version in the Dockerfile
1. Build the docker image with
   `sudo docker build . -t matlab-gitlab:<version>`
2. Download a new `license.lic` file for the new version (see step 5 of this guide)
3. Update the CI Variable `MATLAB_LICENSE` with the new license content
4. Update the image names (not the tags) in `.gitlab-ci.yml` to use the new image.

:::{.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip
The solution presented in this guide relies on using a license file for activation. As this license is tied to a specific host ID and username, only one may be used at a time. For more complex, multi-version setups, consider exploring network licenses, or GitHub as the hosting platform.
:::

<!-- ## References
- [Activating Matlab without an internet connection](https://nl.mathworks.com/matlabcentral/answers/259627-how-do-i-activate-matlab-or-other-mathworks-products-without-an-internet-connection)
- [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)
- [Register a Gitlab runner](https://docs.gitlab.com/runner/register/) -->
