# В матрице найти среднее арифметическое положительных элементов, кратных 3.

def multiple_of_3(x):
    return x > 0 and x % 3 == 0


def average_of_multiples_of_3(matrix):
    positive_multiples_of_3 = filter(multiple_of_3, [element for row in matrix for element in row])

    count = 0
    total = 0
    for element in positive_multiples_of_3:
        count += 1
        total += element

    return total / count if count > 0 else "В матрице нет положительных элементов, кратных 3."


# Пример матрицы
matrix = [
    [3, 6, 9],
    [12, 15, 18],
    [21, -4, 5]
]

print("Среднее арифметическое положительных элементов, кратных 3, в матрице:",
      average_of_multiples_of_3(matrix))
