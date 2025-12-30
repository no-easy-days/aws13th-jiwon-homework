str_numbers = ["10", "20", "30", "40", "50"]

int_numbers = list(map(lambda x: int(x) + 100, str_numbers))

result = int_numbers

print(result)