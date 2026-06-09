a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operation: ")

result = None

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        print("Division by zero is not allowed")

if result is not None:
    print("Answer =", result)
