def read_matrix(path):
    """Читает матрицу из файла и возвращает список списков целых.

    Формат:
    - первая строка: два положительных целых — rows cols;
    - далее ровно rows строк, в каждой ровно cols целых чисел;
    - лишние и пустые строки — ошибка;
    - один обычный перевод строки после последней строки данных допустим.

    При ошибке формата выбрасывает ValueError с пояснением и номером строки.
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Файл пуст: отсутствует заголовок 'rows cols'.")

    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError(
            f"Строка 1: заголовок должен содержать ровно два целых числа "
            f"'rows cols', получено {len(header_parts)} частей."
        )
    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError(
            f"Строка 1: заголовок содержит нецелые значения "
            f"'{header_parts[0]}' и/или '{header_parts[1]}'."
        )
    if rows <= 0 or cols <= 0:
        raise ValueError(
            f"Строка 1: rows и cols должны быть положительными, "
            f"получено rows={rows}, cols={cols}."
        )

    data_lines = lines[1:]

    if any(line.strip() == "" for line in data_lines):
        # Находим первую пустую строку для сообщения
        for offset, line in enumerate(data_lines, start=2):
            if line.strip() == "":
                raise ValueError(
                    f"Строка {offset}: пустая строка внутри данных."
                )

    if len(data_lines) > rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, но найдено {len(data_lines)} "
            f"(лишние строки после строки {rows + 1})."
        )
    if len(data_lines) < rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, но найдено {len(data_lines)} "
            f"(не хватает {rows - len(data_lines)} строк)."
        )

    matrix = []
    for row_index, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(
                f"Строка {row_index}: ожидалось {cols} чисел, "
                f"получено {len(parts)}."
            )
        row_values = []
        for part in parts:
            try:
                row_values.append(int(part))
            except ValueError:
                raise ValueError(
                    f"Строка {row_index}: '{part}' не является целым числом."
                )
        matrix.append(row_values)

    return matrix
