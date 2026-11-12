## Execução local
```bash
pip install -r requirements-dev.txt
python -m pytest -q
python scripts/gate.py
uvicorn app.main:app --reload
```