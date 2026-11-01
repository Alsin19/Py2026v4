from files_lab import read_matrix
from table import row_sums, column_sums


def read_positive_integer():
    """Повторяет ввод, пока не получено целое число > 0.
    Различает сообщения «не целое число» и «должно быть больше нуля»."""
    while True:
        raw = input("Введите положительное целое число: ")
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число. Попробуйте снова.")
            continue
        if value <= 0:
            print("Ошибка: должно быть больше нуля. Попробуйте снова.")
            continue
        return value


def sum_odd(matrix):
    """Сумма нечётных элементов матрицы (вариант задания).
    Использует исходную матрицу, ничего не меняет."""
    total = 0
    for row in matrix:
        for value in row:
            if value % 2 != 0:
                total += value
    return total


def format_row(values):
    """Числа строкой через пробел (для отчёта)."""
    return " ".join(str(value) for value in values)


def main():
    input_path = "matrix.txt"
    report_path = "report.txt"

    try:
        matrix = read_matrix(input_path)
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_path}' не найден.")
        return
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{input_path}' не является корректным UTF-8.")
        return
    except PermissionError:
        print(f"Ошибка: нет доступа к файлу '{input_path}'.")
        return
    except OSError as error:
        print(f"Ошибка файлового доступа: {error}")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return

    rows_total = row_sums(matrix)
    columns_total = column_sums(matrix)
    odd_sum = sum_odd(matrix)

    report_lines = [
        f"Суммы строк: {format_row(rows_total)}",
        f"Суммы столбцов: {format_row(columns_total)}",
        f"Результат варианта: {odd_sum}",
    ]
    report_text = "\n".join(report_lines) + "\n"

    try:
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)
    except PermissionError:
        print(f"Ошибка: нет доступа для записи в '{report_path}'.")
        return
    except OSError as error:
        print(f"Ошибка файлового доступа при записи: {error}")
        return

    print(f"Отчёт успешно записан в '{report_path}'.")


if __name__ == "__main__":
    main()
