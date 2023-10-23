# Даны два целых числа: A, B. Проверить истинность высказывания: "Хотя бы одно из чисел A и B нечетное".

try:
    A = int(input("Введите целое число A: "))
    B = int(input("Введите целое число B: "))

    if A % 2 != 0 or B % 2 != 0:
        print("Высказывание истинно")
    else:
        print("Высказывание ложно")

except (ZeroDivisionError, ValueError):
    print("Введены неверные данные. Попробуйте снова.")
