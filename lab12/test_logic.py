from logic import (
    validate_records,
    next_id,
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)


def make_sample():
    return [
        {"id": 1, "title": "Бег", "category": "кардио", "amount": 30, "completed": True},
        {"id": 2, "title": "Планка", "category": "силовая", "amount": 5, "completed": False},
        {"id": 3, "title": "Велотренажёр", "category": "кардио", "amount": 45, "completed": True},
        {"id": 4, "title": "Приседания", "category": "силовая", "amount": 15, "completed": False},
        {"id": 5, "title": "Растяжка", "category": "восстановление", "amount": 10, "completed": True},
    ]


def test_validate_ok():
    validate_records(make_sample())
    validate_records([])
    # Дополнительные ключи допустимы
    validate_records([{"id": 1, "title": "X", "category": "Y",
                       "amount": 0, "completed": False, "extra": 42}])


def test_validate_errors():
    cases = [
        ("корень не список", {"a": 1}),
        ("запись не словарь", [1]),
        ("нет ключа id", [{"title": "X", "category": "Y", "amount": 0, "completed": False}]),
        ("id = True", [{"id": True, "title": "X", "category": "Y", "amount": 0, "completed": False}]),
        ("id = 0", [{"id": 0, "title": "X", "category": "Y", "amount": 0, "completed": False}]),
        ("id повтор", [
            {"id": 1, "title": "A", "category": "B", "amount": 0, "completed": False},
            {"id": 1, "title": "C", "category": "D", "amount": 1, "completed": True},
        ]),
        ("title пустой", [{"id": 1, "title": "   ", "category": "Y", "amount": 0, "completed": False}]),
        ("category = 5", [{"id": 1, "title": "X", "category": 5, "amount": 0, "completed": False}]),
        ("amount = True", [{"id": 1, "title": "X", "category": "Y", "amount": True, "completed": False}]),
        ("amount < 0", [{"id": 1, "title": "X", "category": "Y", "amount": -1, "completed": False}]),
        ("completed = 1", [{"id": 1, "title": "X", "category": "Y", "amount": 0, "completed": 1}]),
    ]
    for name, data in cases:
        try:
            validate_records(data)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Ожидалась ошибка: {name}")


def test_next_id():
    assert next_id([]) == 1
    assert next_id(make_sample()) == 6
    assert next_id([{"id": 10}]) == 11


def test_add_record():
    records = []
    record = add_record(records, "  Бег  ", "  кардио ", 30)
    assert record["id"] == 1
    assert record["title"] == "Бег"
    assert record["category"] == "кардио"
    assert record["amount"] == 30
    assert record["completed"] is False
    # Одинаковые названия разрешены, id различается
    second = add_record(records, "Бег", "кардио", 20)
    assert second["id"] == 2
    assert len(records) == 2


def test_add_record_errors():
    for title, category, amount in [("", "c", 1), ("   ", "c", 1),
                                    ("t", "", 1), ("t", "   ", 1),
                                    ("t", "c", -1), ("t", "c", True)]:
        try:
            add_record([], title, category, amount)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Ожидалась ошибка: {title!r}, {category!r}, {amount!r}")


def test_find_records():
    records = make_sample()
    snapshot = [dict(r) for r in records]
    found = find_records(records, "бег")
    assert [r["id"] for r in found] == [1]
    found = find_records(records, "КАРДИО")  # не в title — не найдётся
    assert found == []
    found = find_records(records, "а")  # подстрока "а" в названиях
    # "Планка", "Приседания", "Растяжка"
    assert [r["id"] for r in found] == [2, 4, 5]
    # Исходный список не изменён
    assert records == snapshot
    try:
        find_records(records, "   ")
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалась ошибка на пустой запрос")


def test_set_completed():
    records = make_sample()
    assert set_completed(records, 2, True) is True
    assert records[1]["completed"] is True
    assert set_completed(records, 999, True) is False
    assert set_completed(records, 1, False) is True
    assert records[0]["completed"] is False


def test_delete_record():
    records = make_sample()
    assert delete_record(records, 3) is True
    assert [r["id"] for r in records] == [1, 2, 4, 5]
    assert delete_record(records, 3) is False  # уже удалена
    # id существующих не перенумеровываются
    assert [r["id"] for r in records] == [1, 2, 4, 5]


def test_statistics():
    stats = statistics(make_sample())
    assert stats["total"] == 5
    assert stats["completed"] == 3
    assert stats["not_completed"] == 2
    assert stats["amount_total"] == 105
    assert list(stats["by_category"].keys()) == ["восстановление", "кардио", "силовая"]
    assert stats["by_category"]["кардио"] == 75
    assert stats["by_category"]["силовая"] == 20
    assert stats["by_category"]["восстановление"] == 10
    # Пустой список
    empty = statistics([])
    assert empty["total"] == 0
    assert empty["amount_total"] == 0
    assert empty["by_category"] == {}


def run_all():
    test_validate_ok()
    test_validate_errors()
    test_next_id()
    test_add_record()
    test_add_record_errors()
    test_find_records()
    test_set_completed()
    test_delete_record()
    test_statistics()
    print("test_logic.py: все тесты пройдены.")


if __name__ == "__main__":
    run_all()
