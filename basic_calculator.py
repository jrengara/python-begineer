# num1 = input("Enter input 1 : ")
# num2 = input("Enter input 2 : ")
# result = float(num1) + float(num2)
# print("result -- " + str(result))


num1 = float(input("Enter first number1 : "))
num2 = float(input("Enter second number2 : "))
operator = input("Enter the operator (+,-,*,/,%): ")

result = 0.0

if operator == "+":
    print(num1 + num2)
    result = num1 + num2
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
    result = num1 * num2
elif operator == "/":
    print(num1 / num2)
elif operator == '%':
    print(num1 % num2)
else:
    print(operator + " is not a valid operator")
print(result)
