import joblib

model = joblib.load("pass_fail_model.pkl")

study = float(input("Enter study hours per day: "))
att = float(input("Enter attendance percentage: "))
internal = float(input("Enter internal marks: "))
prev = float(input("Enter previous exam score: "))

pred = model.predict([[study, att, internal, prev]])

if pred[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
