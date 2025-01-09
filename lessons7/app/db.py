import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            age INTEGER NOT NULL,
            lesson TEXT NOT NULL,
            task TEXT NOT NULL,
            deadline TEXT NOT NULL
        )
''')

conn.commit()
conn.close()

def save_to_db(student_data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO students (chat_id, name, phone, age, lesson, task, deadline)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''',(
    student_data['chat_id'],
    student_data['name'],
    student_data['age'],
    student_data['phone'],
    student_data['lesson'],
    student_data['task'],
    student_data['deadline'].strftime('%d.%m.%Y %H:%M'),
))
    conn.commit()
    conn.close()