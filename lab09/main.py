from table import row_sums, column_sums, diagonal_pattern, transform

rows_count = int(input("Количество строк матрицы: "))
if rows_count < 0:
    print("Ошибка: количество строк не может быть отрицательным.")
    raise SystemExit(1)

matrix = []
if rows_count > 0:
    first_line = input("Строка 1 (числа через пробел): ")
    first_row = [int(token) for token in first_line.split()]
    if not first_row:
        print("Ошибка: строка не может быть пустой.")
        raise SystemExit(1)
    expected_length = len(first_row)
    matrix.append(first_row)

    for i in range(2, rows_count + 1):
        line = input(f"Строка {i} (числа через пробел): ")
        row = [int(token) for token in line.split()]
        if len(row) != expected_length:
            print(f"Ошибка: в строке {i} {len(row)} элементов, "
                  f"ожидалось {expected_length}.")
            raise SystemExit(1)
        matrix.append(row)

print()
print(f"Матрица: {matrix}")

print(f"Суммы строк:    {row_sums(matrix)}")
print(f"Суммы столбцов: {column_sums(matrix)}")

size = int(input("Размер диагонального узора (целое >= 1): "))
if size < 1:
    print("Ошибка: размер должен быть >= 1.")
    raise SystemExit(1)

pattern = diagonal_pattern(size)
print()
print(f"Диагональный узор {size}×{size}:")
for pattern_row in pattern:
    print(" ".join(str(value) for value in pattern_row))

transformed = transform(matrix)
print()
print(f"Исходная матрица:   {matrix}")
print(f"Новая матрица:      {transformed}")
