import csv

total_amount = 0
paid_count = 0

with open("claims.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = int(row["amount"])
        status = row["status"]

        # 1. Total amount
        total_amount += amount

        # 2. Count PAID claims
        if status == "PAID":
            paid_count += 1

        # 3. High value claims
        if amount > 500:
            print("High Value:", row["claim_id"], row["member"], amount)

print("Total Amount:", total_amount)
print("Paid Claims Count:", paid_count)
