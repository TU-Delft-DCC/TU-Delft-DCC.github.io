# Why and when to use containers
Containers and more, specifically docker containers are all over the place, just like git repositories. Containers make our lives easy when it comes to reproducing computational environments, testing someone else's software efficiently, deploying software and services securely, but also scaling software and maintaining it. 

If you happen to have an open source software and you want to facilitate that others can run it, test it, assess it or even contribute to it. Having a some `Dockerfile`, or `docker-compose.yml` file within your source code can be of great help. Specially when you are developing a complex application.

Containers are another level of portability, reusability and reproducibility!

[The company Docker](https://www.docker.com/resources/what-container) say's on its website:
> (Why, when to use them) Use containers to Build, Share and Run your applications

> (What is a container) A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. Container images become containers at runtime.

## Some things you should be aware of
- Docker is not the only solution to create and manage containers.
- Managing containers networking and making runtimes available via http ports can be challenging at the beggining.
- In the next page we will be using [Podman](https://podman.io/), as it has othe advantages that we care about at TU Delft.
- [Singularity](https://sylabs.io/) a container runtime that is explicitly designed for data processing.
- If you happen to have complex software composed of multiple micro-services(database, backend, frontend) or if you want to have a solution that is scalable and easy to deploy in a cluster or in the cloud, you should look into [Kubernetes](https://kubernetes.io/).