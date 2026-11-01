album_price = float(input("Цена одного альбома (руб): "))
album_quantity = int(input("Количество альбомов: "))

brush_set_price = float(input("Цена одного набора кистей (руб): "))
brush_set_quantity = int(input("Количество наборов кистей: "))

delivery_cost = float(input("Стоимость доставки (руб): "))
paid_amount = float(input("Сумма, внесённая покупателем (руб): "))

albums_total = album_price * album_quantity
brush_sets_total = brush_set_price * brush_set_quantity
goods_total = albums_total + brush_sets_total
order_total = goods_total + delivery_cost
total_units = album_quantity + brush_set_quantity
change = paid_amount - order_total

print()
print("=" * 45)
print("        ЗАКАЗ: ХУДОЖЕСТВЕННАЯ МАСТЕРСКАЯ")
print("=" * 45)
print(f"Альбомы:            {album_quantity} шт. × {album_price:.2f} = {albums_total:.2f} руб.")
print(f"Наборы кистей:      {brush_set_quantity} шт. × {brush_set_price:.2f} = {brush_sets_total:.2f} руб.")
print("-" * 45)
print(f"Товары без доставки: {goods_total:.2f} руб.")
print(f"Доставка:            {delivery_cost:.2f} руб.")
print(f"Итого к оплате:      {order_total:.2f} руб.")
print(f"Всего единиц товара: {total_units} шт.")
print(f"Сдача:               {change:.2f} руб.")
print("=" * 45)# -*- coding: utf-8 -*-

