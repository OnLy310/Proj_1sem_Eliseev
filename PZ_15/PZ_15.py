# Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной нагрузки по кафедре. Таблица Дисциплины должна
# иметь следующую структуру записи: Код дисциплины, Наименование дисциплины, Специальность, Лекции (кол. часов),
# Практические (кол. часов), Лабораторные (кол. часов), Форма отчетности.

import sqlite3 as sq

with sq.connect('syllabus.db') as con:
    cur = con.cursor()
    con.execute("DROP TABLE IF EXISTS Disciplines")
    cur.execute('''CREATE TABLE IF NOT EXISTS Disciplines (
                  Code INTEGER PRIMARY KEY,
                  Name TEXT,
                  Speciality TEXT,
                  Lectures INTEGER,
                  Practical INTEGER,
                  Laboratory INTEGER,
                  Reporting_form TEXT
                  )''')
    con.commit()


def add_discipline(code, name, speciality, lectures, practical, laboratory, reporting_form):
    cur.execute('''
    INSERT INTO disciplines (Code, Name, Speciality, Lectures, Practical, Laboratory,
    Reporting_form)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (code, name, speciality, lectures, practical, laboratory, reporting_form))
    con.commit()


def findDisciplineByCode(code):
    cur = con.cursor()
    cur.execute('''SELECT * FROM Disciplines WHERE Code = ?''', (code,))
    result = cur.fetchall()
    return result


def findDisciplineByName(name):
    cur = con.cursor()
    cur.execute('''SELECT * FROM Disciplines WHERE Name = ?''', (name,))
    result = cur.fetchall()
    return result


def deleteByNumber(disciplines_id):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''DELETE FROM Disciplines WHERE disciplines_id = ?''', (disciplines_id, ))
    con.commit()
    con.close()


def deleteByLectures(lectures):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''DELETE FROM Disciplines WHERE Lectures = ?''', (lectures,))
    con.commit()
    con.close()


def deleteByPractical(practical):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''DELETE FROM Disciplines WHERE Practical = ?''', (practical,))
    con.commit()
    con.close()


def updateBySpeciality(Code, newSpeciality):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''UPDATE Disciplines
                 SET Speciality = ?
                 WHERE Code = ?''', (Code, newSpeciality,))
    con.commit()
    con.close()


def updateByName(Code, newName):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''UPDATE Disciplines
                 SET Name = ?
                 WHERE Code = ?''', (Code, newName,))
    con.commit()
    con.close()


def updateByLectures(Code, newLectures):
    con = sq.connect("syllabus.db")
    cur = con.cursor()
    cur.execute('''UPDATE Disciplines
                 SET Lectures = ?
                 WHERE Code = ?''', (Code, newLectures,))
    con.commit()
    con.close()


add_discipline(1, 'Математика', 'Математика', 20, 30, 10, 'Экзамен')
add_discipline(2, 'Русский язык', 'Русская филология', 25, 35, 15, 'Экзамен')
add_discipline(3, 'История', 'История', 30, 45, 25, 'Экзамен')
add_discipline(4, 'Химия', 'Химия', 50, 37, 28, 'Экзамен')
add_discipline(5, 'Физика', 'Физика', 47, 52, 15, 'Экзамен')
add_discipline(6, 'География', 'География', 15, 25, 5, 'Экзамен')
add_discipline(7, 'Литература', 'Литература', 55, 45, 25, 'Экзамен')
add_discipline(8, 'Биология', 'Биология', 20, 25, 15, 'Экзамен')
add_discipline(9, 'Физическая культура', 'Физическая культура', 5, 8, 7, 'Экзамен')
add_discipline(10, 'Английский язык', 'Английский язык', 35, 45, 25, 'Экзамен')


def getDisciplines():
    con = sq.connect("syllabus.db")
    c = con.cursor()
    c.execute('SELECT * FROM disciplines')
    return c.fetchall()


for disciplines in getDisciplines():
    print(disciplines)

con.close()
