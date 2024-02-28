# Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество.

from collections import Counter


def find_common_elements(seq1, seq2):
    # Множества для быстрого поиска общих элементов
    set1 = set(seq1)
    set2 = set(seq2)

    # Нахождение общих элементов
    common_elements = filter(lambda x: x in set1, set2)

    # Количество общих элементов
    common_count = Counter(common_elements)

    return common_count


sequence1 = [1, 2, 3, 4, 5]
sequence2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(sequence1, sequence2)
print("Общие элементы:", common_elements)
