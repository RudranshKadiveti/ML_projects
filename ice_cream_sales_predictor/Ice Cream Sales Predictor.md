**Ice Cream Sales Predictor**



This is a small machine learning project I built while learning the basics of ML.  

GOAL: predict ice cream sales based on the temperature and the season.



I wanted to make something easy to understand, but still realistic and useful.  

So I created a dataset with real-world patterns and trained a model on it.





 **Files in this Project**





**ice\_cream\_sales.csv**  -  The dataset (Temperature, Season, Sales) 

**ice \_cream\_trainer.py** - Trains the model and saves it 

**evaluator\_ice\_cream.py** - Tests the model and shows a graph 

**sales\_predictor.py** - Lets you enter new values and get predictions 

**ice\_cream\_sales\_predictor.md**  - This file 







 **About the Dataset**



The dataset has 2,875 rows and three columns:



\- Temperature – temperature in °C  

\- Season 

&nbsp; - 0 = Winter  

&nbsp; - 1 = Spring  

&nbsp; - 2 = Summer  

&nbsp; - 3 = Autumn  

\- Sales – number of ice creams sold  



The data is synthetic, but it follows realistic logic:

\- When the temperature goes up, sales usually increase  

\- Summer has the highest sales  

\- Winter has the lowest  







 **Model Used**



I used a Linear Regression model from scikit-learn.



The model learns a simple relationship like:



Sales ≈ Temperature + Season





**Example**



Input:  

Temperature: 30  

Season: 2  



**Output**:  

Predicted Sales: 228  





**What I Learned**



This project helped me learn:

\- How to load and work with data  

\- How to train a machine learning model  

\- How to check model accuracy using MSE and R²  

\- How to visualize predictions  

\- How to save and reuse trained models  











