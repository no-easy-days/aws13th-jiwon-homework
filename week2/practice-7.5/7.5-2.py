import os
from datetime import datetime

DIARY_DIR = "diaries"  # 일기 저장 폴더

# 일기 폴더 없으면 생성
if not os.path.exists(DIARY_DIR):
    os.makedirs(DIARY_DIR)


def write_today_diary():
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{today}.txt"
    path = os.path.join(DIARY_DIR, filename)

    print("오늘의 일기를 입력하세요 (끝내려면 엔터 두 번):")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"{filename} 저장 완료")


def read_diary_by_date():
    date = input("읽고 싶은 날짜를 입력하세요 (YYYY-MM-DD): ")
    filename = f"diary_{date}.txt"
    path = os.path.join(DIARY_DIR, filename)

    if not os.path.exists(path):
        print("해당 날짜의 일기가 없습니다.")
        return

    print(f"\n{filename} 내용:")
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


def list_all_diaries():
    files = os.listdir(DIARY_DIR)
    diaries = [f for f in files if f.startswith("diary_")]

    if not diaries:
        print("저장된 일기가 없습니다.")
        return

    print("저장된 일기 목록:")
    for diary in sorted(diaries):
        print("-", diary)


def main():
    while True:
        print("일기장 프로그램")
        print("1. 오늘 일기 쓰기")
        print("2. 특정 날짜 일기 읽기")
        print("3. 모든 일기 목록 보기")
        print("4. 종료")

        choice = input("선택: ")

        if choice == "1":
            write_today_diary()
        elif choice == "2":
            read_diary_by_date()
        elif choice == "3":
            list_all_diaries()
        elif choice == "4":
            print("프로그램 종료 👋")
            break
        else:
            print("올바른 번호를 입력하세요.")


main()
