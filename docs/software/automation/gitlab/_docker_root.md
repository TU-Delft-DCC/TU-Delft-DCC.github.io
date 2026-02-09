## Relocate Docker directory
To relocate the Docker root directory, complete the following steps as root or a user with "sudo all" privileges:

1. Stop the Docker services:
    
    ```bash
    sudo systemctl stop docker
    sudo systemctl stop docker.socket
    sudo systemctl stop containerd
    ```

2. Create the necessary directory structure into which to move Docker root by running the following command. In this example, we will move the Docker root to `/data/docker`:  

    ```bash
    sudo mkdir -p /data/docker
    ```

3. Move the existing Docker data into the new directory structure:

    ```bash
    sudo mv /var/lib/docker/* /data/docker/
    ```

4. Edit the file `/etc/docker/daemon.json`. If the file does not exist, create the file with the following command:

    ```bash
    sudo nano /etc/docker/daemon.json
    ```
    Add the following content to the file and save the file:

    ```json
    {
      "data-root": "/data/docker"
    }
    ```

5. Restart the Docker services:

    ```bash
    sudo systemctl start docker   
    ```
    After you run the command, all Docker services through dependency management will be started automatically.

6. Validate the new Docker root location

    ```bash
    sudo docker info -f '{{.DockerRootDir}}'
    ```
    The output should be similar to the following, indicating that the Docker root directory has been successfully relocated:

    ```
     /data/docker
    ```