products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

discounted = list(filter(lambda x : x["discount"] > 20, products))
print(discounted)