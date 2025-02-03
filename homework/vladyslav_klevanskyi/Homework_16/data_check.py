import os
import dotenv
import mysql.connector as mysql

from csv_open import get_csv_data

dotenv.load_dotenv()

# Get data from csv file
csv_data = get_csv_data("data.csv")

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)

# Query
query = """
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
WHERE s.name = %s
AND s.second_name = %s
AND g.title = %s
AND b.title = %s
AND m.value = %s
AND sub.title = %s
AND l.title = %s
"""

# Create list for lost data
lost_data = []

# Get data from DB with parameters from SCV file
for row in csv_data:
    cursor.execute(
        query,
        (
            row["name"],
            row["second_name"],
            row["group_title"],
            row["book_title"],
            row["mark_value"],
            row["subject_title"],
            row["lesson_title"]
        )
    )
    retrieved_data = cursor.fetchone()
    if retrieved_data is None:
        lost_data.append(row)

db.close()

print(lost_data)
