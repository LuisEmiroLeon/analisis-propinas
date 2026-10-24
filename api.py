
import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

MODEL_PATH = "modelo_propinas.pkl"
COLS = ["total_bill","size","day_Fri","day_Sat","day_Sun","time_Dinner"]

if not os.path.exists(MODEL_PATH):
    tips = sns.load_dataset("tips")
    df = pd.get_dummies(tips, columns=["sex","smoker","day","time"], drop_first=True)
    X = df[COLS]
    y = df["tip"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="API Propinas Luis - Dia 25",
    description="Modelo ganador R2 0.4675: total_bill + size + day_Fri/Sat/Sun + time_Dinner",
    version="1.0.0"
)

class PrediccionRequest(BaseModel):
    total_bill: float
    size: int
    day: str
    time: str

    class Config:
        json_schema_extra = {
            "example": {
                "total_bill": 20.0,
                "size": 2,
                "day": "Fri",
                "time": "Dinner"
            }
        }

@app.get("/")
def home():
    return {
        "mensaje": "API Propinas Dia 25 - R2 0.4675",
        "modelo": COLS,
        "docs": "/docs",
        "ejemplo": {"total_bill":20, "size":2, "day":"Fri", "time":"Dinner"}
    }

@app.post("/predict")
def predict(req: PrediccionRequest):
    day_Fri = 1 if req.day == "Fri" else 0
    day_Sat = 1 if req.day == "Sat" else 0
    day_Sun = 1 if req.day == "Sun" else 0
    time_Dinner = 1 if req.time == "Dinner" else 0

    data = pd.DataFrame([[req.total_bill, req.size, day_Fri, day_Sat, day_Sun, time_Dinner]], columns=COLS)
    pred = model.predict(data)[0]

    return {
        "propina_estimada": round(float(pred), 2),
        "r2_modelo": 0.4675,
        "input": req.model_dump(),
        "columnas_usadas": COLS
    }
