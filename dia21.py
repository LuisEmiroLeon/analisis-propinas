## RandomForest vs LinearRegression

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
df['sex_code'] = (df['sex'] == 'Male').astype(int)
df['smoker_code'] = (df['smoker'] == 'Yes').astype(int)

X = df[['total_bill', 'size', 'sex_code', 'smoker_code']]
y = df['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
print(f"R² RF test: {r2_score(y_test, rf.predict(X_test)):.4f} - ¿supera tu 0.4485?") # RF = 0.2029

"""
R² RF test: 0.2029 vs LinearRegression: 0.4485

RandomForest perdió. Y eso es NORMAL.

¿Por qué?

Dataset pequeño: 244 filas. RandomForest necesita miles de datos para aprender sus árboles. Con 244, memoriza ruido (overfitting).
Relación lineal: total_bill -> tip es casi lineal (10% de la cuenta). LinearRegression es perfecto para eso. RF busca curvas complejas donde no las hay.
Pocas features: 4 columnas. RF brilla con 20-100 features.
Esto es lo que te preguntan en entrevistas Jr:

"¿Cuándo usar LinearRegression vs RandomForest?"

Tu respuesta ahora: "Probé ambos en tips dataset (244 filas, relación lineal) 
- LinearRegression R² 0.44 superó a RF 0.20, porque con pocos datos y relación lineal, el modelo simple generaliza mejor.
"""