# Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и "деление". Каждый метод должен
# принимать два аргумента и возвращать результат операции.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b


# Пример использования класса с вводом значений с клавиатуры
calc = Calculator()

# Ввод значений с клавиатуры
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Примеры операций
print(f"Сложение: {a} + {b} = {calc.add(a, b)}")
print(f"Вычитание: {a} - {b} = {calc.subtract(a, b)}")
print(f"Умножение: {a} * {b} = {calc.multiply(a, b)}")
try:
    print(f"Деление: {a} / {b} = {calc.division(a, b)}")
except ValueError as e:
    print(e)
