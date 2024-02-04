#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull ashishdevops007/python-flask-app-aws-devops

# Run the Docker image as a container
docker run -d -p 7777:7777 ashishdevops007/python-flask-app-aws-devops
