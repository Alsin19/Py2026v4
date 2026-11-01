last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет, 1-120): "))
favorite_subject = input("Любимый предмет: ")
hours_per_week = float(input("Количество часов подготовки в неделю (>= 0): "))

if not (1 <= age <= 120):
    print("Ошибка: возраст должен быть целым числом от 1 до 120.")
    raise SystemExit(1)

if hours_per_week < 0:
    print("Ошибка: количество часов не может быть отрицательным.")
    raise SystemExit(1)

full_name = f"{first_name} {last_name}"
age_in_four_years = age + 4
hours_in_four_weeks = hours_per_week * 4
average_hours_per_day = hours_per_week / 7

print()
print("=" * 40)
print("           КАРТОЧКА ПРОФИЛЯ")
print("=" * 40)
print(f"Фамилия:            {last_name}")
print(f"Имя:                {first_name}")
print(f"Полное имя:         {full_name}")
print(f"Группа:             {group}")
print(f"Город:              {city}")
print(f"Возраст:            {age}")
print(f"Возраст через 4 г.: {age_in_four_years}")
print(f"Любимый предмет:    {favorite_subject}")
print(f"Часов в неделю:     {hours_per_week:.2f}")
print(f"За 4 недели:        {hours_in_four_weeks:.2f}")
print(f"В среднем в день:   {average_hours_per_day:.2f}")
print("=" * 40)

