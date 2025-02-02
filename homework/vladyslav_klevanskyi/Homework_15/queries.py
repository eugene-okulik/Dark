import mysql.connector as mysql

db = mysql.connect(
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    user="st-onl",
    password="AVNS_tegPDkI5BlB2lW5eASC",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

# 1.1 Create a student
name = "Zakk"
second_name = "Wylde"
group_id = None
insert_student_query = """
INSERT INTO students (name, second_name, group_id)
VALUES (%s, %s, %s)
"""
cursor.execute(insert_student_query, (name, second_name, group_id))
student_id = cursor.lastrowid
db.commit()
# Checking
cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")
print("Created student ->", cursor.fetchone())

# 1.2 Create two books and indicate that the created student took them
book_title1 = "Music for adults"
book_title2 = "Music for no one"
insert_book_query = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
cursor.execute(insert_book_query, (book_title1, student_id))
book1_id = cursor.lastrowid
cursor.execute(insert_book_query, (book_title2, student_id))
book2_id = cursor.lastrowid
db.commit()
# Checking
cursor.execute(f"SELECT b.title as book_title, s.name, s.second_name "
               f"FROM books b "
               f"JOIN students s ON b.taken_by_student_id = s.id "
               f"WHERE s.id = {student_id}"
               )
print("Created books ->", cursor.fetchall())

# 1.3 Create a group and assign our student to it.
group_title = "G7"
start_date = "Oct 2022"
end_date = "Sep 2023"
insert_group_query = """
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
"""
cursor.execute(insert_group_query, (group_title, start_date, end_date))
group_id = cursor.lastrowid

update_group_query = """UPDATE students SET group_id = %s WHERE id = %s"""
cursor.execute(update_group_query, (group_id, student_id))
db.commit()
# Checking
cursor.execute(f"SELECT s.name, s.second_name, g.title as group_title "
               f"FROM students s "
               f"JOIN `groups` g ON s.group_id = g.id "
               f"WHERE s.id = {student_id}"
               )
print("Created student with group ->", cursor.fetchall())

# 1.4 Create new subjects
subject_titles = ("Solfeggio", "Playing guitar", "Playing drums")
insert_subject_query = """INSERT INTO subjets (title) VALUES (%s)"""
subject_id_dict = {}
for title in subject_titles:
    cursor.execute(insert_subject_query, (title,))
    subject_id_dict[title] = cursor.lastrowid
db.commit()
# Checking
num = 0
for subject_title, subject_id in subject_id_dict.items():
    num += 1
    cursor.execute(f"SELECT * FROM subjets WHERE id = {subject_id}")
    print(f"Created subject {num} ->", cursor.fetchone())

# 1.5 Create two lessons for each subject
lessons_titles = {
    "Solfeggio": ("Solfeggio Basics", "Solfeggio in Details"),
    "Playing guitar": ("Guitar Basics", "Guitar in Details"),
    "Playing drums": ("Drums Basics", "Drums in Details")
}
insert_lesson_query = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
lesson_id_dict = {}
for subject_title, lessons_titles in lessons_titles.items():
    for lesson_title in lessons_titles:
        cursor.execute(
            insert_lesson_query,
            (lesson_title, subject_id_dict[subject_title])
        )
        lesson_id_dict[lesson_title] = cursor.lastrowid
db.commit()
# Checking
num = 0
for lesson_title, lesson_id in lesson_id_dict.items():
    num += 1
    cursor.execute(f"SELECT * FROM lessons WHERE id = {lesson_id}")
    print(f"Created lesson {num} ->", cursor.fetchone())

# 1.6 Put marks for the student for all created lessons
marks = ("A", "B", "C", "D", "F", "G")
insert_mark_query = """
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
"""
marks_id_dict = {}
index = 0
for lesson_title, lesson_id in lesson_id_dict.items():
    cursor.execute(insert_mark_query, (marks[index], lesson_id, student_id))
    index += 1
    marks_id_dict[lesson_id] = cursor.lastrowid
db.commit()
# Checking
num = 0
for lesson_id, mark_id in marks_id_dict.items():
    num += 1
    cursor.execute(f"SELECT * FROM marks WHERE id = {mark_id}")
    print(f"Created mark {num} ->", cursor.fetchone())

# 2.1 Receive all the student's grades
select_students_grades_query = """
SELECT value, name, second_name
FROM marks
JOIN students on marks.student_id = students.id
WHERE student_id = %s
"""
cursor.execute(select_students_grades_query, (student_id, ))
print("All student's grades ->", cursor.fetchall())

# 2.2 Receive all the student's books
select_students_books_query = """
SELECT title, name, second_name
FROM books
JOIN students on books.taken_by_student_id = students.id
WHERE taken_by_student_id = %s
"""
cursor.execute(select_students_books_query, (student_id,))
print("All student's books ->", cursor.fetchall())

# 2.3 Receive all information about the student
select_all_student_info_query = """
SELECT
 s.name,
 s.second_name,
 g.title as group_title,
 b.title as book_title,
 m.value as mark,
 sub.title as subject_title,
 l.title as lesson_title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = %s
"""
cursor.execute(select_all_student_info_query, (student_id,))
print("All information about the student ->", cursor.fetchall())

db.close()
