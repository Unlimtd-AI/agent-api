#!/bin/bash

############################################################################
# Script to build the Docker image using Docker Buildx.
#
# Instructions:
# 1. Set the IMAGE_NAME and IMAGE_TAG variables to the desired values.
# 2. Ensure Docker Buildx is installed and configured.
# 3. Run 'docker buildx create --use' before executing this script.
#
# This script builds a multi-platform Docker image for linux/amd64 and linux/arm64.
# The image is tagged and pushed to the specified repository.
############################################################################

# Exit immediately if a command exits with a non-zero status.
set -e

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS_ROOT="$(dirname ${CURR_DIR})"
DOCKER_FILE="Dockerfile"
IMAGE_NAME="agno-agent-api"
IMAGE_TAG="latest"

REGISTRY=cr.eu-north1.nebius.cloud/e00gg36h3ta91x0e1d
FULL_IMAGE_NAME=$REGISTRY/$IMAGE_NAME:$IMAGE_TAG

echo "Running: docker buildx build --platform=linux/amd64,linux/arm64 -t $FULL_IMAGE_NAME -f $DOCKER_FILE $WS_ROOT --push"
docker buildx build \
   --platform=linux/amd64,linux/arm64 \
   -t $FULL_IMAGE_NAME \
   -f $DOCKER_FILE $WS_ROOT \
   --push
