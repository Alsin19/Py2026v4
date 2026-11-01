subject_1 = input("Название первого предмета: ")
lessons_1 = int(input(f"Количество занятий по '{subject_1}' за неделю (>= 0): "))
duration_1 = int(input(f"Продолжительность одного занятия по '{subject_1}' (мин, > 0): "))

subject_2 = input("Название второго предмета: ")
lessons_2 = int(input(f"Количество занятий по '{subject_2}' за неделю (>= 0): "))
duration_2 = int(input(f"Продолжительность одного занятия по '{subject_2}' (мин, > 0): "))

if lessons_1 < 0 or lessons_2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    raise SystemExit(1)

if duration_1 <= 0 or duration_2 <= 0:
    print("Ошибка: продолжительность занятия должна быть положительной.")
    raise SystemExit(1)

time_1 = lessons_1 * duration_1
time_2 = lessons_2 * duration_2
total_minutes = time_1 + time_2
total_hours = total_minutes / 60

available_hours = float(input(
    f"Доступное время на неделю в часах (не меньше {total_hours:.2f}): "
))

if available_hours < total_hours:
    print(f"Ошибка: доступное время ({available_hours:.2f} ч) "
          f"меньше суммарной нагрузки ({total_hours:.2f} ч).")
    raise SystemExit(1)

free_hours = available_hours - total_hours
four_weeks_minutes = total_minutes * 4
four_weeks_hours = four_weeks_minutes / 60

print()
print("=" * 40)
print("           УЧЕБНАЯ НАГРУЗКА")
print("=" * 40)
print(f"{subject_1}: {time_1} мин")
print(f"{subject_2}: {time_2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_minutes} мин = {four_weeks_hours:.2f} ч")
print("=" * 40)# -*- coding: utf-8 -*-

