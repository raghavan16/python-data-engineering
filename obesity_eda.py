import pandas as pd

df = pd.read_csv("obesity_prediction.csv")

print("Shape:", df.shape) 
print("Columns:", list(df.columns))
print("Nulls per column:\n", df.isna().sum())

print(df["Obesity"].value_counts())
print(df.groupby("Obesity")["Weight"].mean())

df["BMI"] = df["Weight"] / (df["Height"] ** 2)
print(df.groupby("Obesity")["BMI"].mean())

print(df.groupby("Gender")["Obesity"].value_counts())
