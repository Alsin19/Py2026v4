def sum_digits(number):
    """Сумма цифр модуля целого числа. Для нуля — 0."""
    value = abs(number)   # сначала модуль, иначе отрицательное не приблизится к 0 при // 10
    total = 0
    if value == 0:
        return 0
    while value > 0:
        total += value % 10
        value //= 10
    return total


def average(numbers):
    """Среднее списка чисел или None для пустого списка. Список не меняется."""
    if not numbers:
        return None
    total = 0
    count = 0
    for value in numbers:
        total += value
        count += 1
    return total / count


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    words = text.split()          # режет по любым пробельным сериям и убирает края
    normalized = " ".join(words)
    return normalized.lower()


def select_numbers(numbers, threshold):
    """Новый список чисел не меньше порога; порядок и повторы сохраняются."""
    selected = []
    for value in numbers:
        if value >= threshold:
            selected.append(value)
    return selected
