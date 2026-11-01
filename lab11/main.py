import json

from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    select_tasks,
)


def read_positive_integer(prompt):
    """Повторяет ввод, пока не получено целое > 0."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число. Попробуйте снова.")
            continue
        if value <= 0:
            print("Ошибка: должно быть больше нуля. Попробуйте снова.")
            continue
        return value


def read_nonnegative_integer(prompt):
    """Повторяет ввод, пока не получено целое >= 0."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число. Попробуйте снова.")
            continue
        if value < 0:
            print("Ошибка: должно быть неотрицательным. Попробуйте снова.")
            continue
        return value


def load_todos(path):
    """Читает и валидирует todos.json. При ошибках печатает и возвращает None."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл '{path}' не найден.")
        return None
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{path}' не является корректным UTF-8.")
        return None
    except json.JSONDecodeError as error:
        # JSONDecodeError — подкласс ValueError, обработчик стоит раньше
        print(f"Ошибка JSON в '{path}': {error}.")
        return None
    except PermissionError:
        print(f"Ошибка: нет доступа к файлу '{path}'.")
        return None
    except OSError as error:
        print(f"Ошибка файлового доступа: {error}")
        return None

    try:
        validate_todos(data)
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return None

    return data


def write_json(path, payload):
    """Записывает payload в JSON-файл UTF-8. Возвращает True при успехе."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
            file.write("\n")
    except PermissionError:
        print(f"Ошибка: нет доступа для записи в '{path}'.")
        return False
    except OSError as error:
        print(f"Ошибка файлового доступа при записи: {error}")
        return False
    return True


def main():
    input_path = "todos.json"
    leaders_path = "leaders.json"
    selected_path = "selected.json"

    todos = load_todos(input_path)
    if todos is None:
        print("Результаты не перезаписываются: входные данные некорректны.")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)

    print("Сводка по завершённым задачам:")
    for user_id in sorted(counts):
        print(f"  Пользователь {user_id}: {counts[user_id]}")
    print(f"Лидеры: {leaders}")

    leader_tasks = []
    for record in todos:
        if record["userId"] in leaders and record["completed"]:
            leader_tasks.append(record)
    if not write_json(leaders_path, leader_tasks):
        return
    print(f"Завершённые задачи лидеров сохранены в '{leaders_path}'.")

    user_id = read_positive_integer("Введите userId (целое > 0): ")
    threshold = read_nonnegative_integer(
        "Введите порог для условия 'id больше порога' (целое >= 0): "
    )

    try:
        selected = select_tasks(todos, user_id, threshold)
    except ValueError as error:
        print(f"Ошибка отбора: {error}")
        return

    if not write_json(selected_path, selected):
        return
    print(f"Отобранные задачи сохранены в '{selected_path}'.")
    print(f"Найдено задач: {len(selected)}")


if __name__ == "__main__":
    main()
