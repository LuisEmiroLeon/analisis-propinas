# Modelo Multivariable
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Codificar texto a números: Male=1, Female=0, Smoker Yes=1 No=0
df['sex_code'] = (df['sex'] == 'Male').astype(int)
df['smoker_code'] = (df['smoker'] == 'Yes').astype(int)

model2 = LinearRegression()
model2.fit(df[['total_bill', 'size', 'sex_code', 'smoker_code']], df['tip'])
r2 = r2_score(df['tip'], model2.predict(df[['total_bill','size','sex_code','smoker_code']]))
print(f"R² con 4 features: {r2:.4f}") # Resultado: 0.4688

