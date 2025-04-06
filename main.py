from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    consommation_annuelle: float
    production_pv: float
    prix_batterie: float
    prix_borne: float
    tarif_electricite: float

@app.post("/calculate/lfp")
def calculate_lfp(data: InputData):
    rendement = 0.9
    economie = min(data.production_pv, data.consommation_annuelle) * data.tarif_electricite * rendement
    tri = data.prix_batterie / economie
    return {
        "solution": "Batterie LFP",
        "tri": round(tri, 2),
        "economie_annuelle": round(economie, 2)
    }

@app.post("/calculate/ve")
def calculate_ve(data: InputData):
    rendement = 0.85
    economie = min(data.production_pv, data.consommation_annuelle) * data.tarif_electricite * rendement * 0.9
    tri = data.prix_borne / economie
    return {
        "solution": "Véhicule Électrique V2H",
        "tri": round(tri, 2),
        "economie_annuelle": round(economie, 2)
    }

@app.post("/calculate/compare")
def compare(data: InputData):
    lfp = calculate_lfp(data)
    ve = calculate_ve(data)

    recommendation = "La batterie LFP est plus rentable." if lfp["tri"] < ve["tri"] else "Le VE V2H est plus rentable."
    return {
        "lfp": lfp,
        "ve": ve,
        "recommendation": Ajout de main.py
    }
