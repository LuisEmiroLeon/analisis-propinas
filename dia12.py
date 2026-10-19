# Visualización Pro - inicio de tu proyecto de portafolio.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
sns.barplot(data=df, x='day', y='total_bill') # grafica de barras de la propina promedio por día
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip") # grafica de dispersión de la propina en función del total de la cuenta
plt.show()

sns.histplot(df['propina_pct'] if 'propina_pct' in df else df['tip']) # histograma de la distribución de la propina en porcentaje o en valor absoluto si no existe la columna 'propina_pct'
plt.show()
