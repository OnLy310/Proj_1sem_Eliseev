# Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной нагрузки по кафедре. Таблица Дисциплины должна
# иметь следующую структуру записи: Код дисциплины, Наименование дисциплины, Специальность, Лекции (кол. часов),
# Практические (кол. часов), Лабораторные (кол. часов), Форма отчетности.

import sqlite3 as sq

with sq.connect('учебный_план.db') as con:
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Дисциплины (
                  Код INTEGER PRIMARY KEY,
                  Наименование TEXT,
                  Специальность TEXT,
                  Лекции INTEGER,
                  Практические INTEGER,
                  Лабораторные INTEGER,
                  Форма_отчетности TEXT)''')
con.commit()


def add_discipline(code, name, speciality, lectures, practical, laboratory, reporting_form):
    cursor.execute('''INSERT INTO Дисциплины (Код, Наименование, Специальность, Лекции, Практические, Лабораторные,
    Форма_отчетности)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (code, name, speciality, lectures, practical, laboratory,
                                                        reporting_form))
    con.commit()


def find_discipline_by_code(code):
    cursor.execute('''SELECT * FROM Дисциплины WHERE Код = ?''', (code,))
    return cursor.fetchall()


def find_discipline_by_name(name):
    cursor.execute('''SELECT * FROM Дисциплины WHERE Наименование = ?''', (name,))
    return cursor.fetchall()

# Поиск по другим полям для удаления и редактирования


add_discipline(1, 'Математика', 'Математика', 20, 30, 10, 'Экзамен')
result = find_discipline_by_code(1)
print(result)

con.close()
