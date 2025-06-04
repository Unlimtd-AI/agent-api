#!/bin/bash

############################################################################
# Container Entrypoint script
############################################################################

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

curl -fsSL https://ollama.com/install.sh | sh

# Add to PATH for both root and vscode user
PATH="$HOME/.local/bin:${PATH}"

nohup ollama serve > /tmp/ollama.log 2>&1 &

echo "Pull Models"
sleep 2

# For chat
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:70b

# For tools
ollama pull llama3.1:8b
ollama pull llama3.1:70b

# For embedding
ollama pull llama2:7b
ollama pull llama2:70b

echo ">>> Hello World!"

while true; do sleep 18000; done
