# Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение.
# Выделить из этой строки имя файла (без расширения).

import os

filename = "C:/Users/User/Documents/PycharmProjects/IS-22/Proj_1sem_Eliseev/PZ_7_9/PZ_7_9_2.py"
basename = os.path.basename(filename)
newname = os.path.splitext(basename)[0]

print(newname)
