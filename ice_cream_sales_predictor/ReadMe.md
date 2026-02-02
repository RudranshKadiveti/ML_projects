![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-red)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Sales%20Prediction-yellow)
![Model](https://img.shields.io/badge/Model-Linear%20Regression-blueviolet)
![Status](https://img.shields.io/badge/Project-Beginner%20Friendly-success)


# Ice Cream Sales Predictor

This is a small machine learning project built while learning the fundamentals of machine learning.

The goal of this project is to **predict ice cream sales based on temperature and season**.

The project is designed to be simple, easy to understand, and still realistic.
A synthetic dataset was created using real-world patterns, and a regression model was trained on it.

---

## Project Structure

| File                           | Description                                       |
| ------------------------------ | ------------------------------------------------- |
| `ice_cream_sales.csv`          | Dataset containing Temperature, Season, and Sales |
| `ice_cream_trainer.py`         | Trains the model and saves it                     |
| `evaluator_ice_cream.py`       | Evaluates the model and displays a graph          |
| `sales_predictor.py`           | Accepts user input and predicts sales             |
| `ice_cream_sales_predictor.md` | Project documentation (this file)                 |

---

## Dataset Overview

The dataset contains **2,875 rows** with the following columns:

* **Temperature** – Temperature in degrees Celsius (°C)
* **Season** – Encoded as:

  * `0` → Winter
  * `1` → Spring
  * `2` → Summer
  * `3` → Autumn
* **Sales** – Number of ice creams sold

### Data Logic

The dataset is synthetic, but follows realistic trends:

* As **temperature increases**, sales generally increase
* **Summer** has the highest sales
* **Winter** has the lowest sales

---

## Model Used

A **Linear Regression** model from `scikit-learn` is used.

The model learns a simple relationship between the inputs and the output:

```
Sales ≈ Temperature + Season
```

---

## Example Prediction

**Input**

```
Temperature: 30
Season: 2
```

**Output**

```
Predicted Sales: 228
```

---

## What I Learned

This project helped me understand:

* How to load and process datasets
* How to train a machine learning model
* How to evaluate model performance using **MSE** and **R²**
* How to visualize predictions
* How to save and reuse trained models

---

This project represents my first step into applied machine learning.

