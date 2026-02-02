# Student Pass / Fail Predictor

This is a machine learning mini project that predicts whether a student will
PASS or FAIL based on their academic performance and attendance.

I built this project to understand how classification models work and how
student data can be used to make predictions in a realistic way.

---

## Files in this Project

| File | What it does |
|------|--------------|
| student_pass_fail.csv | Dataset used for training |
| pass_fail_train.py | Trains the model and saves it |
| pass_fail_evaluator.py | Evaluates the model and shows confusion matrix |
| pass_fail_predict.py | Takes user input and predicts result |
| STUDENT_PASS_FAIL_PREDICTOR.md | This file |

---

## About the Dataset

The dataset contains 2,876 student records with the following columns:

- StudyHours – hours studied per day  
- Attendance – attendance percentage  
- InternalMarks – marks out of 50  
- PreviousScore – marks out of 30  
- Result – target value  
  - 0 = Fail  
  - 1 = Pass  

The data was generated to follow realistic academic patterns:
- More study hours lead to a higher chance of passing  
- Higher attendance improves performance  
- Good internal marks increase final success  
- Strong previous exam scores increase the chance of passing  

---

## Model Used

I used Logistic Regression from scikit-learn, which is commonly used for
binary classification problems like pass/fail.

---

## Example

Input:  
Study Hours: 6  
Attendance: 85  
Internal Marks: 40  
Previous Score: 22  

Output:  
Prediction: PASS  

---

## What I Learned

This project helped me learn:
- How to build a classification model  
- How to evaluate using confusion matrix and accuracy  
- How to interpret precision, recall, and F1-score  
- How to save and load models for reuse  

---
