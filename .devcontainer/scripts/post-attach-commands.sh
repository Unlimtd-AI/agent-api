# ------------------------------- SETUP PYTHON VIRTUAL ENVIRONMENT -------------------------------
./scripts/dev_setup.sh
source .venv/bin/activate

## Generate requirements.txt
./scripts/generate_requirements.sh
# ./scripts/generate_requirements.sh upgrade

uv pip install -r requirements.txt

# ------------------------------- SERVE OLLAMA ---------------------------------------------
nohup ollama serve > ollama.log 2>&1 &

echo "Pull Models"
sleep 2

ollama pull deepseek-r1:8b
ollama pull llama3.1:8b # For tools
ollama pull llama2:7b # For embedding