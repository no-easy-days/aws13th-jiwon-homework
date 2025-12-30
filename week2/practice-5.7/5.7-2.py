def print_report(name, scores):
    max_scores = max(scores)
    min_scores = min(scores)
    avg_scores = sum(scores) / len(scores)
    if avg_scores > 90:
        grade = "A"
    elif avg_scores > 80:
        grade = "B"
    elif avg_scores > 70:
        grade = "C"
    elif avg_scores > 60:
        grade = "D"
    else:
        grade = "F"

    print(f"=== {name} 성적표 ===")
    print(f"점수: {scores}")
    print(f"평균: {avg_scores}")
    print(f"최고점: {max_scores}")
    print(f"최저점: {min_scores}")
    print(f"등급: {grade}")


print_report("김철수", [85, 92, 78, 96, 88])