text = input("Введите текст: ")

count_colons = text.count(":")

new_text = text.replace(":", "-")

print()
print(f"Количество замен: {count_colons}")
print(f"Новая строка:     {new_text}")
