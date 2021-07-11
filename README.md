# Docker
This is a repository with some experiments with Docker.

This app (wrote on python) only exposes the endpoint /docker in the port 8888

# Build the image
Run the next command to build the image

```
docker build -t mypythonapp:v0.0.1 .
```

# Run the image in a container
Run the next command to run the image built
```
docker run -d --name testing -p 8888:8888 mypythonapp:v0.0.1
```
Verify if the container is running:
```
docker ps
```
Should be show the next output:
```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                       NAMES
6993cd3d5f57   mypythonapp:v0.0.3   "flask run --port=88…"   28 minutes ago   Up 27 minutes   0.0.0.0:8888->8888/tcp, :::8888->8888/tcp   testing
```

# Verify the app in the browser
Go to your browser and put the next URL:
```
<IP Number of your machine>:8888
```
To see the JSON with information
```
<IP Number of your machine>:8888/docker
```