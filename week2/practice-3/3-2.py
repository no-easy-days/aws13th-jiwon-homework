email = input("Enter your email address:")
pwd = input("Enter your password:")

parts = email.split("@")

if len(pwd) < 8:
    print("Password is too short")
else:
    print(parts[0])
    print(parts[1])
    print("✅Password is valid")
