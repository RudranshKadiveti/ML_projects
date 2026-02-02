import pandas as pd
import numpy as np

np.random.seed(21)
rows = 3000

income = np.random.randint(15000, 120000, rows)
credit_score = np.random.randint(300, 850, rows)
loan_amount = np.random.randint(5000, 500000, rows)
employment_years = np.random.randint(0, 30, rows)

risk = (
    loan_amount * 0.0005 -
    income * 0.0003 -
    credit_score * 0.01 -
    employment_years * 0.3 +
    np.random.normal(0, 1, rows)
)

default = (risk > -1.2).astype(int)

df = pd.DataFrame({
    "Income": income,
    "CreditScore": credit_score,
    "LoanAmount": loan_amount,
    "EmploymentYears": employment_years,
    "Default": default
})

df.to_csv("loan_default.csv", index=False)

print("loan_default.csv created")
