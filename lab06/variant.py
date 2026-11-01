raw = input("Введите целые числа через пробел: ")

numbers = []
for token in raw.split():
    numbers.append(int(token))

selected = []
for value in numbers:
    if value % 2 != 0:
        selected.append(value)

sorted_copy = sorted(selected)

count = len(selected)
total = sum(selected)

print(f"Исходный порядок: {selected}")
print(f"Количество:       {count}")
print(f"Сумма:            {total}")
print(f"Сортированная копия: {sorted_copy}")
