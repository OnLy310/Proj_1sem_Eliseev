# Задание 1
# Изменить конструктор класса, добавив атрибут iscompleted (True/False).
# Создать экземпляр с новым атрибутом, вывести все значения собственных
# атрибутов экземпляра (__dict__).
# Обеспечить увеличение count на величину, передаваемую в качестве аргумента
# Создать новую функцию reset_count, которая будет обнулять счетчик выполненных задач
# Проверить содержимое магической переменной __dict__


class Note:
    def __init__(self, text, iscompleted):
        self.text = text
        self.count = 0
        self.iscompleted = iscompleted

    def upcount(self, count):
        self.count += count

    def resert_count(self):
        self.count = 0


note1 = Note('Задача 1', True)
print(note1.__dict__)

note1.upcount(3)
print(note1.count)

print(note1.__dict__)

note1.resert_count()
print(note1.count)

print(note1.__dict__)
