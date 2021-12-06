import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)

c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()

c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)

c.execute('DELETE FROM tasks WHERE id = ?', (1,))
conn.commit()

c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()