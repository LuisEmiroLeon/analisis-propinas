import pandas as pd
import joblib

COLS = ["total_bill","size","day_Fri","day_Sat","day_Sun","time_Dinner"]

class PredictorPropinas:
    def __init__(self, model_path="modelo_propinas.pkl"):
        self.model = joblib.load(model_path)
        self.r2 = 0.4675
        self.cols = COLS

    def _mapear(self, day, time):
        return {
            "day_Fri": 1 if day == "Fri" else 0,
            "day_Sat": 1 if day == "Sat" else 0,
            "day_Sun": 1 if day == "Sun" else 0,
            "time_Dinner": 1 if time == "Dinner" else 0
            }

    def predecir(self, total_bill, size, day, time):
        mapa = self._mapear(day, time)
        data = pd.DataFrame([[total_bill, size,
                              mapa["day_Fri"], mapa["day_Sat"],
                              mapa["day_Sun"], mapa["time_Dinner"]]],
                              columns=self.cols)
        pred = float(self.model.predict(data)[0])
        return round(pred, 2)

if __name__ == "__main__":
    p = PredictorPropinas()
    print(f"R2: {p.r2}")
    print(f"$20,2,Fri,Dinner: ${p.predecir(20, 2, 'Fri', 'Dinner')}")
