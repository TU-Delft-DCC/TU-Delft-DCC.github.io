<!-- ---
section: gitlab
title: CI with Gitlab
author_1: Ashley Cryan
author_2: Maurits Kok
--- -->

# Continuous Integration with GitLab

## Background
If you happen to be working with TU Delft GitLab instance and you want to implement DevOps or CI/CD pipelines, then you need to install a GitLab runner on your own. This should runner should be in a server, responding to changes such as commits or pull requests in your GitLab repository.

## Quick overview of how it works
In order to be ready to run CI/CD pipeline, a gitlab-runner Docker container is running on the server all the time. When a new commit is made in the GitLab repository, this triggers the CI/CD process to run a job (e.g., unit test) based on the pipeline defined in the .gitlab-ci.yml file in the repository. The container used to carry out the CI/CD tests is defined in the .gitlab-ci.yml file in the first line, and spawned from within the continuously running gitlab-runner container. In our example, we define `image:python:3.12.3` so every time a commit is made in the repository, a new container based on the python:3.12.3 Docker image is started and used to run tests on the python scripts and generate artifacts as defined in the .gitlab-ci.yml file.

![](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/711ac593ec886bd9216dff0591a82e6f/Untitled_Document__31_.png)

## What this documentation will help achieve
The documentation below will help you deploy GitLab runner in a Docker container on a server to automatically run CI/CD tests and store artifacts every time there is a new commit to a GitLab repository.

## Prerequisites
**Server:** This example uses a server to run the whole process. You can request a server from TU Delft ICT service following these directions [here](../VPS_request.md). It is useful to set this up on a server so that Docker can be running continuously, and be ready to run CI/CD tests whenever a new commit occurs in the repository.

**Docker:** We use a Docker container to run the GitLab runner and initialise the CI/CD pipeline.

**Gitlab runner:** (from GitLab documentation) "Runners are the agents that run the CI/CD jobs that come from GitLab. When you register a runner, you are setting up communication between your GitLab instance and the machine where GitLab Runner is installed. Runners usually process jobs on the same machine where you installed GitLab Runner." [Link](https://docs.gitlab.com)

**GitLab repository:** A remote repository that can store your code and keeps track of your project development. You're on one right now! :) If you haven’t already, you use your netID and password to login to TU Delft’s GitLab instance at gitlab.tudelft.nl and create a repository containing your project code.

**CI/CD pipeline:** “A CI/CD pipeline automates your software delivery process. The pipeline builds code, runs tests (CI), and safely deploys a new version of the application (CD)” [Link](https://semaphoreci.com/blog/cicd-pipeline).

## Tools/Software
* GitLab (TU Delft instance)
* Docker
* gitlab-runner Docker image

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
If you don't have a VPS already, you can request one from TU Delft ICT. Instructions for requesting a server and storage from ICT can be found under [Remote servers/Request a Virtual Private Server](../VPS_request.md).

We recommend the following configuration for configuring a GitLab runner:

- Basic Configuration 4 (Ubuntu)
- No additional **ports** need to be configured for deploying a GitLab runner with Docker.
- Additional space if your Docker images are larger than ~10Gb.

### Step 2. Connect to the server via ssh
The email response from Sysadmin@TUDelft.nl confirming the successful deployment of your server should contain instructions to connect via ssh.

The default login procedure is to connect to the Bastion host (an intermediary server) and then to your server, so it is a two-step process. Please check your email for Steps A and B as described by ICT admin.

You can also connect to your server using Putty (Windows) or, on Mac/Linux, configure one-step access by storing ssh keys between your local machine and your server and designating an alias.

When you are successfully connected, you should see in your terminal/command prompt something like this:

![](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/048a06a817852a399c697582ae1e3a08/Screen_Shot_2020-11-17_at_10.30.31.png)

### Step 3. Install Docker on the server

Servers often do not come with Docker installed, so you may need to do it by yourself. To check whether Docker is installed, run `docker --version`. If you get an error message, you can install it using the following commands:

`sudo su` (this will give you the root access)
`apt install docker.io`

Now, Docker is installed. You can check if it is installed successfully by again typing `docker --version` in the terminal. The result should show the version of Docker you just installed.

### Step 4. Pull the gitlab-runner Docker image
In order to run CI/CD jobs for your repository, you need to install GitLab Runner. GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline. Rather than install GitLab Runner directly on the server, we will run a lightweight version of it as a Docker container. To do so, we first need to pull the gitlab-runner Docker image by running:

`docker pull gitlab/gitlab-runner`

You can check whether it was successful by running `docker images` - you should see the gitlab/gitlab-runner image listed in the output.

### Step 5. Create a unit test function stored as a file in the repository

### Step 6. Set up the CI by configuration of the .gitlab-ci.yml file

This file in the root of your repository defines what CI/CD tests to run upon each new commit. It does this by prescribing what container to run, what scripts to run inside the container, and what things to store as artefacts.

In the first line of the file, you can write `image: <image_name>:<tag>` to indicate you want to run the runner in a Docker container container.  `<image_name>` should be replaced by the name of the image you want to use to start a container and `<tag>` should be replaced by the tag of the image you want to use(image names can be found on DockerHub). Tag will be set to `latest` by default.

**Important:** The file must be named exactly `.gitlab-ci.yml` so it will be recognizable by GitLab runner. Below is an example .gitlab-ci.yml file.

```yaml
# This is a sample build configuration for Python.
# Check our guides at https://confluence.atlassian.com/x/x4UWN for more examples.
# Only use spaces to indent your .yml configuration.
# -----
test:
  # You can specify a custom docker image from Docker Hub as your build environment.
  image: python:3.12.3
  cache:
    paths:
      - .cache/pip
      - venv/
  script: # Modify the commands below to build your repository.
    - pip install -r requirements.txt
    - nosetests --with-coverage  --cover-html
  artifacts:
    paths:
      - cover/
```


Tags can be added as a final section in your .gitlab-ci.yml file (they are optional, we didn’t enter any in this example). You then need to enter these tags exactly when registering the runner.

### Step 7. Setup the GitLab runner

- Follow the instructions [here](https://docs.gitlab.com/ee/tutorials/create_register_first_runner/#create-and-register-a-project-runner) **till step 7** to create a GitLab runner for your repository

- Choose 'Linux' under operating systems

- Copy the authentication token generated and keep it handy. It will be required in Step 9.

### Step 8. Deploy GitLab runner in a Docker container

```bash
docker run -d --name gitlab-runner --restart always \
-v /srv/gitlab-runner/config:/etc/gitlab-runner \
-v /var/run/docker.sock:/var/run/docker.sock \
gitlab/gitlab-runner:latest
```

**on Mac OS, use /Users/Shared/ instead of /srv/**

Check that gitlab-runner container is running using `docker ps -a`

### Step 9. Register the runner using authentication token

Run the following command to register your runner and configure it to deploy in a Docker container on your server.

`docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register`

**on Mac OS, use /Users/Shared/ instead of /srv/**

In response to this command you will be prompted to answer the following questions

```bash
- GitLab URL: https://gitlab.tudelft.nl
- gitlab-ci token: Paste the authentication token generated in Step 7.
- Enter name of the runner: example-runner
- Type of executor: docker
- Default Docker image: Specify the same image as the one specified in the 'image' field of the .gitlab-ci.yml file.
```

See an example below.

```bash
docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register
```

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
julia:1.6
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!

Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml"
```

### Step 10. Check that the CI/CD process is activated and your pipeline runs successfully

- In your repository, navigate to Settings > CI/CD > Click on Expand under Runners: You should see that the runner is active as indicated by a green dot. This means that the CI pipeline is ready to run, but it needs to be triggered.

- In order to trigger the CI pipeline, you should make a new commit to the GitLab repository.

- After you have made a new commit to the repository, navigate to Your Project -> Build -> Pipelines to check the status of CI/CD pipelines connected to your repository. If you find a green message that says “passed” with a check mark then congratulations, your pipeline works! If you see a red message that says “failed”, check to see the error message associated with it - sometimes you need to reconfigure your .gitlab-ci.yml file to make sure it uses the correct formatting and defines the tests appropriately.

![](https://gitlab.tudelft.nl/acryan/data-management-for-researchers/-/wikis/uploads/f7aadbc87f49d31de4da37a2f8a76ef3/Screen_Shot_2020-11-17_at_11.56.41.png)


<!-- ## Notes and References
This guide was created using multiple references on GitLab runner and Docker. If you would like more information or details, please refer to the links below.
* https://www.hostinger.com/tutorials/how-to-install-docker-on-ubuntu
* https://cloudcone.com/docs/article/how-to-install-and-run-docker-on-ubuntu-20-04-lts/
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
* https://docs.gitlab.com/ee/topics/build_your_application.html
* https://docs.gitlab.com/runner/executors/docker.html#define-image-and-services-from-gitlab-ciyml
* https://gitlab.tudelft.nl/help/ci/yaml/index.md
* https://docs.gitlab.com/ee/ci/docker/using_docker_images.html
* https://semaphoreci.com/blog/cicd-pipeline -->
