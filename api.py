import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import os
from database import init_db, guardar_prediccion

MODEL_PATH = "modelo_propinas.pkl"
COLS = ["total_bill","size","day_Fri","day_Sat","day_Sun","time_Dinner"]

# Crear DB si no existe
init_db()

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="API Propinas Luis - Dia 29 DB",
    description="Modelo R2 0.4675 + SQLite - guarda historial",
    version="1.1.0"
)

class PrediccionRequest(BaseModel):
    total_bill: float
    size: int
    day: str
    time: str

@app.get("/")
def home():
    return {
        "mensaje": "API Dia 29 - R2 0.4675 + DB",
        "docs": "/docs",
        "historial": "/historial"
    }

@app.post("/predict")
def predict(req: PrediccionRequest):
    day_Fri = 1 if req.day == "Fri" else 0
    day_Sat = 1 if req.day == "Sat" else 0
    day_Sun = 1 if req.day == "Sun" else 0
    time_Dinner = 1 if req.time == "Dinner" else 0

    data = pd.DataFrame([[req.total_bill, req.size, day_Fri, day_Sat, day_Sun, time_Dinner]], columns=COLS)
    pred = float(model.predict(data)[0])

    # GUARDAR EN DB - Esto es lo nuevo del Día 29
    guardar_prediccion(req.total_bill, req.size, req.day, req.time, round(pred,2))

    return {
        "propina_estimada": round(pred, 2),
        "r2_modelo": 0.4675,
        "guardado_en_db": True,
        "input": req.model_dump()
    }

@app.get("/historial")
def historial():
    import sqlite3
    conn = sqlite3.connect("propinas.db")
    c = conn.cursor()
    c.execute("SELECT id, total_bill, size, day, time, propina_estimada, fecha FROM predicciones ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()
    return {"total": len(rows), "ultimas_predicciones": rows}