# Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

try:
    N = int(input("Введите целое число N (>0): "))
    summa = 0

    for i in range(1, N + 1):
        summa += 1 / i

    print("Сумма равна:  ", summa)
except ValueError:
    print("Введены неверные данные. Попробуйте снова.")
