import pandas as pd

df = pd.read_csv("claims.csv")

print("=== FULL DATA ===")
print(df)

print("\n=== DATA INFO ===")
print(df.info())

print("\n=== PAID CLAIMS ===")
paid_df = df[df["status"] == "PAID"]
print(paid_df)

print("\n=== HIGH VALUE PAID CLAIMS ===")
high_paid_df = df[(df["status"] == "PAID") & (df["amount"] > 500)]
print(high_paid_df)

print("\n=== TOTAL AMOUNT ===")
print(df["amount"].sum())

print("\n=== PAID CLAIMS COUNT ===")
print((df["status"] == "PAID").sum())

print("\n=== TOTAL AMOUNT BY MEMBER ===")
print(df.groupby("member")["amount"].sum())
