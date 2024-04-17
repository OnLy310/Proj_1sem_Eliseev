# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии Достоевского (т.е. с различными окончаниями,
# например, Достоевский, Достоевского) в единственном экземпляре.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

roster = re.findall(r'Досто[её]вск[аиоуыэ][а-я]*', text)

u_roster = set(roster)

print(u_roster)
