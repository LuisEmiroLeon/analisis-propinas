# Machine Learning - Regresión lineal simple
# Regresión lineal simple con scikit-learn

import pandas as pd
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

model = LinearRegression()
model.fit(df[['total_bill']], df['tip'])

print(model.predict([[50]])) # Imprime la predicción de propina para una cuenta total de 50
print(f"Coeficiente: {model.coef_[0]}, Intercepto: {model.intercept_}")  # Imprime el coeficiente de la regresión lineal

# propina = 0.105 * total_bill + 0.92
# Coeficiente 0.105: Por cada $1 extra en la cuenta, la propina sube ∼10.5 centavos (10.5% de propina promedio)
# Intercepto 0.92: Propina base de $0.92 aunque la cuenta sea pequeña
# Predicción $50 -> $6.17: Cuenta de $50 deja $6.17 (12.3%)
