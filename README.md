# Análisis de Propinas en Restaurantes - Dataset Tips

Proyecto de análisis exploratorio, machine learning y deploy con Python, Pandas, Scikit-Learn y Streamlit.
**Deploy en vivo:** https://predecir-propinas-luis.streamlit.app/

## 📊 Dataset
- 244 registros de propinas de restaurante en USA
- Fuente: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
- Columnas: total_bill, tip, sex, smoker, day, time, size

## 🔧 Progreso del Curso (Día 9 al 24)

**Día 9 - Lectura:**
- `pd.read_csv(url)` para leer desde URL real
- `info()`, `describe()`, `head(10)`, `mean()`

**Día 10 - Limpieza:**
- `isnull().sum()` -> 0 nulos
- `duplicated()` -> 0 duplicados
- Filtro `df[df['total_bill'] > 30]`

**Día 11 - Feature Engineering:**
- Nueva columna: `propina_pct = tip / total_bill * 100`
- `sort_values('propina_pct', ascending=False)`
- Selección de columnas clave

**Día 12 - Visualización:**
- barplot: gasto promedio por día
- scatterplot: total_bill vs tip
- histplot: distribución de % propina

**Día 13 - Insights con groupby:**
- Mujeres dejan ~16.6% vs Hombres ~15.9%
- No fumadores ~16.3% vs Fumadores ~15.3%
- Dinner vs Lunch

**Día 14-20 - Modelado Base:**
- Train/Test split
- LinearRegression baseline

**Día 21-23 - Búsqueda del Mejor Modelo:**
- Probamos 4 columnas: `total_bill, size, sex_code, smoker_code` -> R² 0.4365
- Probamos 6 columnas con `pd.get_dummies(..., drop_first=True)`
- Columnas disponibles en esta versión de pandas: `sex_Female, smoker_No, day_Fri, day_Sat, day_Sun, time_Dinner`

**Día 24 - Ganador y Deploy en Streamlit Cloud:**
- **Mejor combo encontrado:** `['total_bill', 'size', 'day_Fri', 'day_Sat', 'day_Sun', 'time_Dinner']`
- **R²: 0.4675** (supera al objetivo de 0.4485)
- Modelo guardado con `joblib.dump()` para evitar error `STACK_GLOBAL / _pickle.UnpicklingError`
- `app.py` actualizado con mapeo exacto de columnas
- Fix de git: `git push --set-upstream origin main --force` para resincronizar OneDrive + GitHub
- **Deploy final:** https://predecir-propinas-luis.streamlit.app/
  - Test: $20, 2 pers, Fri, Dinner = $2.97
  - Test: $20, 2 pers, Thur, Lunch = $2.95

## 💡 Insight Principal
Las mujeres y los no fumadores dejan un mayor porcentaje de propina, aunque la diferencia no es abismal. El % de propina más común está entre 15% y 18%. El modelo final demuestra que `total_bill` y `size` explican la mayor parte de la propina, con ajustes pequeños por día y momento (Dinner/Fri/Sat).

## 🚀 Día 25 - Siguiente Actividad (Propuesta)

**Objetivo:** Exponer el modelo R² 0.4675 como API REST con FastAPI.

**Tareas:**
1. Crear `api.py` con FastAPI que cargue `modelo_propinas.pkl`
2. Endpoint `POST /predict` que reciba JSON: `{"total_bill":20, "size":2, "day":"Fri", "time":"Dinner"}`
3. Retorne `{"propina_estimada": 2.97, "r2": 0.4675}`
4. Probar local con `uvicorn api:app --reload` y docs en `/docs`
5. Actualizar README con ejemplo de `curl`

**Bonus:** Dockerizar la API.

## 🛠️ Tecnologías
Python 3.14, Pandas 2.x, Numpy, Matplotlib, Seaborn, Scikit-Learn, joblib, Streamlit, FastAPI (Día 25)

## ▶️ Cómo correrlo

```bash
# Instalar
pip install pandas seaborn matplotlib scikit-learn joblib streamlit fastapi uvicorn

# Correr análisis
python dia13.py

# Buscar mejor modelo (R2 0.4675)
python buscar_mejor.py

# Correr app Streamlit local
streamlit run app.py

# Día 25 - API (próximo)
uvicorn api:app --reload
```
