# Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной нагрузки по кафедре. Таблица Дисциплины должна
# иметь следующую структуру записи: Код дисциплины, Наименование дисциплины, Специальность, Лекции (кол. часов),
# Практические (кол. часов), Лабораторные (кол. часов), Форма отчетности.

import sqlite3

conn = sqlite3.connect('учебный_план.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Дисциплины (
                  Код INTEGER PRIMARY KEY,
                  Наименование TEXT,
                  Специальность TEXT,
                  Лекции INTEGER,
                  Практические INTEGER,
                  Лабораторные INTEGER,
                  Форма_отчетности TEXT)''')
conn.commit()


def add_discipline(code, name, speciality, lectures, practical, laboratory, reporting_form):
    cursor.execute('''INSERT INTO Дисциплины (Код, Наименование, Специальность, Лекции, Практические, Лабораторные,
    Форма_отчетности)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (code, name, speciality, lectures, practical, laboratory,
                                                        reporting_form))
    conn.commit()


def find_discipline_by_code(code):
    cursor.execute('''SELECT * FROM Дисциплины WHERE Код = ?''', (code,))
    return cursor.fetchall()


def find_discipline_by_name(name):
    cursor.execute('''SELECT * FROM Дисциплины WHERE Наименование = ?''', (name,))
    return cursor.fetchall()

# Поиск по другим полям и для удаления и редактирования записей


add_discipline(1, 'Математика', 'Математика', 20, 30, 10, 'Экзамен')
result = find_discipline_by_code(1)
print(result)

# Закрытие соединения с базой данных
conn.close()
