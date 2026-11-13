import mysql.connector as mysql


db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl",
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    "insert into students (name, second_name, group_id) values (%s, %s, %s)",
    ("Vladimir", "Anikin", None),
)
student_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s), (%s, %s), (%s, %s)",
    ("lev", student_id, "volk", student_id, "ciaplia", student_id),
)
cursor.execute(
    "insert into `groups` (title, start_date, end_date) values ('Test', 'oct 2026', 'nov 2026')"
)
cursor.execute(
    "update students set group_id = (select id from `groups` where title = 'Test' Limit 1) where id = %s",
    (student_id,),
)
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ("raz",))
subject_1_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ("neskolko",))
subject_2_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s)",
    (
        "raz",
        subject_1_id,
        "dva",
        subject_1_id,
        "tri",
        subject_2_id,
        "chetiry",
        subject_2_id,
    ),
)
lesson_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s), (%s, %s, %s)",
    (
        1,
        lesson_id,
        student_id,
        2,
        lesson_id + 1,
        student_id,
        3,
        lesson_id + 2,
        student_id,
        4,
        lesson_id + 3,
        student_id,
    ),
)

cursor.execute("SELECT * from marks where student_id = %s", (student_id,))
print(cursor.fetchall())

cursor.execute("SELECT * from books where taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())

cursor.execute(
    "Select * from students "
    "join `groups` on group_id = `groups`.id "
    "join books on students.id = taken_by_student_id "
    "join marks on students.id = student_id "
    "join lessons on marks.lesson_id = lessons.id "
    "join subjects on lessons.subject_id = subjects.id "
    "where students.id = %s",
    (student_id,),
)

print(cursor.fetchall())

db.commit()

db.close()
