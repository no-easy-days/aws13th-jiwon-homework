scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
best = sorted(scores.items(), key=lambda items: items[1], reverse=True)
print(f"최고 학생은 {best[0]} 입니다.")

