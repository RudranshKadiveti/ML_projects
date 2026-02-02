import joblib

model = joblib.load("model.pkl")

temp = float(input("Enter temperature: "))
season = int(input("Enter season (0=Winter,1=Spring,2=Summer,3=Autumn): "))

pred = model.predict([[temp, season]])
print("Predicted Sales:", int(pred[0]))
