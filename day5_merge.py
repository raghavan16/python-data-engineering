import pandas as pd

claims_df = pd.read_csv("claims.csv")
members_df = pd.read_csv("members.csv")
print("===claims-data===") 
print(claims_df)
print("===members-data===")  
print(members_df)

merged_df = pd.merge(claims_df,members_df,left_on="member", right_on="member_id",how="inner")
print("\n=== MERGED DATA ===")
print(merged_df)

paid_df = merged_df[merged_df["status"]=="PAID"]
print("\n=== PAID CLAIMS ===")
print(paid_df)

plan_spend = paid_df.groupby("plan")["amount"].sum()
print("\n=== TOTAL SPEND BY PLAN ===")
print(plan_spend)
plan_spend.to_csv("plan_spend_report.csv")

high_value_df = paid_df[paid_df["amount"] > 500]
print("\n=== HIGH VALUE CLAIMS ===")
print(high_value_df[["claim_id", "member_name", "plan", "amount"]])
