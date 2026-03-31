import sqlite3

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number:", end=' ')

class TodoList:
    def __init__(self):
        self.conn = sqlite3.connect("todos.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
        
    def add_todo(self, todo: str) -> None:
        self.cursor.execute("INSERT INTO todos (task) VALUES (?)", (todo,))
        self.conn.commit()

    def mark_todo_as_done(self, task_id: int) -> None:
        self.cursor.execute("SELECT id FROM todos WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if row is None:
            print("Task not found")
        else:
            self.cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
            self.conn.commit()

    def show_todos(self) -> None:
        print("To-do list")
        self.cursor.execute("SELECT * FROM todos")
        rows = self.cursor.fetchall()
        for id, task in rows:
            print(f"{id}: {task}")

print("Welcome to CLI To-dos list")
todo_list = TodoList()

while True:
    print("\n1. Show todos")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Exit")
    
    choice = get_int_input("Make a choice: ")
    
    if choice == 1:
        todo_list.show_todos()
    elif choice == 2:
        print("Enter task to be added:", end=' ')
        todo_task = input()
        todo_list.add_todo(todo_task)
    elif choice == 3:
        task_id = get_int_input("Enter id of task to be marked as done: ")
        todo_list.mark_todo_as_done(task_id)
    elif choice == 4:
        todo_list.conn.close()
        break
    else:
        print("Please input a valid choice")