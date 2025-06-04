#!/bin/bash

############################################################################
# Setup Ollama Models script
############################################################################

# Exit immediately if a command exits with a non-zero status.
set -e

# echo "Serve Ollama"
sudo nohup ollama serve > /tmp/ollama.log 2>&1 &

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