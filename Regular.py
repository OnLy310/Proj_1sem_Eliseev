import re
p = re.compile(r"красн((ая)|(ое))")
print("Найдено" if p.search("красная") else "Нет")
# Выдаст Найдено

print("Найдено" if p.search("красное") else "Нет")
# Выдаст Найдено

print("Найдено" if p.search("красный") else "Нет")
# Выдаст Нет
