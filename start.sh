# python -m venv venv
source venv/bin/activate
# pip install -r requirements.txt
uvicorn app.api.main:app --host 0.0.0.0 --port 8000