import sqlite3

class IdExc(Exception): # id value exception
    def __init__(self, head="TODOTaskIdError", message = "Invalid ID!"):
        super().__init__(message)
        self.head = head
        self.message = message

class NameExc(Exception): # task name exception
    def __init__(self, head="TODOTaskNameError", message = "Invalid name!"):
        super().__init__(message)
        self.head = head
        self.message = message

class PriorityExc(Exception): # priority value exception
    def __init__(self, head="TODOTaskPriorityError", message = "Invalid priority!"):
        super().__init__(message)
        self.head = head
        self.message = message


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self): # creating DB table
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self): # adding task
        # requesting user to enter a task name
        task_name = input('Enter task name: ')
        # checking if the task name is valid
        if len(task_name) == 0 or task_name.isspace():
            raise NameExc
        # checking if the task with this name already exists
        res = self.find_task(task_name)
        if res != None:
            raise NameExc(message="Task with this name already exists!")

        # requesting user to enter a priority value
        priority = int(input('Enter priority: '))
        # checking if the priority value is valid
        if priority < 1:
            raise PriorityExc

        # inserting data into a DB
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (task_name, priority))
        self.conn.commit()

    def delete_task(self): # deleting a task
        numid = int(input('Enter id which you want to delete: '))
        if numid < 1:
            raise IdExc

        self.c.execute('DELETE FROM tasks WHERE id = ?;', (numid,))
        self.conn.commit()

    def update_priority(self): # update priority of a task
        # requesting a priority value
        priority = int(input("Enter preferable priority: "))
        if priority < 1:
            raise PriorityExc

        # requesting a task id
        numid = int(input('Enter ID: '))
        if numid < 1:
            IdExc

        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, numid))
        self.conn.commit()

    def find_task(self, task_name): # finding task with a certain name; returns None if task is not found
        find = False

        for row in self.c.execute('SELECT id, name, priority FROM tasks;'):
            if row[1] == task_name:
                find = True
                return row

        if not find:
            return None

    def show_tasks(self): # printing tasks list to the console
        print("Task table contains the following tasks...")
        print("ID      | Task name   | Priority")
        for row in self.c.execute('SELECT * FROM tasks;'):
            print(row)

    def menu_controller(self, put = 0): # menu controller

        if put == 1: # show tasks
            self.show_tasks()

        elif put == 2 : # add task
            try:
                self.add_task()
            except NameExc as e:
                print(e.message)
            except PriorityExc as e:
                print(e.message)
            except:
                print("Something went wrong!")
            else:
                print("Task added successfully.")
            finally:
                print()

        elif put == 3: # update priority
            try:
                self.update_priority()
            except PriorityExc as e:
                print(e.message)
            except IdExc as e:
                print(e.message)
            except:
                print("Something went wrong!")
            else:
                print("Task updated successfully.")
            finally:
                print()

        elif put == 4: # delete task
            try:
                self.delete_task()
            except IdExc as e:
                print(e.message)
            except:
                print("Something went wrong!")
            else:
                print("The task has been deleted successfully.")
            finally:
                print()
        
        elif put == 5:
            print("Closing the program...")

        else:
            pass

    def run(self): # runs the program
        while True:
            print('''
1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit
''')
            try:
                put = int(input("Choose an option: "))
                if put == 5:
                    self.menu_controller(put)
                    break
            except:
                print("Invalid input!")
            else:
                if put in [1, 2, 3, 4]:
                    self.menu_controller(put)
