import sqlite3

###
# This code is from
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#step-4-setting-up-the-database
# It is for setting up the database and populating it with test posts.
###

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
