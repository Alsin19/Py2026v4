score = int(input("Результат теста (целое от 0 до 100): "))

if score < 0 or score > 100:
    print("Ошибка диапазона")
elif score <= 49:
    print("Нужна доработка")
elif score <= 84:
    print("Зачёт")
else:
    print("Отличный результат")

