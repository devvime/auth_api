echo "Iniciando servidor de sesenvolvimento"

source venv/bin/activate
uvicorn app.main:app --reload