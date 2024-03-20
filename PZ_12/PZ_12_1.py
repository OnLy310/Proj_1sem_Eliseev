# Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество.

sequence1 = [1, 2, 3, 4, 5]
sequence2 = [4, 5, 6, 7, 8]

common_elements = list(filter(lambda x: x in sequence1, sequence2))
common_count = len(common_elements)

print("Общие элементы:", common_elements)
print("Количество общих элементов:", common_count)
