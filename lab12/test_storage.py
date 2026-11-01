import json
import os
import tempfile

from storage import load_records, save_records
from logic import validate_records


def test_roundtrip():
    records = [
        {"id": 1, "title": "Бег", "category": "кардио", "amount": 30, "completed": True},
        {"id": 2, "title": "Планка", "category": "силовая", "amount": 5, "completed": False},
    ]
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "data.json")
        save_records(path, records)
        loaded = load_records(path)
        assert loaded == records
        validate_records(loaded)
        # Повторная загрузка
        assert load_records(path) == records


def test_load_missing():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "missing.json")
        try:
            load_records(path)
        except FileNotFoundError:
            pass
        else:
            raise AssertionError("Ожидалась FileNotFoundError")


def test_load_bad_json():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "bad.json")
        with open(path, "w", encoding="utf-8") as f:
            f.write("{not valid json")
        try:
            load_records(path)
        except json.JSONDecodeError:
            pass
        else:
            raise AssertionError("Ожидалась JSONDecodeError")


def test_load_bad_utf8():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "bad_utf8.json")
        with open(path, "wb") as f:
            f.write(b"\xff\xfe\x00")
        try:
            load_records(path)
        except UnicodeDecodeError:
            pass
        else:
            raise AssertionError("Ожидалась UnicodeDecodeError")


def run_all():
    test_roundtrip()
    test_load_missing()
    test_load_bad_json()
    test_load_bad_utf8()
    print("test_storage.py: все тесты пройдены.")


if __name__ == "__main__":
    run_all()
