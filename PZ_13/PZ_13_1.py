def replace_column(matrix, array):
    if len(matrix) != len(array):
        print("Размерности матрицы и массива не совпадают")
        return

    for row, value in zip(matrix, array):
        row[1] = value


# Пример использования
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

array = [10, 11, 12]

replace_column(matrix, array)

for row in matrix:
    print(row)
