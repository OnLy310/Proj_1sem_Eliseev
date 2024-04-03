# В матрице найти среднее арифметическое положительных элементов, кратных 3.

def average_of_multiples(matrix):
    total = 0
    count = 0

    for row in matrix:
        for num in row:
            if num > 0 and num % 3 == 0:
                total += num
                count += 1

    if count == 0:
        return "В матрице нет положительных элементов, кратных 3"
    else:
        return total / count


# Пример матрицы
matrix = [
    [1, 6, 9],
    [12, 5, -3],
    [-6, 8, 10]
]

result = average_of_multiples(matrix)
print("Среднее арифметическое положительных элементов, кратных 3, в матрице:", result)
