import sqlite3

def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ho TEXT,
        ten TEXT,
        email TEXT,
        password TEXT,
        gender TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_user(ho, ten, email, password, gender):
    conn = sqlite3.connect("users.db")  
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (ho, ten, email, password, gender)
    VALUES (?, ?, ?, ?, ?)
    """, (ho, ten, email, password, gender))

    conn.commit()
    conn.close()