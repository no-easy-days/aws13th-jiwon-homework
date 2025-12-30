def validate_password(password):

    if len(password) < 8:
        return "False: password must contain at least 8 characters"


print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")