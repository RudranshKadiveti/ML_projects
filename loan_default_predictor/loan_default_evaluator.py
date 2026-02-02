import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

df = pd.read_csv("loan_default.csv")

X = df[["Income", "CreditScore", "LoanAmount", "EmploymentYears"]]
y = df["Default"]

model = joblib.load("loan_default_model.pkl")
pred = model.predict(X)

acc = accuracy_score(y, pred)
cm = confusion_matrix(y, pred)

print("Accuracy:", acc)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y, pred))

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix - Loan Default")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0, 1], ["No Default", "Default"])
plt.yticks([0, 1], ["No Default", "Default"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()
