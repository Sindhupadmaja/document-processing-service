# Document Processing Service

An API that accepts documents, validates uploads, extracts structured fields, persists job state/results, and exposes an asynchronous worker-style processing flow.

## Tech stack
fastapi==0.115.6
uvicorn[standard]==0.34.0
python-multipart==0.0.20
SQLAlchemy==2.0.36
pydantic==2.10.4
pytest==8.3.4
httpx==0.28.1


## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate | macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Tests
```bash
pytest -q
```

## Portfolio progression
This project is intentionally structured so you can learn it from the fundamentals upward. Start with the README, run the tests, inspect `app/`, then improve one layer at a time.

## Environment
Copy `.env.example` to `.env` and change values for a real deployment. Never commit secrets.
