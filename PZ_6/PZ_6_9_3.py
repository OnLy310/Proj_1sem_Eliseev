# Дано множество A из N точек на плоскости и точка B (точки заданы своими координатами x, y). Найти точку из множества
# A, наиболее близкую к точке B. Расстояние R между точками с координатами (x1, y1) и (x2, y2) вычисляется по формуле:
# R = √(x2 - x1)^2 + (y2 - y1)^2.

import math


def closest_point(a, b):
    min_distance = float('inf')
    closest = None

    for point in a:
        distance = math.sqrt((b[0]) - point[0] ** 2 + (b[1]) - point[1] ** 2)

        if distance < min_distance:
            closest = point

        return closest


a = [(1, 2), (3, 4), (5, 6)]
b = (2, 3)

result = closest_point(a, b)
print("Ближайшая точка из множества A к точке B: ", result)
