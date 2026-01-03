import json

#읽기
with open('logs.json', 'r', encoding='utf-8') as f:
    logs = json.load(f)

#ERROR 필터링
errors = []

for log in logs:
    if log['level'] == 'ERROR':
        errors.append(log)

#저장
with open('errors.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

print(f"에러를 errors.json에 저장했습니다.")