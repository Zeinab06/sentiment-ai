# Active ton venv d'abord
source venv/bin/activate  # ou .venv/bin/activate

# Installe les nouvelles dépendances
pip install -r requirements.txt

# Lance l'app
python3 -m uvicorn src.main:app --reload --port 8000