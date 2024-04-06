# В матрице элементы второго столбца заменить элементами из одномерного динамического массива соответствующей
# размерности.

def replace_second_column(matrix, array):
    if len(matrix) != len(array):
        print("Размеры матрицы и массива должны быть одинаковыми")
        return

    for i in range(len(matrix)):
        matrix[i][1] = array[i]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

array = [10, 11, 12]

replace_second_column(matrix, array)

for row in matrix:
    print(row)
