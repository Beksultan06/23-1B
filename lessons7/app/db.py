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
            lesson TEXT NOT NULL
            task TEXT NOT NULL
            deadline TEXT NOT NULL
        )
''')

conn.commit()
conn.close()

