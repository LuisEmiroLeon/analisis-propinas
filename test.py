
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
df['sex_code'] = (df['sex'] == 'Male').astype(int)
df['smoker_code'] = (df['smoker'] == 'Yes').astype(int)

X = df[['total_bill','size','sex_code','smoker_code']]
y = df['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print(f"R² train: {r2_score(y_train, model.predict(X_train)):.4f}")
print(f"R² test (real): {r2_score(y_test, model.predict(X_test)):.4f}")

