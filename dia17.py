import pandas as pd
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

model = LinearRegression()
model.fit(df[['total_bill']], df['tip'])

from sklearn.metrics import mean_absolute_error, r2_score

y_pred = model.predict(df[['total_bill']])
print(r2_score(df['tip'], y_pred))
# El modelo es bueno
# da como resultado 0.45661658635167657