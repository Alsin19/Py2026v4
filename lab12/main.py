import json

from logic import (
    MEASUREMENT_UNIT,
    validate_records,
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)
from storage import load_records, save_records


DATA_PATH = "data.json"


def read_nonempty_text(prompt):
    """Непустая строка после strip(); повтор при ошибке."""
    while True:
        raw = input(prompt)
        if raw.strip() == "":
            print("Ошибка: значение не может быть пустым. Попробуйте снова.")
            continue
        return raw.strip()


def read_nonnegative_int(prompt):
    """Целое >= 0; повтор при ошибке. bool-подобный ввод не возможен из int()."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число. Попробуйте снова.")
            continue
        if value < 0:
            print("Ошибка: число не может быть отрицательным. Попробуйте снова.")
            continue
        return value


def read_positive_int(prompt):
    """Целое > 0; повтор при ошибке."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число. Попробуйте снова.")
            continue
        if value <= 0:
            print("Ошибка: число должно быть больше нуля. Попробуйте снова.")
            continue
        return value



def load_and_validate(path):
    """Читает и валидирует data.json. Возвращает список или None при ошибке.
    При ошибке печатает причину и НЕ перезаписывает файл."""
    try:
        records = load_records(path)
    except FileNotFoundError:
        print(f"Файл '{path}' не найден. Начинаем с пустого списка.")
        return []
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
        validate_records(records)
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return None

    return records



def save_safely(path, records):
    """Пытается сохранить. Возвращает True при успехе, False при ошибке."""
    try:
        save_records(path, records)
    except PermissionError:
        print(f"Ошибка: нет доступа для записи в '{path}'.")
        return False
    except OSError as error:
        print(f"Ошибка файлового доступа при записи: {error}")
        return False
    print(f"Данные успешно сохранены в '{path}'.")
    return True


def show_records(records):
    print()
    if not records:
        print("Нет записей")
        return
    print("ID  | Название             | Категория        | Кол-во     | Статус")
    print("-" * 80)
    for record in sorted(records, key=lambda r: r["id"]):
        status = "выполнено" if record["completed"] else "не выполнено"
        print(
            f"{record['id']:<3} | {record['title']:<20} | "
            f"{record['category']:<16} | {record['amount']} {MEASUREMENT_UNIT:<3} | {status}"
        )


def do_add(records):
    title = read_nonempty_text("Название: ")
    category = read_nonempty_text("Категория: ")
    amount = read_nonnegative_int("Продолжительность в минутах (>= 0): ")
    try:
        new_record = add_record(records, title, category, amount)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    print(f"Добавлена запись id={new_record['id']}.")


def do_find(records):
    query = read_nonempty_text("Поиск по названию (непустая подстрока): ")
    try:
        found = find_records(records, query)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    if not found:
        print("Ничего не найдено.")
        return
    for record in found:
        status = "выполнено" if record["completed"] else "не выполнено"
        print(
            f"id={record['id']} | {record['title']} | "
            f"{record['category']} | {record['amount']} {MEASUREMENT_UNIT} | {status}"
        )


def do_set_completed(records):
    record_id = read_positive_int("ID записи: ")
    while True:
        answer = input("Установить статус 'выполнено'? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            break
        print("Ошибка: ответьте 'да' или 'нет'.")
    completed = answer == "да"
    if set_completed(records, record_id, completed):
        state = "выполнено" if completed else "не выполнено"
        print(f"Статус записи id={record_id}: {state}.")
    else:
        print(f"Запись с id={record_id} не найдена.")


def do_delete(records):
    record_id = read_positive_int("ID записи для удаления: ")
    answer = input(f"Удалить запись id={record_id}? (да/нет): ").strip().lower()
    if answer != "да":
        print("Удаление отменено.")
        return
    if delete_record(records, record_id):
        print(f"Запись id={record_id} удалена.")
    else:
        print(f"Запись с id={record_id} не найдена.")


def do_statistics(records):
    stats = statistics(records)
    print()
    print(f"Всего записей:       {stats['total']}")
    print(f"Выполнено:           {stats['completed']}")
    print(f"Не выполнено:        {stats['not_completed']}")
    print(f"Сумма {MEASUREMENT_UNIT}:            {stats['amount_total']}")
    print("По категориям:")
    if not stats["by_category"]:
        print("  (нет категорий)")
    else:
        for category, total in stats["by_category"].items():
            print(f"  {category}: {total} {MEASUREMENT_UNIT}")


def ask_save_and_exit(records):
    """Выход: предложить сохранить. Возвращает True, если можно выходить."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            if save_safely(DATA_PATH, records):
                return True
            print("Не удалось сохранить. Остаёмся в меню.")
            return False
        if answer == "нет":
            return True
        print("Ошибка: ответьте 'да' или 'нет'.")


def print_menu():
    print()
    print("=== План тренировок ===")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")


def main():
    records = load_and_validate(DATA_PATH)
    if records is None:
        print("Запуск завершён: входные данные некорректны.")
        return

    while True:
        print_menu()
        command = input("Выберите пункт: ").strip()

        if command == "1":
            show_records(records)
        elif command == "2":
            do_add(records)
        elif command == "3":
            do_find(records)
        elif command == "4":
            do_set_completed(records)
        elif command == "5":
            do_delete(records)
        elif command == "6":
            do_statistics(records)
        elif command == "7":
            save_safely(DATA_PATH, records)
        elif command == "8":
            if ask_save_and_exit(records):
                print("До свидания.")
                return
        else:
            print("Неизвестная команда. Повторите выбор.")


if __name__ == "__main__":
    main()
