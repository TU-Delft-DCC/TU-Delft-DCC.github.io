# Working remotely with computers
As mentioned in the [introduction of this "Research Computing Guides"](../01_README.md), you might find yourself in a situation where you need to work with a remote virtual machine provided by TU Delft, a server or a cluster. In many of the cases you will have to use the command line to work remotely.

**Some things to keep in mind:**
- A remote computer is not a server even though it could be.
- Remote computers can also be Virtual Machines working on actual computers/hardware
- Servers are meant to run continuously and provide a "service" often via http, to "client computers". It implies some understanding of networks, http protocols, and server software.

For more information on how to get a Virtual Private Server read [this guide](./01_VPS_request.md)

## Some use cases and examples
1. You might want to run jobs in a remote machine instead of your desktop, specially when the computational task can take a lot of resources. 
2. You might want to run an instance of a service. For example a geoserver, a postgresql database for your lab or research group, others.
3. You need to use a cluster to run simulations or process large data sets.
4. You want to setup a server to host a static website or web application. 

## Basic skills 
- Working with the command line, shell scripting and linux.
- Working remotely and securely using ssh.
- Transfer files from one computer to another.
- Working with containers.

## Bonus
- Understanding of linux
- Understanding of how the web and http works
- Understanding of security
- Docker or similar
- Kubernetes 