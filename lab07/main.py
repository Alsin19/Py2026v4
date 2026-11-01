from functions import sum_digits, average, normalize_text, select_numbers

number = int(input("Введите целое число: "))
digits_sum = sum_digits(number)
print(f"Сумма цифр числа {number}: {digits_sum}")

raw_numbers = input("Введите числа через пробел (можно пусто): ")
numbers = []
for token in raw_numbers.split():
    numbers.append(int(token))

avg = average(numbers)
if avg is None:
    print("Среднее: Нет данных")
else:
    print(f"Среднее: {avg:.2f}")

text = input("Введите произвольный текст: ")
print(f"Нормализованный текст: '{normalize_text(text)}'")

threshold = int(input("Введите порог (целое неотрицательное): "))
selected = select_numbers(numbers, threshold)
print(f"Числа не меньше {threshold}: {selected}")
