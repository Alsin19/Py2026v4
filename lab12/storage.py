import json


def load_records(path):
    """Читает JSON-файл UTF-8 и возвращает список записей.
    Не валидирует структуру (это делает logic.validate_records).
    Исключения: FileNotFoundError, UnicodeDecodeError,
    json.JSONDecodeError, PermissionError, OSError."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_records(path, records):
    """Записывает records в JSON-файл UTF-8.
    Возвращает None при успехе; исключения пробрасываются
    (PermissionError, OSError, TypeError при несериализуемых данных)."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
