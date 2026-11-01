original = input("Введите строку: ")

words = original.split()
normalized = " ".join(words)

original_length = len(original)
normalized_length = len(normalized)
word_count = len(words)

print()
print(f"Исходная длина:      {original_length}")
print(f"Новая длина:         {normalized_length}")
print(f"Нормализованный текст: '{normalized}'")
print(f"Количество слов:     {word_count}")
