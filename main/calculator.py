method = (input("Enter a method (+ - * /) "))
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))

if method == "+":
    print(num1 + num2)
elif method == "-":
    print(num1 - num2)
elif method == "*":
    print(num1 * num2)
elif method == "/":
    print(num1 / num2)
else:
    print("Invalid method")