text = input("Введите строку: ")

words = text.split()  # разбиение по пробельным символам
count_matched = 0

for word in words:
    cleaned_word = word.strip(".,!?;:").lower()
    if cleaned_word == "":
        continue  # пустые результаты пропускаем
    if cleaned_word.startswith("к"):
        print(cleaned_word)
        count_matched += 1

if count_matched == 0:
    print("Нет совпадений")
print(f"Количество: {count_matched}")
