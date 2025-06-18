# Docker

[Tutorial](https://docker-curriculum.com/)

> Docker is a tool that allows easy deployment of applications in a sandbox (called containers)

## Image

Template for a Docker container

- Contains everything needed to run an application
- immutable, once built it does not change

Think of it like 
- a software package
- a recipe

ex.
`docker pull nginx`
- Downloads the Nginx image
- Contains everything needed to run Nginx

## Container

A running instance of a Docker image
  
- Mutable, can modify it while it's running (for logs, temp files runtime data, etc.)
- Contains the image + a writable layer
- Many containers can be made from the same image

Think of it like an 
- executable built from the software
- cooked dish made from the recipe

p.s. Still exists even if not running

## Volumes

Persist data (store in the local filesystem) that a container generates

Volumes will be mounted to the container for services to use

## Dockerfile

Custom image instructions

## Commands

### Pull

`docker pull busybox`

Fetches the image from Docker registry

### Build

`docker build -t my_image .`

Builds an image

Flags
- `-t` tag image with a name

### Run

`docker run my_image`

Creates a container based off the image
- p.s. Container runs until you stop it

Flags
- `--name my_container_name` names container
- `-w /app` make app the working directory
- `--rm` auto removes the container after it exits
- `-v` volume mount (share/persist a folder between container and your computer) " 
  - POWERSHELL: `-v "${PWD}:/app` mounts your current local folder (`${PWD}`) into the container at `/app`
- `-d` detached
- `-it` interactive terminal
  - `-i` interactive (keep STDIN open so you can type commands)
  - `-t` allocate a TTY (terminal)
- `-p` set port number (ex. 8089)

### Compose | Save run options | docker-compose.yaml

`docker compose up -d`

docker-compose.yaml file tells Docker how to run your multi-container application
- this allows you to easily delete everything and restart
  - WARNING: if the database container is deleted all the data in the database is also deleted
- NON-INTERACTIVE, so if you want to use a shell do `docker compose run -rm my_container`

- Optional
  - `docker compose up -d` Builds (if needed) and starts containers
  - `docker compose logs -f` View logs
  - `docker compose down` Stop containers
  - `docker compose ps` View containers
  - `docker compose run sap_cds`
    - `--rm` remove the container when stopped
    - `--service-ports` opens the ports in the yaml

#### Auto Update After Change | Compose Watch

`docker compose watch`

[Documentation](https://docs.docker.com/compose/how-tos/file-watch/)

Build, run, and automatically update the containers when the code is changed

### Containers

List running containers

`docker ps`

Run container again with a command

`docker exec [flags] CONTAINER_NAME_OR_ID COMMAND`

Stop

`docker stop CONTAINER_NAME_OR_ID`

Remove

`docker rm CONTAINER_NAME_OR_ID`

Stop & Remove

`docker rm -f CONTAINER_NAME_OR_ID`

Remove all containers

`docker rm -f $(docker ps -a -q)`
