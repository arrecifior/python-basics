import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

# create list with tuples of data
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]

#insert data
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
#fix changes
conn.commit()
#close connection
conn.close