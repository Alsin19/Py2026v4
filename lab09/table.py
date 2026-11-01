def row_sums(matrix):
    """Список сумм строк. Для [] возвращает []."""
    result = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        result.append(total)
    return result


def column_sums(matrix):
    """Список сумм столбцов. Для [] возвращает [].
    Непустая матрица прямоугольная и имеет хотя бы один столбец."""
    if not matrix:
        return []
    column_count = len(matrix[0])
    result = []
    for column_index in range(column_count):
        total = 0
        for row in matrix:
            total += row[column_index]
        result.append(total)
    return result


def diagonal_pattern(size):
    """Квадратная таблица size×size: 0 на главной диагонали, 1 выше, 2 ниже.
    size >= 1."""
    pattern = []
    for row in range(size):
        pattern_row = []
        for column in range(size):
            if row == column:
                pattern_row.append(0)
            elif row < column:
                pattern_row.append(1)
            else:  # row > column
                pattern_row.append(2)
        pattern.append(pattern_row)
    return pattern


def transform(matrix):
    """Новая матрица той же формы: нечётные элементы заменены нулями.
    Исходная матрица не изменяется. Для [] возвращает []."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value % 2 != 0:
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
