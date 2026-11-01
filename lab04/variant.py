n = int(input("Количество чисел (n >= 0): "))

# Проверка ограничения
if n < 0:
    print("Ошибка: n не может быть отрицательным.")
    raise SystemExit(1)

count_odd = 0
sum_odd = 0

for i in range(1, n + 1):
    value = int(input(f"Число {i}: "))
    if value % 2 != 0:
        count_odd += 1
        sum_odd += value

print()
print(f"Количество нечётных: {count_odd}")
print(f"Сумма нечётных: {sum_odd}")
