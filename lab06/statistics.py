raw = input("Введите целые числа через пробел: ")

numbers = []
for token in raw.split():
    numbers.append(int(token))

if not numbers:
    print("Нет данных")
else:
    # Ручной подсчёт: количество, сумма, минимум, максимум
    count = 0
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for value in numbers:
        count += 1
        total += value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    average = total / count  # count >= 1, деления на ноль нет

    print(f"Количество: {count}")
    print(f"Сумма:      {total}")
    print(f"Минимум:    {minimum}")
    print(f"Максимум:   {maximum}")
    print(f"Среднее:    {average:.2f}")
