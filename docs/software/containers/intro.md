---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-dd]
date: 2024-11-14

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Introduction to containers

# Short description of the document, will be used in the listing
description: Containers are a way to package software and its dependencies into a single unit that can run consistently across different environments.
hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Elviss Dvinskis
author_2: Maurits Kok

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1:
maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
categories: 
 - Containers
 - Reproducibility

---

## Introduction to containers
Just as you document your software dependencies, it may be useful to record and manage your development environments. This may involve documenting the specific configurations, tools, and versions used during development to ensure that everything runs consistently across different setups. 

By recording your environments, you create a reproducible framework that significantly reduces the infamous *"it works on my machine"* syndrome, where code runs on one machine but fails on others.

Environment management includes specifying your operating system, programming language (and their versions), system libraries, and any other software or tools required. This practice not only helps in maintaining consistency across development, testing, and production stages but also streamlines onboarding for new team members, as they can quickly set up their environment to match the recorded specifications.

## Why use containers?
Containers remove the need for manual installation or troubleshooting, ensuring that software runs consistently across different machines. Containers act as a self-contained unit that bundle everything needed to run software, including dependencies and system libraries, into a single package known as an **image**.

The definition files, like Dockerfiles or Singularity definition files, are essentially instruction manuals to build a container image.

:::{.callout-tip collapse="true"} 
## **An analogy for a container image**
Consider a container image like a detailed movie script that outlines every scene. When the movie is shot (i.e., the container is executed), a temporary set is built where all filming occurs in a controlled environment. Once filming ends, the set is dismantled, but the script remains unchanged, allowing the software to be re-executed with the same consistent results every time, just as each scene is reproduced faithfully with the same script.
:::

Containers can be useful for various purposes:

- If installing certain software is complex or incompatible with your operating system, you can use a pre-built container image to run the software seamlessly.
- Likewise, if you want to make sure that the people you are working with use the exact same environment, you could provide them with an image of your container.
- If you are facing issues due to different system architectures you can distribute a definition file to build an image that tailors to different machines. While it might not replicate your environment exactly, it often provides a sufficiently close alternative.

Popular containerisation solutions:

- [Docker](https://www.docker.com) and [Podman](https://podman.io) are great for general software development.
- [Singularity](https://sylabs.io/docs/) is tailored for high-performance computing (HPC) environments.
- For managing and scaling containers across multiple machines, tools like [Kubernetes](https://kubernetes.io/) are commonly used.

[Docker's official samples and examples](https://github.com/dockersamples)

:::{.callout-note}
## **Further reading**

- [Recording environments lesson on CodeRefinery](https://coderefinery.github.io/reproducible-research/environments/)
- [Carpentries incubator lesson on Docker](https://carpentries-incubator.github.io/docker-introduction/)
- [Guides and manuals for Docker](https://docs.docker.com)
- [Singularity documentation](https://singularity-docs.readthedocs.io/en/latest/)

:::

## Advantages and disadvantages of using containers
Containers have gained widespread popularity due to their significant benefits in solving various challenges:

- They enable a smooth transition of workflows across different operating systems and configurations.
- They address the common issue of software behaving differently on different machines by providing a consistent runtime environment.
- For software with nested dependencies, containers can be a vital tool for ensuring long-term reproducibility.
- Containers package software in isolated files, simplifying management, installation, and removal compared to traditional methods.

But it is important to consider the downsides:

- The convenience of containers might lead to overlooking underlying software installation issues and not adhering to good software development practices.
- There's a risk of creating a new form of dependency - software that *"only works in a specific container"*, which could limit flexibility and interoperability.
- Container images can grow in size substantially, especially if not carefully managed.
- Modifying existing containers can sometimes be challenging, requiring a good understanding of the container's configuration.
- Ensuring container security is vital, as misconfigurations can expose vulnerabilities.

:::{.callout-caution}
## **Caution**
It's crucial to source your container images from reputable and official channels. There have been instances where images were found to be malicious, so it is very important to apply the same caution as when installing software packages from untrusted sources. 

Always download images from trusted sources like [Docker Hub](https://hub.docker.com). Utilize container scanning tools, such as [Docker scanning tools](https://www.docker.com/blog/automating-your-containers-security-scanning/) to mitigate risks from malicious images.
:::
