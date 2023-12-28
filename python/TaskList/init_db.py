import sqlite3

connection = sqlite3.connect('database.db')

# Open schema.sql file to create a connection with the db.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insert content into the db.
cur.execute("INSERT INTO tasks (title, content, status) VALUES (?, ?, ?)",
            ('First Task', 'Content for the first task', 'Status')
            )

cur.execute("INSERT INTO tasks (title, content, status) VALUES (?, ?, ?)",
            ('Second Tasks', 'Content for the second task', 'Status')
            )

# Commit the content.
connection.commit()

# Close the connection.
connection.close()
