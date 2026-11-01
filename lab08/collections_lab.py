def word_counts(text):
    """Словарь «слово → количество».
    Нижний регистр, разбиение по пробельным символам,
    удаление .,!?;: с краёв, пропуск пустых результатов.
    Пустой текст → {}."""
    counts = {}
    for raw_word in text.split():
        word = raw_word.strip(".,!?;:").lower()
        if word == "":
            continue
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def print_counts_sorted(counts):
    """Печать пар «слово → количество» по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список общих тем (темы уже в нижнем регистре)."""
    common = set(first) & set(second)
    return sorted(common)


def all_topics(first, second):
    """Отсортированный список всех уникальных тем."""
    unique = set(first) | set(second)
    return sorted(unique)

def demo_record():
    """Словарь записи: изменение значения и добавление ключа; кортеж и распаковка."""
    record = {"title": "Утренняя пробежка", "hours": 1}

    record["hours"] = 2
    record["completed"] = False

    print(f"Запись после изменений: {record}")

    # Кортеж из title и hours, затем распаковка
    title_hours = (record["title"], record["hours"])
    title, hours = title_hours
    print(f"Кортеж: {title_hours}")
    print(f"Распаковано: title = '{title}', hours = {hours}")

def demo_records():
    """Пять содержательных записей с тремя категориями; одна повторяется."""
    records = [
        {"title": "Бег",            "category": "кардио",     "amount": 30},
        {"title": "Планка",         "category": "силовая",    "amount": 5},
        {"title": "Велотренажёр",   "category": "кардио",     "amount": 45},
        {"title": "Приседания",     "category": "силовая",    "amount": 15},
        {"title": "Растяжка",       "category": "восстановление", "amount": 10},
    ]
    for rec in records:
        print(f"{rec['title']:<15} | {rec['category']:<15} | {rec['amount']} мин")


if __name__ == "__main__":
    print("=== word_counts ===")
    text = input("Введите текст: ")
    counts = word_counts(text)
    if not counts:
        print("{}")
    else:
        print_counts_sorted(counts)

    print()
    print("=== common_topics / all_topics ===")
    first = ["python", "sql", "git"]
    second = ["sql", "git", "docker"]
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы:   {all_topics(first, second)}")

    print()
    print("=== Словарь и кортеж ===")
    demo_record()

    print()
    print("=== Записи (тренировки) ===")
    demo_records()
