# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего максимального элемента:
# Меняем местами первую и последнюю трети:
# 2. Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое, количество букв в нижнем
# регистре. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю
# строку фразой введенной пользователем.

import random

sequence = [random.randint(-100, 100) for _ in range(20)]

# Запись последовательности в файл
with open('sequence.txt', 'w') as file:
    file.write('Исходные данные:\n')
    file.write(', '.join(map(str, sequence)) + '\n')
    file.write(f'Количество элементов: {len(sequence)}\n')
    file.write(f'Индекс последнего максимального элемента: {sequence.index(max(sequence))}\n')

# Меняем местами
third = len(sequence) // 3
sequence[:third], sequence[-third:] = sequence[-third:], sequence[:third]

# Запись в файл
with open('modified_sequence.txt', 'w') as file:
    file.write('Исходные данные после изменения:\n')
    file.write(', '.join(map(str, sequence)))


# Чтение файла и подсчет букв в нижнем регистре
with open('text18-9.txt', 'r', encoding='UTF-16') as file:
    content = file.read()
    lowercase_count = sum(1 for char in content if char.islower())

# Вывод
print("Содержимое файла:")
print(content)
print(f"Количество букв в нижнем регистре: {lowercase_count}")

# Получение последней строки от пользователя
last_line = input("Введите последнюю строку для стихотворения: ")

# Запись текста в стихотворной форме
with open('poem.txt', 'w') as file:
    file.write(content + '\n')
    file.write(last_line)
