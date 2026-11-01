def validate_todos(data):
    """Строгая проверка набора задач. При нарушении — ValueError.
    Корень — список словарей. Поля:
    - id: положительный int (type is int, не bool), уникальный;
    - userId: положительный int (type is int, не bool);
    - title: непустая строка;
    - completed: bool (type is bool).
    Дополнительные ключи допустимы.
    """
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком.")

    seen_ids = set()
    for index, record in enumerate(data):
        if not isinstance(record, dict):
            raise ValueError(f"Запись #{index}: должна быть словарём.")

        if "id" not in record:
            raise ValueError(f"Запись #{index}: отсутствует поле 'id'.")
        task_id = record["id"]
        if type(task_id) is not int:
            raise ValueError(
                f"Запись #{index}: поле 'id' должно быть целым (int), "
                f"получено {type(task_id).__name__}."
            )
        if task_id <= 0:
            raise ValueError(
                f"Запись #{index}: поле 'id' должно быть положительным, "
                f"получено {task_id}."
            )
        if task_id in seen_ids:
            raise ValueError(
                f"Запись #{index}: id={task_id} повторяется."
            )
        seen_ids.add(task_id)

        # --- userId ---
        if "userId" not in record:
            raise ValueError(f"Запись #{index}: отсутствует поле 'userId'.")
        user_id = record["userId"]
        if type(user_id) is not int:
            raise ValueError(
                f"Запись #{index}: поле 'userId' должно быть целым (int), "
                f"получено {type(user_id).__name__}."
            )
        if user_id <= 0:
            raise ValueError(
                f"Запись #{index}: поле 'userId' должно быть положительным, "
                f"получено {user_id}."
            )

        # --- title ---
        if "title" not in record:
            raise ValueError(f"Запись #{index}: отсутствует поле 'title'.")
        title = record["title"]
        if not isinstance(title, str):
            raise ValueError(
                f"Запись #{index}: поле 'title' должно быть строкой, "
                f"получено {type(title).__name__}."
            )
        if title == "":
            raise ValueError(
                f"Запись #{index}: поле 'title' не может быть пустым."
            )

        # --- completed ---
        if "completed" not in record:
            raise ValueError(
                f"Запись #{index}: отсутствует поле 'completed'."
            )
        completed = record["completed"]
        if type(completed) is not bool:
            raise ValueError(
                f"Запись #{index}: поле 'completed' должно быть bool, "
                f"получено {type(completed).__name__}."
            )

    return None


def completion_counts(todos):
    """Словарь «userId → число завершённых задач».
    Включает всех пользователей, даже с нулём завершённых."""
    counts = {}
    for record in todos:
        user_id = record["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if record["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Отсортированный список userId с максимальным числом завершённых.
    Для пустого словаря или максимума 0 — []."""
    if not counts:
        return []
    maximum = 0
    first = True
    for value in counts.values():
        if first or value > maximum:
            maximum = value
            first = False
    if maximum == 0:
        return []
    leaders = []
    for user_id, value in counts.items():
        if value == maximum:
            leaders.append(user_id)
    leaders.sort()
    return leaders


def select_tasks(todos, user_id, parameter=None):
    """Задачи пользователя user_id, удовлетворяющие условию варианта.
    Вариант: id больше порога. parameter — целое неотрицательное число.
    Порядок записей сохраняется. Исходный список не меняется."""
    if parameter is None:
        raise ValueError("Для варианта требуется параметр-порог (id > порог).")
    if type(parameter) is not int:
        raise ValueError("Порог должен быть целым числом.")
    if parameter < 0:
        raise ValueError("Порог должен быть неотрицательным.")

    selected = []
    for record in todos:
        if record["userId"] != user_id:
            continue
        if record["id"] > parameter:
            selected.append(record)
    return selected
