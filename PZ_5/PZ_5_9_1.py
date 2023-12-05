# Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.
import random


def check_duplicates():
    number = random.randint(1000, 9999)
    digits = str(number)
    print(number)

    if len(set(digits)) != len(digits):
        return True
    else:
        return False


result = check_duplicates()
if result:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")
