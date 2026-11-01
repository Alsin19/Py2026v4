n = int(input("Количество чисел (n >= 1): "))

if n < 1:
    print("Ошибка: n должно быть >= 1.")
    raise SystemExit(1)

first_value = int(input("Число 1: "))
total = first_value
positive_count = 1 if first_value > 0 else 0
maximum = first_value

for i in range(2, n + 1):
    value = int(input(f"Число {i}: "))
    total += value
    if value > 0:
        positive_count += 1
    if value > maximum:
        maximum = value

print()
print(f"Сумма: {total}")
print(f"Положительных значений: {positive_count}")
print(f"Максимум: {maximum}")

