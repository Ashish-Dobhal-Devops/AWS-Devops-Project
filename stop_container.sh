#!/bin/bash
set -e

# Collect the running container ID (If any)
containerid=`docker ps | awk -F " " '{print $1}'`

#Stop the running container (if any)
docker rm -f $containerid