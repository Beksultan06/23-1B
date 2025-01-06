import sqlite3

DATABASE_PATH = "register.db"

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_number INTEGER NOT NULL,
            email TEXT NOT NULL
        )""")
    conn.commit()
    conn.close()