# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.

from tkinter import *

def calculate_unoccupied_length():
    try:
        A = int(A_entry.get())
        B = int(B_entry.get())
        if A <= B:
            result_label.config(text="Ошибка: A должно быть больше B")
            return
        unoccupied_length = A % B
        result_label.config(text=f"Длина незанятой части отрезка: {unoccupied_length}")
    except ValueError:
        result_label.config(text="Ошибка: введите целые числа")

root = Tk()
root.title("Рассчитать незанятую длину отрезка")
root.geometry("450x200")

A_label = Label(root, text="Введите длину отрезка A:")
A_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
A_entry = Entry(root)
A_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

B_label = Label(root, text="Введите длину отрезка B:")
B_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
B_entry = Entry(root)
B_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

calculate_button = Button(root, text="Рассчитать", command=calculate_unoccupied_length)
calculate_button.grid(row=2, column=0, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=1, pady=10)

root.mainloop()
