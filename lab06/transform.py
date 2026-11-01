raw = input("Введите целые числа через пробел: ")

original = []
for token in raw.split():
    original.append(int(token))

transformed = []
for value in original:
    if value < 0:
        transformed.append(-value)
    else:
        transformed.append(value)

print(f"Исходный список: {original}")
print(f"Новый список:    {transformed}")
