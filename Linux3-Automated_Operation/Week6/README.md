# **Docker**
- light virtual machine
- images and containers
    - image is like the design drawing, can use to run in containers
    - 1 image can create multiple containers
    - image included environment,code,everything need to run a service/program
- online docker image name style
    - `part1 | part2 | part3 : tag`
        - `part1` : repo,docker hub(can ignore),self
        - `part2` : name,ex: tom,mary. docker official can ignore
        - `part3` : image's name
        - `tag` : version, default is latest
## **Techniques**
- use namespace to segregate all virtual machines
    - PID namespace,network namespace,user namespace, IPC namespace,mount namespace, UTS namespace,...
- cgroups : 用以共享硬體資源
- aufs
    - file system of docker, use stack 
- image : only readable
    - If want to add new functions, can only add at the top layer and make it into new image

## **Install docker on centos**
1. Remove old version of docker
```
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```
2. Set up the repository
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

3. Install Docker Engine, containerd, and Docker Compose
```
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
## **docker commands**
1. Show all local docker images
```
docker images
```
2. Current working container
```
docker ps
```
- `docker ps -a` : can show all containers
- `docker ps -a -q` : show all container's id
3. To run a image into container
```
docker run image
```
- `docker run hello-world`
- `docker -i -t --name=centos9-1 centos:centos7 /bin/bash`
    - `-i` : interactive with container
    - `-t` : terminal
    - `/bin/bash` : to run on new bash or will stop after done
4. To remove container
```
docker rm container_id/name
```
- `docker rm $(docker ps -a -q)` : rm all exited containers
- `docker rm -f $(docker ps -a -q)` : rm all containers

5. To search online's image, or can go to docker hub
```
docker search image_name
```
6. To go into running container 
```
docker exec -it container_id/name /bin//bash
```
7. To exit container
```
exit
```
- exit and let container keep running
    - CTRL + Q (Windows)
    - fn + control + Q (Mac)
8. Create new image from container
```
docker commit target_container_id new_image_name:tag
```
