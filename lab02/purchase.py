price = int(input("Цена одной тетради (целые рубли, >= 0): "))
count = int(input("Количество тетрадей (>= 0): "))
paid = int(input("Переданная сумма (руб): "))

if price < 0:
    print("Ошибка: цена не может быть отрицательной.")
    raise SystemExit(1)
if count < 0:
    print("Ошибка: количество не может быть отрицательным.")
    raise SystemExit(1)
if paid < price * count:
    print("Ошибка: переданной суммы недостаточно.")
    raise SystemExit(1)

total_cost = price * count
change = paid - total_cost

print(f"Стоимость: {total_cost} руб.")
print(f"Сдача: {change} руб.")

