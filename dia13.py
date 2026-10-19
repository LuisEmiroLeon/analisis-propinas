# Analisis con grupo de datos con pandas (groupby)
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

df['propina_pct'] = df['tip'] / df['total_bill'] * 100 # Calcula el porcentaje de propina y lo agrega como una nueva columna al DataFrame

print(df.groupby('sex')['propina_pct'].mean()) # Imprime el promedio de propina por sexo
print(df.groupby('smoker')['propina_pct'].mean()) # Imprime el promedio de propina por fumador
print(df.groupby('time')['propina_pct'].mean()) # Imprime el promedio de propina por tiempo (almuerzo o cena)
print(df.groupby('day')['propina_pct'].mean()) # Imprime el promedio de propina por día de la semana