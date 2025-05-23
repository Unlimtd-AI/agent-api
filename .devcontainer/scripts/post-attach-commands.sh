# ------------------------------- SETUP PYTHON VIRTUAL ENVIRONMENT -------------------------------
./scripts/dev_setup.sh
source .venv/bin/activate

## Generate requirements.txt
./scripts/generate_requirements.sh

# ./scripts/generate_requirements.sh upgrade

uv pip install -r requirements.txt

# ------------------------------- SERVE OLLAMA ---------------------------------------------
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