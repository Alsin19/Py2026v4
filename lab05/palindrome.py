text = input("Введите текст: ")

cleaned_chars = []
for char in text:
    if char != " ":
        cleaned_chars.append(char.lower())
cleaned = "".join(cleaned_chars)

if cleaned == "":
    print("Нет текста")
else:
    # Срез [::-1] даёт перевёрнутую строку
    if cleaned == cleaned[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
