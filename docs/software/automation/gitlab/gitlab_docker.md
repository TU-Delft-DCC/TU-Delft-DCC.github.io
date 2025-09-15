---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-08-29

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-05

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: CI with Gitlab

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Ashley Cryan
author_2: Maurits Kok

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - gitlab
 - CI/CD
 - docker

---

## Background
If you are using **TU Delft GitLab instance** and you want to implement **DevOps or CI/CD pipelines**, you will need to install a **GitLab runner** yourself. This runner must be set  up on a server, where it will respond to repository events such as commits or pull requests in your GitLab project.

## Quick overview of how it works
To run a CI/CD pipeline, a gitlab-runner Docker container runs continuously on the server. When a new commit is pushed to the GitLab repository, it triggers the CI/CD process. The pipeline, defined in the `.gitlab-ci.yml` file, specifies the jobs to run (e.g., unit tests). The **Docker image** used for running the CI/CD jobs is specified in the first line of the `.gitlab-ci.yml` file. In the below example, we define `image:python:3.12.3`, a new container based on the **python:3.12.3** Docker image is spawned each time a commit is made. This container executes the tests on your Python scripts and generates artifacts, as outlined in the `.gitlab-ci.yml` file.

<img src="https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/711ac593ec886bd9216dff0591a82e6f/Untitled_Document__31_.png" width="600" style="display: block; margin: 0 auto;">

## What this documentation will help achieve
This guide will help you **deploy a GitLab Runner in a Docker container** on a server. Once set up, the runner will automatically execute CI/CD tests and store artifacts whenever a new commit is pushed to your GitLab repository.

## Prerequisites
**Server:** This guide assumes you have access to a server to host the GitLab Runner. You can request a server from TU Delft ICT Services by following the instructions [here](../../../infrastructure/VPS_request.md). It is useful to set this up on a server so that Docker can be running continuously, and be ready to run CI/CD tests whenever a new commit occurs in the repository.

**Docker:** A Docker container is used to run the GitLab Runner and initialize the CI/CD pipeline.

**Gitlab runner:** "Runners are the agents that run the CI/CD jobs that come from GitLab. When you register a runner, you are setting up communication between your GitLab instance and the machine where GitLab Runner is installed. Runners usually process jobs on the same machine where you installed GitLab Runner." - [GitLab documentation](https://docs.gitlab.com)

**GitLab repository:** A remote GitLab repository stores your project code and keeps track of its development. You're on one right now! :) If you haven’t already, log in to TU Delft’s GitLab instance at _gitlab.tudelft.nl_ using your **NetID and password**, and create a repository for your project.

**CI/CD pipeline:** “A CI/CD pipeline automates your software delivery process. The pipeline builds code, runs tests (CI), and safely deploys a new version of the application (CD)”.

## Tools/Software
* GitLab (TU Delft instance)
* Docker
* `gitlab-runner` Docker image

## Steps
1. Request the server
2. Connect to the server via ssh
3. Install Docker on the server
4. Pull in the gitlab-runner image
5. Create a unit test function stored as a file in the repository
6. Make the .gitlab-ci.yml file
7. Set up the GitLab runner
8. Deploy the GitLab runner in a Docker container
9. Register the runner
10. Test the CI/CD pipeline

### Step 1. Request server running Ubuntu
If you don't have a VPS already, you can request one from TU Delft ICT. Instructions for requesting a server and storage are available [here](../../../infrastructure/VPS_request.md).

Recommended Configuration for a GitLab Runner:

- Basic Configuration 4 (Ubuntu)
- No additional **ports** need to be configured for deploying a GitLab Runner with Docker.
- Additional space if your Docker images exceed ~10Gb.

### Step 2. Connect to the server via ssh
The email response from Sysadmin@TUDelft.nl will include instructions for connecting to your server via SSH. The default login process involves:

- Connecting to the **Bastion host** (an intermediary server).
- Connecting to your assigned server (so it is a two-step process).

 Refer to your email provided by ICT admin for these steps.

For **Windows**, you can use PuTTY to connect. For **Mac/Linux**, you can configure one-step access by storing SSH keys between your local machine and the server and setting up an alias.

Upon successfull connection, your terminal/command prompt should display something like this:

<img src="https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/048a06a817852a399c697582ae1e3a08/Screen_Shot_2020-11-17_at_10.30.31.png" width="500" style="display: block; margin: 0 auto;">

### Step 3. Install Docker on the server

Servers often do not come with Docker installed, so you may need to do it by yourself. To check whether Docker is installed, run `docker --version`. If you get an error message, you can install it using the following commands:

```bash
sudo su # this will give you the root access
apt install docker.io
```

Now that you've instlled Docker, you can check its installation with `docker --version` from the terminal. The result should show the version of Docker you just installed.

### Step 4. Pull the gitlab-runner Docker image
In order to run CI/CD jobs for your repository, you need to install GitLab Runner. GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline. Rather than install GitLab Runner directly on the server, we will run a lightweight version of it as a Docker container. To do so, we first need to pull the gitlab-runner Docker image by running:

`docker pull gitlab/gitlab-runner`

You can check whether it was successful by running `docker images` - you should see the gitlab/gitlab-runner image listed in the output.

### Step 5. Create a unit test function stored as a file in the repository

### Step 6. Set up the CI by configuration of the .gitlab-ci.yml file

This file, located in the root of your repository, defines the CI/CD pipeline. It specifies the docker container to run, what scripts to run inside the container, and what to store as artifacts after the job completion.

In the first line of the file, specify the Docker image using: `image: <image_name>:<tag>` to indicate you want to run the runner in a Docker container.  Replace <image_name> with the name of the Docker image (e.g., python, image names can be found on DockerHub). Replace <tag> with the image version (e.g., 3.12.3). If omitted, the latest tag is used by default.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa exclamation-triangle  >}} Important
> This file must be named **.gitlab-ci.yml** for the GitLab Runner to recognize it. Below is an example `.gitlab-ci.yml` file.
> Only use spaces to indent your .yml configuration.
:::

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
Check [Atlassian guides](https://confluence.atlassian.com/x/x4UWN) for more examples.
:::

```yaml
# Sample CI/CD configuration for Python
# -----
test:
  image: python:3.12.3 # Docker image for the build environment
  cache:
    paths:
      - .cache/pip
      - venv/
  script: # Modify the commands below to build your repository.
    - pip install -r requirements.txt  # Install dependencies
    - nosetests --with-coverage  --cover-html # Run tests with coverage
  artifacts:
    paths:
      - cover/ # Store coverage reports as artifacts
```

**Optional:** You can add tags to the `.gitlab-ci.yml` file to assign specific runners to jobs. If you use tags, ensure they match exactly when registering the runner.

### Step 7. Setup the GitLab runner

- Follow the instructions [here](https://docs.gitlab.com/ee/tutorials/create_register_first_runner/#create-and-register-a-project-runner) **up to step 7** to create a GitLab Runner for your repository

- Choose **Linux** under operating systems

- Copy the **authentication token** generated during the process. You will need it for **Step 9**.

### Step 8. Deploy GitLab runner in a Docker container
Run the following command to deploy the GitLab Runner as a Docker container:

```bash
docker run -d --name gitlab-runner --restart always \
-v /srv/gitlab-runner/config:/etc/gitlab-runner \
-v /var/run/docker.sock:/var/run/docker.sock \
gitlab/gitlab-runner:latest
```

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
on **Mac OS**, replace `/Users/Shared/` with `/srv/`
:::


Check that gitlab-runner container is running with
``` bash
docker ps -a
```

### Step 9. Register the runner using authentication token

Run the following command to register your runner and configure it to deploy in a Docker container on your server.

```bash
docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register
```

:::{.callout-note appearance="simple" icon="false"}
## {{< fa info-circle >}} Note
on **Mac OS**, replace `/Users/Shared/` with `/srv/`
:::

You will be prompted to answer the following questions:
 Copy
```bash
Enter the GitLab instance URL (for example, https://gitlab.com/):
https://gitlab.tudelft.nl

Enter the registration token:
xxxxxxxxxxxxxxx

Verifying runner... is valid                        runner=xxxxxxx

Enter a name for the runner. This is stored only in the local config.toml file:
[xxxxxxx]: example-runner

Enter an executor: instance, kubernetes, docker-windows, docker-autoscaler, parallels, shell, ssh, virtualbox, docker+machine, custom, docker:
docker

Enter the default Docker image (for example, ruby:2.7):
python:3.12.3

Runner registered successfully. 

Feel free to start it, but if it is running already the config should be automatically reloaded!

Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml"
```

### Step 10. Verify the CI/CD Pipeline

##### 1. Check Runner Status:

- Go to your repository’s Settings > CI/CD.
- Under Runners, expand the section to confirm that your runner is active (indicated by a green dot). This means the runner is ready to execute jobs, but it requires a trigger to start.

##### 2. Trigger the Pipeline:

- Make a new commit to your GitLab repository. This will automatically trigger the pipeline to run.

##### 3. Monitor Pipeline Status:

- After the new commit, navigate to CI/CD > Pipelines in your project.
- Check the status of your pipeline:
    - A green "passed" status with a checkmark means your pipeline ran successfully. Congratulations!
    - A red "failed" status indicates an error. Review the error message to troubleshoot. Common issues include incorrect formatting in the .gitlab-ci.yml file or misconfigured test definitions.

<img src="https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/f7aadbc87f49d31de4da37a2f8a76ef3/Screen_Shot_2020-11-17_at_11.56.41.png" width="600" style="display: block; margin: 0 auto;">

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more
This guide was created using multiple references on GitLab runner and Docker. If you would like more information or details, please refer to the links below.<br>
- [Hostinger - how to install docker on Ubuntu](https://www.hostinger.com/tutorials/how-to-install-docker-on-ubuntu)<br>
- [Cloudclone - How to install docker on Ubuntu](https://cloudcone.com/docs/article/how-to-install-and-run-docker-on-ubuntu-20-04-lts/)<br>
- [Digitalocean- How to install docker on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)<br>
- [GitLab - Use CI/CD to build your application](https://docs.gitlab.com/ee/topics/build_your_application.html)<br>
- [GitLab - Docker executor](https://docs.gitlab.com/runner/executors/docker.html#define-image-and-services-from-gitlab-ciyml)<br>
- [TU Delft - GitLab CI/CD YAML syntax reference](https://gitlab.tudelft.nl/help/ci/yaml/index.md)<br>
- [GitLab - CI/CD jobs in Docker containers](https://docs.gitlab.com/ee/ci/docker/using_docker_images.html)<br>
- [Semaphore - Introduction to CI/CD pipeline](https://semaphoreci.com/blog/cicd-pipeline )<br>
:::