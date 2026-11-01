raw = input("Введите целые числа через пробел: ")

numbers = []
for token in raw.split():
    numbers.append(int(token))

if not numbers:
    print("Нет данных")
else:

    maximum = numbers[0]
    for value in numbers:
        if value > maximum:
            maximum = value

    # Все индексы максимума через enumerate в порядке возрастания
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)

    print(positions)
