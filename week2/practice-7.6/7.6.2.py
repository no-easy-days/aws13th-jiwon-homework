import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row['나이']) 
        if age >= 30:
            print(f"{row['이름']} ({age}세)")