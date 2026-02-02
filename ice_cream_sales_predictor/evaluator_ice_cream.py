import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("ice_cream_sales.csv")

X = df[["Temperature", "Season"]]
y = df["Sales"]

model = joblib.load("model.pkl")
pred = model.predict(X)

mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2 Score:", r2)

plt.figure()
plt.scatter(y, pred, alpha=0.3)
min_val = min(y.min(), pred.min())
max_val = max(y.max(), pred.max())
plt.plot([min_val, max_val], [min_val, max_val])
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()
