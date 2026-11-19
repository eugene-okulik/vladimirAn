import csv
import mysql.connector as mysql
import os
import dotenv

# Подключение через .env
dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor(dictionary=True)

# Читка csv файла
with open("homework/eugene_okulik/Lesson_16/hw_data/data.csv", newline="") as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
quere = """ Select students.id from students
join `groups` on group_id = `groups`.id
join books on students.id = taken_by_student_id
join marks on students.id = student_id
join lessons on marks.lesson_id = lessons.id
join subjects on lessons.subject_id = subjects.id
WHERE students.name = %s
    AND students.second_name = %s
    AND `groups`.title = %s
    AND books.title = %s
    AND subjects.title = %s
    AND lessons.title = %s
    AND marks.value = %s
LIMIT 1 """

for peremennaia in data:
    cursor.execute(
        quere,
        (
            peremennaia["name"],
            peremennaia["second_name"],
            peremennaia["group_title"],
            peremennaia["book_title"],
            peremennaia["subject_title"],
            peremennaia["lesson_title"],
            peremennaia["mark_value"],
        ),
    )
    if not cursor.fetchall():
        print("Эти данные отсутствуют:", peremennaia)


db.close()
