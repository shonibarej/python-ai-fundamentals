import csv

# data = [
#     {"name": "Alice", "role": "Data Analyst", "salary": 45000},
#     {"name": "Bob", "role": "AI Engineer", "salary": 75000},
#     {"name": "Carol", "role": "Data Analyst", "salary": 50000},
# ]

# with open("employees.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "role", "salary"])
#     writer.writeheader()
#     writer.writerows(data)


# with open("employees.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    analysts = [row for row in reader if row["role"] == "Data Analyst"]
    print(analysts)