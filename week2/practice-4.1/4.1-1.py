score = int(input("점수를 입력하세요: "))
if 90 <= score <= 100 :
    print("A 등급입니다.")
elif score >= 80:
    print("B 등급입니다.")
elif score >= 70:
    print("C 등급입니다.")
elif score >= 60:
    print("D 등급입니다.")
elif 0 < score < 60:
    print("F 등급입니다.")
else:
    print("잘못된 입력입니다.")