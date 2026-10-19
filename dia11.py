# Limpieza de datos con pandas
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
df['propina_pct'] = df['tip'] / df['total_bill'] * 100 # Calcula el porcentaje de propina y lo agrega como una nueva columna al DataFrame
print(df[df['propina_pct'] > 25]) # Imprime las filas donde 'propina_pct' es mayor a 25
print(df.sort_values('propina_pct', ascending=False).head()) # Imprime las primeras filas del DataFrame ordenadas por 'propina_pct' de mayor a menor
df = df[['total_bill', 'tip', 'propina_pct']] # Filtra el DataFrame para que solo contenga las columnas 'total_bill', 'tip' y 'propina_pct'
print(df.head(10)) # Imprime las primeras filas del DataFrame filtrado