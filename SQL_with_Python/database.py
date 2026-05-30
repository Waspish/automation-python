"""
Задание
Напишите Python-скрипт, который выполняет следующие шаги в строгой последовательности.
Используйте библиотеку mysql.connector и все операции должны быть реализованы
через функции (как в примере ниже).

Шаг 1. Подключение и создание курсора
Установите соединение с БД и создайте курсор с параметром dictionary=True.

Шаг 2. Добавление нового студента
Создайте функцию insert_into_students(cursor, name, second_name), которая вставляет запись
в таблицу students (поле group_id пока оставить NULL) и возвращает id нового студента.
Вызовите функцию, передав свои имя и фамилию (например, 'Иван', 'Петров').
 Сохраните полученный student_id.

Шаг 3. Добавление книг для студента
Создайте список из двух книг (названия придумайте сами).
Используя executemany, вставьте обе книги в таблицу books,
указав taken_by_student_id равным student_id из шага 2.

Шаг 4. Создание новой группы
Напишите функцию insert_into_groups(cursor, title, start_date, end_date),
которая добавляет группу и возвращает её id.
Вызовите функцию, указав название группы (например, 'Python-2025'),
дату начала и окончания (в формате 'YYYY-MM-DD'). Сохраните group_id.

Шаг 5. Обновление студента (привязка к группе)
Создайте функцию update_students_group(cursor, group_id, student_id),
которая обновляет поле group_id у студента с заданным id.
Вызовите её, чтобы привязать созданного студента к созданной группе.

Шаг 6. Добавление двух предметов
Реализуйте функцию insert_into_subjects(cursor, title), которая вставляет предмет и возвращает его id.
Добавьте два любых предмета (например, «Алгебра» и «Литература»). Сохраните их subject_id.

Шаг 7. Добавление уроков для каждого предмета
Напишите функцию insert_into_lessons(cursor, title, subject_id), вставляющую урок.
Для каждого предмета добавьте по два урока (например, «Введение» и «Основы»). Сохраните все lesson_id.

Шаг 8. Выставление оценок студенту
Создайте функцию insert_into_marks(cursor, value, lesson_id, student_id), которая добавляет оценку.
Поставьте студенту по одной оценке за каждый из
четырёх созданных уроков (значения оценок – на ваше усмотрение, от 1 до 5).

Шаг 9. Получение и вывод данных
После всех вставок выполните три запроса и выведите результаты в консоль:

Все оценки студента
SELECT value FROM marks WHERE student_id = <student_id>
Выведите список оценок.

Все книги, которые взял студент
SELECT title FROM books WHERE taken_by_student_id = <student_id>
Выведите список названий.

Полную информацию о студенте (одним запросом с JOIN)
Запрос должен вернуть:

все поля студента (students.*)

все поля его группы (groups.*)

все книги студента (books.title)

все оценки (marks.value)

названия уроков (lessons.title)

названия предметов (subjects.title)
Используйте JOIN для связывания таблиц.
Выведите полученные строки.
"""
import os

import dotenv
from mysql import connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user='st-onl',
    passwd=os.getenv('DB_PASSWD'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor_inst = db.cursor(dictionary=True)


def insert_into_students(cursor, name, second_name):
    insert_students_query = "INSERT INTO students (group_id ,name, second_name) VALUES (NULL, %s, %s)"
    cursor.execute(insert_students_query, (name, second_name))
    select_students_query = "SELECT id FROM students order by id DESC LIMIT 1"
    cursor.execute(select_students_query)
    student_id = cursor.fetchone().get('id')
    return student_id


books = ['Lord Of The Rings', 'Two Towers']
student_id = insert_into_students(cursor_inst, 'Andrei', 'Astapenka')
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor_inst.executemany(insert_books_query, [(books[0], student_id), (books[1], student_id)])
cursor_inst.execute('SELECT * FROM books order by id DESC LIMIT 2')
rows = cursor_inst.fetchall()


def insert_into_groups(cursor, title, start_date, end_date):
    insert_groups_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
    cursor.execute(insert_groups_query, (title, start_date, end_date))
    select_groups_query = "SELECT id FROM `groups` order by id DESC LIMIT 1"
    cursor.execute(select_groups_query)
    group_id = cursor.fetchone().get('id')
    return group_id


group_id = insert_into_groups(cursor_inst, 'Team C', '22.07.2001', '22.07.2002')
print(group_id)


def update_students_group(cursor, group_id, student_id):
    update_students_group_query = "UPDATE students SET group_id = %s WHERE `id` = %s"
    cursor.execute(update_students_group_query, (group_id, student_id))


update_students_group(cursor_inst, group_id, student_id)
select_students_query = "SELECT * FROM students order by id DESC LIMIT 1"
cursor_inst.execute(select_students_query)
print(cursor_inst.fetchone())
