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
