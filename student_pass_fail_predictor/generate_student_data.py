import pandas as pd
import numpy as np

np.random.seed(7)
rows = 2876

study_hours = np.random.randint(0, 10, rows)
attendance = np.random.randint(50, 100, rows)
internal_marks = np.random.randint(0, 51, rows)
previous_score = np.random.randint(0, 31, rows)

score = (
    study_hours * 8 +
    attendance * 0.4 +
    internal_marks * 2 +
    previous_score * 3 +
    np.random.normal(0, 8, rows)
)

result = (score > 95).astype(int)

df = pd.DataFrame({
    "StudyHours": study_hours,
    "Attendance": attendance,
    "InternalMarks": internal_marks,
    "PreviousScore": previous_score,
    "Result": result
})

df.to_csv("student_pass_fail.csv", index=False)

print("New balanced student_pass_fail.csv created")
