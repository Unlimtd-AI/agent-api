# ------------------------------- SETUP PYTHON VIRTUAL ENVIRONMENT -------------------------------
./scripts/dev_setup.sh
source .venv/bin/activate

## Generate requirements.txt
./scripts/generate_requirements.sh

# ./scripts/generate_requirements.sh upgrade

uv pip install -r requirements.txt