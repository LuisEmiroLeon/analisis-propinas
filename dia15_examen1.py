import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print(df.info()) # Imprime información sobre el DataFrame
print(df.describe()) # Imprime estadísticas descriptivas del DataFrame
print(df.isnull().sum()) # Imprime el número de valores nulos en cada columna
df['propina_pct'] = df['tip'] / df['total_bill'] * 100 # Calcula el porcentaje de propina
print(df.groupby('day')['propina_pct'].mean().sort_values(ascending=False).head(3)) # Imprime los días con mayor promedio de propina
print(df.groupby(['smoker', 'time'])['propina_pct'].mean()) # Imprime el promedio de propina por fumador y hora
print(df[(df['propina_pct'] > 25) & (df['day'] == 'Sat')].groupby(['sex', 'day'])['propina_pct'].mean()) # Imprime el promedio de propina por sexo y día para los registros que cumplen con las condiciones
print(df.groupby(['sex', 'smoker'])['propina_pct'].mean().unstack()) # Imprime el promedio de propina por sexo y fumador

