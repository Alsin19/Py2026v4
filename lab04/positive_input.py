attempts_rejected = 0

while True:
    value = int(input("Введите целое число: "))
    if value > 0:
        break
    attempts_rejected += 1

print(f"Квадрат числа: {value * value}")
print(f"Отклонённых попыток: {attempts_rejected}")
