a = float(input("Первое число: "))
b = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+":
    result = a + b
    print(f"{result:.2f}")
elif operation == "-":
    result = a - b
    print(f"{result:.2f}")
elif operation == "*":
    result = a * b
    print(f"{result:.2f}")
elif operation == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")

