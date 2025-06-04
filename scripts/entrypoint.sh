#!/bin/bash

############################################################################
# Container Entrypoint script
############################################################################

# Exit immediately if a command exits with a non-zero status.
set -e

# echo "Serve Ollama"
sudo nohup ollama serve > /tmp/ollama.log 2>&1 &

echo "Pull Models"
# # For chat
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:70b

# For tools
ollama pull llama3.1:8b
ollama pull llama3.1:70b

# For embedding
ollama pull llama2:7b
ollama pull llama2:70b

if [[ "$PRINT_ENV_ON_LOAD" = true || "$PRINT_ENV_ON_LOAD" = True ]]; then
  echo "=================================================="
  printenv
  echo "=================================================="
fi

if [[ "$WAIT_FOR_DB" = true || "$WAIT_FOR_DB" = True ]]; then
  dockerize \
    -wait tcp://$DB_HOST:$DB_PORT \
    -timeout 300s
fi

############################################################################
# Start App
############################################################################

case "$1" in
  chill)
    ;;
  *)
    echo "Running: $@"
    exec "$@"
    ;;
esac

echo ">>> Hello World!"

while true; do sleep 18000; done
