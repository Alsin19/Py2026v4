## Задание 11

### todos.json
Учебный набор из пяти задач (пользователи 5 и 10), точное содержимое
из условия.

### analysis.py (без input()/print())

- validate_todos(data) — строгая проверка:
  - корень — список; запись — словарь;
  - id: type is int (bool не проходит), > 0, уникален;
  - userId: type is int (bool не проходит), > 0;
  - title: непустая строка;
  - completed: type is bool.
  Дополнительные ключи допустимы. При нарушении — ValueError с пояснением.
- completion_counts(todos) — {userId: число завершённых}; включает всех
  пользователей, даже с нулём завершённых.
- top_users(counts) — отсортированный список userId с максимумом
  завершённых; для пустого словаря или максимума 0 → [].
- select_tasks(todos, user_id, parameter) — задачи пользователя user_id
  с id > parameter (вариант); порядок сохраняется; исходный список не
  меняется; parameter — целое неотрицательное.

Проверки validate_todos (ошибочные случаи):
- корень не список;
- запись не словарь;
- id отсутствует / True / 0 / повтор;
- userId отсутствует / "5" / -1;
- title отсутствует / "" / 123;
- completed отсутствует / 1 / "true".
Все выбрасывают ValueError с указанием записи.

Проверки анализа:
- completion_counts(учебный набор) → {5: 2, 10: 2};
- top_users({5: 2, 10: 2}) → [5, 10];
- top_users({}) → []; top_users({1: 0, 2: 0}) → [];
- select_tasks(todos, 5, 2) → запись id=5 → [5].

### main.py
- Читает todos.json, валидирует, считает completion_counts и top_users,
  выводит сводку.
- Сохраняет завершённые задачи лидеров в leaders.json (исходный порядок;
  userId и id остаются числами).
- Запрашивает положительный userId и неотрицательный порог
  (повторный ввод при ошибке), сохраняет select_tasks в selected.json.
- Обрабатывает FileNotFoundError, UnicodeDecodeError,
  json.JSONDecodeError (раньше общего ValueError), ошибки структуры
  (ValueError из validate_todos), PermissionError и общий OSError.
- При ошибке входных данных main выходит до записи leaders.json /
  selected.json — прежние результаты не перезаписываются.
- Входной файл открывается только на чтение.

### leaders.json (учебный набор)
Завершённые задачи лидеров [5, 10] в исходном порядке: id = [1, 3, 4, 5].

### selected.json (user_id=5, порог=2)
Задачи пользователя 5 с id > 2: только id=5 («Списки»); id = [5] —
совпадает с вариантом.