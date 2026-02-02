import joblib

model = joblib.load("loan_default_model.pkl")

income = float(input("Enter annual income: "))
credit = float(input("Enter credit score: "))
loan = float(input("Enter loan amount: "))
years = float(input("Enter employment years: "))

proba = model.predict_proba([[income, credit, loan, years]])[0][1]

if proba > 0.45:
    print("Prediction: DEFAULT RISK")
else:
    print("Prediction: SAFE LOAN")


