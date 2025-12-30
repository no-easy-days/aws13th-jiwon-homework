import random

answer = random.randint(1, 100)
count = 0

while True:
    count += 1
    num = int(input(("Enter a number: ")))
    if num > answer:
        print(" 더 작은 수를 입력하세요.")
    elif num < answer:
        print(" 더 큰 수를 입력하세요.")
    else:
        print(f"정답입니다! {count}번 만에 맞추셨습니다!")
        break