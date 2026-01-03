import csv
import json

#csv
with open('users.csv', 'r', encoding='utf-8') as f:
    users = list(csv.DictReader(f))

#json
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)