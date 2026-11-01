total_seconds = int(input("Общее количество секунд (целое >= 0): "))

if total_seconds < 0:
    print("Ошибка: количество секунд не может быть отрицательным.")
    raise SystemExit(1)

hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

print(f"{total_seconds} с = {hours} ч {minutes} мин {seconds} с")# -*- coding: utf-8 -*-

