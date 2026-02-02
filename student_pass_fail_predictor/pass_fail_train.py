import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("student_pass_fail.csv")

X = df[["StudyHours", "Attendance", "InternalMarks", "PreviousScore"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

joblib.dump(model, "pass_fail_model.pkl")

print("Model trained and saved as pass_fail_model.pkl")
