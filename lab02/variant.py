total = int(input("Общий объём (количество деталей, целое >= 0): "))
capacity = int(input("Вместимость одного контейнера (целое > 0): "))

if total < 0:
    print("Ошибка: общий объём не может быть отрицательным.")
    raise SystemExit(1)
if capacity <= 0:
    print("Ошибка: вместимость должна быть положительной.")
    raise SystemExit(1)

full_units = total // capacity                 # полностью заполненные контейнеры
remainder = total % capacity                   # остаток
units_needed = (total + capacity - 1) // capacity  # минимум

print(f"Полностью заполненных контейнеров: {full_units}")
print(f"Остаток деталей: {remainder}")
print(f"Минимальное число контейнеров: {units_needed}")

