# Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном списке четные числа в порядке
# возрастания их индекса, а затем - все нечетные числа в порядке убывания их индексов.

numbers = [2, 7, 4, 5, 8, 9, 10, 13, 6, 3]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i], "индекс", i)

for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 1:
        print(numbers[i], "индекс", i)
