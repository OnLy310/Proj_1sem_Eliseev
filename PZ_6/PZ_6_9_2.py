# Дан список размера N. Найти количество участков, на которых его элементы монотонно убывают.

def decrease_selection(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i-1]:
            count += 1
    return count


my_list = [5, 4, 8, 3, 2, 1, 6, 5, 4, 3, 2]
result = decrease_selection(my_list)
print("Количество участков, на которых элементы монотонно убывают:", result)
