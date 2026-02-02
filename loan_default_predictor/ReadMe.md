![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Classification-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Loan%20Default-yellow)
![Model](https://img.shields.io/badge/Model-Logistic%20Regression-purple)
![Status](https://img.shields.io/badge/Project-Beginner%20Friendly-success)

# Bank Loan Default Predictor

This is a machine learning mini project that predicts whether a customer is
likely to default on a loan based on their financial and employment details.

I built this project to understand how banks and financial institutions assess
credit risk using data.

---

## Files in this Project

| File | What it does |
|------|--------------|
| loan_default.csv | Dataset used for training |
| loan_default_train.py | Trains the model and saves it |
| loan_default_evaluator.py | Evaluates the model and shows confusion matrix |
| loan_default_predict.py | Takes user input and predicts result |
| BANK_LOAN_DEFAULT_PREDICTOR.md | This file |

---

## About the Dataset

The dataset contains 3,000 customer records with the following columns:

- Income – annual income  
- CreditScore – credit score (300–850)  
- LoanAmount – loan amount requested  
- EmploymentYears – years of work experience  
- Default – target value  
  - 0 = No Default  
  - 1 = Default  

The data was generated to follow realistic financial risk patterns:
- Higher loan amounts increase risk  
- Lower income increases risk  
- Lower credit scores increase risk  
- Fewer employment years increase risk  

---

## Model Used

I used Logistic Regression from scikit-learn, which is commonly used for
binary classification problems in finance.

---

## Example

Input:  
Income: 60000  
Credit Score: 700  
Loan Amount: 100000  
Employment Years: 5  

Output:  
Prediction: Default Risk  

---

## What I Learned

This project helped me learn:
- How to build a classification model  
- How to evaluate using confusion matrix  
- How to interpret credit risk predictions  
- How to save and load models for reuse  

---

