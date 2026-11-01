print("=== Фрагмент А ===")
first_str = "2"
second_str = "3"
print(f"Тип до преобразования: {type(first_str).__name__}, {type(second_str).__name__}")
first = int(first_str)
second = int(second_str)
print(f"Тип после преобразования: {type(first).__name__}, {type(second).__name__}")
print(f"Сумма чисел 2 и 3 = {first + second}")

print()
print("=== Фрагмент Б ===")
age_str = input("Возраст: ")
print(f"Тип до преобразования: {type(age_str).__name__}")
age = int(age_str)
print(f"Тип после преобразования: {type(age).__name__}")
print(f"Возраст через год: {age + 1}")

print()
print("=== Фрагмент В ===")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"Среднее чисел 4, 7, 10 = {average}")

