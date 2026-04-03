# Project 1-1: Hello Docker

A foundational Docker project that demonstrates containerization basics by running a simple Python application in a Docker container.

## Project Overview

**Learning Objectives:**
- Understand Docker fundamentals (images, containers, Dockerfile)
- Build and run containerized Python applications
- Practice basic Docker CLI commands

**Tech Stack:**
- Docker
- Python 3.11

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Docker Desktop** (or Docker Engine)
   - Download: https://www.docker.com/products/docker-desktop/
   - Verify installation: `docker --version`
   - Expected output: `Docker version 20.x.x` or higher

2. **Git** (optional, for cloning)
   - Verify installation: `git --version`

## Project Structure

```
Project-1-1/
├── Dockerfile          # Docker image definition
├── hello.py           # Simple Python script
└── README.md          # This file
```

## Build Instructions

### Step 1: Navigate to Project Directory

```bash
cd /path/to/Project-1-1
```

### Step 2: Build the Docker Image

Build the Docker image with a tag name:

```bash
docker build -t hello-docker .
```

**What this does:**
- `docker build` - Builds a Docker image from the Dockerfile
- `-t hello-docker` - Tags the image with the name "hello-docker"
- `.` - Uses the current directory as build context

**Expected output:**
```
[+] Building 2.3s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [internal] load metadata for docker.io/library/python:3.11-slim
 => [1/3] FROM docker.io/library/python:3.11-slim
 => [2/3] WORKDIR /app
 => [3/3] COPY hello.py .
 => exporting to image
 => => naming to docker.io/library/hello-docker
```

### Step 3: Verify Image Creation

Check that the image was created successfully:

```bash
docker images | grep hello-docker
```

**Expected output:**
```
hello-docker   latest   abc123def456   2 minutes ago   125MB
```

## Run Instructions

### Method 1: Run Container (Default)

Run the container and see the output:

```bash
docker run hello-docker
```

**Expected output:**
```
Hello Docker World!
```

### Method 2: Run with Container Name

Run the container with a specific name for easier management:

```bash
docker run --name my-hello-container hello-docker
```

### Method 3: Run in Interactive Mode

Run the container and keep it alive for exploration:

```bash
docker run -it --name my-hello-container hello-docker /bin/bash
```

Then inside the container:
```bash
python hello.py
exit
```

## Verification Steps

### 1. Check Running Containers

```bash
docker ps
```

If the container already exited (because the script finishes quickly):
```bash
docker ps -a
```

### 2. View Container Logs

```bash
docker logs my-hello-container
```

### 3. Inspect Container Details

```bash
docker inspect my-hello-container
```

## Cleanup

### Remove Containers

```bash
# Remove a specific container
docker rm my-hello-container

# Remove all stopped containers
docker container prune
```

### Remove Images

```bash
# Remove the hello-docker image
docker rmi hello-docker

# Remove dangling images
docker image prune
```

## Common Issues and Solutions

### Issue 1: "docker: command not found"
**Solution:** Docker is not installed or not in your PATH. Install Docker Desktop and restart your terminal.

### Issue 2: "permission denied while trying to connect to the Docker daemon"
**Solution:**
- On Linux: Add your user to the docker group: `sudo usermod -aG docker $USER`
- On Mac/Windows: Ensure Docker Desktop is running

### Issue 3: "Conflict. The container name '/my-hello-container' is already in use"
**Solution:** Remove the existing container first:
```bash
docker rm my-hello-container
```

### Issue 4: Build fails with "python:3.11-slim not found"
**Solution:** Check your internet connection and Docker Hub access. Try pulling the base image manually:
```bash
docker pull python:3.11-slim
```

## Understanding the Dockerfile

```dockerfile
# syntax=docker/dockerfile:1          # Specifies Dockerfile syntax version
FROM python:3.11-slim                 # Base image (Python 3.11 slim variant)
WORKDIR /app                          # Sets working directory in container
COPY hello.py .                       # Copies hello.py from host to container
CMD [ "python", "./hello.py" ]       # Default command when container starts
```


## Resources

- [Docker Official Documentation](https://docs.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Python Docker Images](https://hub.docker.com/_/python)

## Part of Learning Roadmap

This is **Project 1-1** in the 10-month Data Engineering Learning Roadmap (Jan-Oct 2026).

**Month:** January (Week 2)
**Focus:** Docker Foundations
**Time Investment:** 1-2 hours
**Repository:** https://github.com/benwaraiotoko/DE-Learning-Projects/1-1_Hello-Docker
