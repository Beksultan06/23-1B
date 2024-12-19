import sqlite3

conn = sqlite3.connect("23-1B.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    )
""")

cursor.execute("""
INSERT INTO users(name, age, email)
VALUES (?, ?, ?)
""",
('Mardon', 20, 'mardon@gmail.com'))

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()