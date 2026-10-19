\# Análisis de Propinas en Restaurantes - Dataset Tips



Proyecto de análisis exploratorio con Python, Pandas y Seaborn.



\## 📊 Dataset

\- 244 registros de propinas de restaurante en USA

\- Fuente: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

\- Columnas: total\_bill, tip, sex, smoker, day, time, size



\## 🔧 ¿Qué hice? (Fase 1-3)



\*\*Día 9 - Lectura:\*\*

\- 'pd.read\_csv(url)' para leer la información desde URL real

\- Utilicé 'info()' para conocer la información del dataframe, 'describe()' para las estadísticas descriptivas, 'head(10)' para conocer la información de las primeras 10 filas y 'mean()' para conocer el promedio



\*\*Día 10 - Limpieza:\*\*

\- 'isnull().sum()' para conocer valores nan o nulos -> 0 nulos

\- 'duplicated()' para conocer cuántos duplicados -> 0 duplicados

\- Filtro 'df\[df\['total\_bill'] > 30]' para conocer las filas donde 'total\_bill' es mayor a 30



\*\*Día 11 - Feature Engineering:\*\*

\- Nueva columna: 'propina\_pct = tip / total\_bill \* 100' para agregar el porcentaje

\- 'sort\_values('propina\_pct', ascending=False)' para ordenar de mayor a menor las filas por la columna de propina\_pct 

\- Selección de columnas clave



\*\*Día 12 - Visualización:\*\*

\- barplot: gráfico de barras para mostrar el gasto promedio por día

\- scatterplot: gráfico de dispersión para ver la relación total\_bill vs tip

\- histplot: histograma para mostrar la distribución de % propina



\*\*Día 13 - Insights con groupby:\*\*

\- Mujeres dejan \~16.6% vs Hombres \~15.9%

\- No fumadores \~16.3% vs Fumadores \~15.3%

\- Dinner vs Lunch



\## 💡 Insight Principal

Las mujeres y los no fumadores dejan un mayor porcentaje de propina, aunque la diferencia no es abismal. El % de propina más común está entre 15% y 18%.



\## 🛠️ Tecnologías

Python 3.13, Pandas 3.0.5, Numpy, Matplotlib, Seaborn



\## ▶️ Cómo correrlo

""" bash

pip install pandas seaborn matplotlib

python dia13.py

