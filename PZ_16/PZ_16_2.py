# Создание базового класса "Работник" и его наследование для создания классов "Менеджер" и "Инженер". В классе
# "Работник" будут общие методы, такие как "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать системы".

class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} работает."

    def get_salary(self):
        return f"{self.name}а зарплата {self.salary}."


class Manager(Worker):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def manage_team(self):
        return f"{self.name} управляет командой."


class Engineer(Worker):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def design_systems(self):
        return f"{self.name} занимается проектированием систем."


manager1 = Manager("Джон", 50000, ["Элис", "Боб", "Чарли"])
engineer1 = Engineer("Элис", 60000, ["Проект А", "Проект Б"])

print(manager1.work())
print(manager1.get_salary())
print(manager1.manage_team())

print(engineer1.work())
print(engineer1.get_salary())
print(engineer1.design_systems())
