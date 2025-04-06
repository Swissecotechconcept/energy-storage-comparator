# Energy Storage Comparator – API REST

API FastAPI pour comparer :
- Batterie stationnaire LFP
- Véhicule électrique avec borne bidirectionnelle (V2H)

## Endpoints

- `POST /calculate/lfp`
- `POST /calculate/ve`
- `POST /calculate/compare`

## Test local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
