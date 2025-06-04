#!/bin/bash

############################################################################
# Setup Ollama Models script
############################################################################

# Exit immediately if a command exits with a non-zero status.
set -e

# Set permissions for the .ollama directory
# Ensure the app directory and .ollama directory exist with correct permissions


sudo mkdir -p /app/.ollama

sudo chown -R app:app /app/
sudo chmod -R 755 /app/
sudo chmod 700 /app/.ollama

# echo "Serve Ollama"
nohup ollama serve > /tmp/ollama.log 2>&1 &

sleep 5

echo "Pull Models"
# # For chat
ollama pull deepseek-r1:8b
# ollama pull deepseek-r1:70b

# For tools
ollama pull llama3.1:8b
# ollama pull llama3.1:70b

# For embedding
ollama pull llama2:7b
# ollama pull llama2:70b