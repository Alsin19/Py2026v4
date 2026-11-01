MEASUREMENT_UNIT = "мин"


def validate_records(records):
    """Строгая проверка списка записей. При нарушении — ValueError.

    Контракт:
    - Принимает корень JSON (список словарей).
    - Не изменяет входные данные.
    - Возвращает None при успехе.
    - Выбрасывает ValueError с пояснением и индексом записи при нарушении.
    """
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком.")

    seen_ids = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Запись #{index}: должна быть словарём.")

        for key in ("id", "title", "category", "amount", "completed"):
            if key not in record:
                raise ValueError(
                    f"Запись #{index}: отсутствует обязательный ключ '{key}'."
                )

        task_id = record["id"]
        if type(task_id) is not int:
            raise ValueError(
                f"Запись #{index}: 'id' должен быть целым (int), "
                f"получено {type(task_id).__name__}."
            )
        if task_id <= 0:
            raise ValueError(
                f"Запись #{index}: 'id' должен быть положительным, "
                f"получено {task_id}."
            )
        if task_id in seen_ids:
            raise ValueError(f"Запись #{index}: id={task_id} повторяется.")
        seen_ids.add(task_id)

        for key in ("title", "category"):
            value = record[key]
            if not isinstance(value, str):
                raise ValueError(
                    f"Запись #{index}: '{key}' должен быть строкой, "
                    f"получено {type(value).__name__}."
                )
            if value.strip() == "":
                raise ValueError(
                    f"Запись #{index}: '{key}' не может быть пустым."
                )

        amount = record["amount"]
        if type(amount) is not int:
            raise ValueError(
                f"Запись #{index}: 'amount' должен быть целым (int), "
                f"получено {type(amount).__name__}."
            )
        if amount < 0:
            raise ValueError(
                f"Запись #{index}: 'amount' должен быть >= 0, "
                f"получено {amount}."
            )

        completed = record["completed"]
        if type(completed) is not bool:
            raise ValueError(
                f"Запись #{index}: 'completed' должен быть bool, "
                f"получено {type(completed).__name__}."
            )

    return None


def next_id(records):
    """Новый id = max существующих + 1; для пустого списка — 1.
    Не изменяет список."""
    maximum = 0
    for record in records:
        if record["id"] > maximum:
            maximum = record["id"]
    return maximum + 1


def add_record(records, title, category, amount):
    """Добавляет запись с completed=False. Изменяет records (append).
    Возвращает новую запись.
    title/category обрезаются strip(); amount — целое >= 0.
    Невалидные аргументы — ValueError (список при этом не меняется)."""
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Название не может быть пустым.")
    if not isinstance(category, str) or category.strip() == "":
        raise ValueError("Категория не может быть пустой.")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество должно быть целым неотрицательным числом.")

    record = {
        "id": next_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Непустая подстрока названия без учёта регистра.
    Не изменяет records. Возвращает новый список совпадений (порядок — как в records).
    Пустой query — ValueError."""
    if not isinstance(query, str) or query.strip() == "":
        raise ValueError("Поисковый запрос не может быть пустым.")
    normalized = query.strip().lower()
    found = []
    for record in records:
        if normalized in record["title"].lower():
            found.append(record)
    return found


def set_completed(records, record_id, completed):
    """Находит запись по id и устанавливает completed.
    Изменяет records. Возвращает True при успехе, False если id не найден."""
    if type(completed) is not bool:
        raise ValueError("Статус должен быть bool.")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись по id. Изменяет records.
    Возвращает True при успехе, False если id не найден."""
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    """Статистика по текущему списку. Не изменяет records.
    Возвращает словарь:
    {
      "total": N,
      "completed": K,
      "not_completed": M,
      "amount_total": S,
      "by_category": {category: sum_amount, ...}   # ключи по алфавиту
    }"""
    total = 0
    completed_count = 0
    amount_total = 0
    by_category = {}

    for record in records:
        total += 1
        if record["completed"]:
            completed_count += 1
        amount_total += record["amount"]
        category = record["category"].strip()
        if category in by_category:
            by_category[category] += record["amount"]
        else:
            by_category[category] = record["amount"]

    # Сортировка категорий по алфавиту
    ordered_categories = {}
    for category in sorted(by_category):
        ordered_categories[category] = by_category[category]

    return {
        "total": total,
        "completed": completed_count,
        "not_completed": total - completed_count,
        "amount_total": amount_total,
        "by_category": ordered_categories,
    }
