num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Choose Operator( + , - , * , / , // , % ) ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 ==  0:
        print("can't divide by zero")
    else:
        result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
else:
    print("Choose Correct Operator( + , - , * , / , // , % )")

print(f"결과는 {result}입니다.")