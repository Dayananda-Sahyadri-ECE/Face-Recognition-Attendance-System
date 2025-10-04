import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
""")

# Update with your name
cursor.execute("DELETE FROM students")  # Optional: clears old entries
cursor.execute("INSERT INTO students (ID, Name) VALUES (?, ?)", (1, "Dayananda"))

conn.commit()
conn.close()
print("Database updated with Dayananda's profile!")
