import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Student ID": [101,102,103,104,104,106,107,108,109,110],
    "Name": [
        " Alice ",
        "Bob",
        "Charlie",
        "David",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        np.nan
    ],
    "Age": [
        20,
        np.nan,
        22,
        -1,
        -1,
        21,
        23,
        20,
        np.nan,
        24
    ],
    "Gender": [
        " Male ",
        "female",
        "Female",
        "MALE",
        "MALE",
        "female",
        "Male",
        "Female",
        "male",
        " Female "
    ],
    "Department": [
        "Computer Science",
        "computer science",
        "IT",
        "Information Technology",
        "Information Technology",
        np.nan,
        "IT",
        "Computer Science",
        "IT",
        "Computer Science"
    ],
    "Marks": [
        85,
        90,
        np.nan,
        70,
        70,
        88,
        95,
        102,
        76,
        81
    ],
    "Enrollment Date": [
        "2024-01-10",
        "2024-01-12",
        "2024-02-01",
        "2024-01-20",
        "2024-01-20",
        "2024-03-05",
        "2024-03-12",
        "2024-02-15",
        "2024-02-20",
        "2024-03-01"
    ]
})

print(df)