import joblib, pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
df['sex_code'] = (df['sex'] == 'Male').astype(int)
df['smoker_code'] = (df['smoker'] == 'Yes').astype(int)

X = df[['total_bill','size','sex_code','smoker_code']]
y = df['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, 'modelo_propinas.pkl')
print("modelo_propinas.pkl guardado") # modelo guardado