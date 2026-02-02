Bank Loan Default Predictor



This is a machine learning mini project that predicts whether a customer is

likely to default on a loan based on their financial and employment details.



I built this project to understand how banks and financial institutions assess

credit risk using data.







Files in this Project





loan\_default.csv - Dataset used for training 

loan\_default\_train.py - Trains the model and saves it 

loan\_default\_evaluator.py - Evaluates the model and shows confusion matrix 

loan\_default\_predict.py - Takes user input and predicts result 

bank\_loan\_default\_predictor.md - This file 







About the Dataset



The dataset contains 3,000 customer records with the following columns:



\- Income – annual income  

\- CreditScore – credit score (300–850)  

\- LoanAmount – loan amount requested  

\- EmploymentYears – years of work experience  

\- Default – target value  

&nbsp; - 0 = No Default  

&nbsp; - 1 = Default  



The data was generated to follow realistic financial risk patterns:

\- Higher loan amounts increase risk  

\- Lower income increases risk  

\- Lower credit scores increase risk  

\- Fewer employment years increase risk  







Model Used



I used Logistic Regression from scikit-learn, which is commonly used for

binary classification problems in finance.







 **Example**



Input:  

Income: 60000  

Credit Score: 700  

Loan Amount: 100000  

Employment Years: 5  



**Output**:  

Prediction: Default risk 





**What I Learned**



This project helped me learn:

\- How to build a classification model  

\- How to evaluate using confusion matrix  

\- How to interpret credit risk predictions  

\- How to save and load models for reuse  







