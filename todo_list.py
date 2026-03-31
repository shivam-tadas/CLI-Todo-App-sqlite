import json

class TodoList:
    todos: list[str]

    def __init__(self):
        self.todos = []

    def add_todo(self, todo: str) -> None:
        self.todos.append(todo)

    def mark_todo_as_done(self, todo_no: int) -> None:
        del self.todos[todo_no - 1]

    def show_todos(self) -> None:
        print("To-do list")
        print("---")
        for i, todo in enumerate(self.todos):
            print(i+1, ": ", todo, sep='')
        print("---")

print("Welcome to CLI To-dos list")
todo_list = TodoList()

try:
    with open("todos.json", "r") as fp:
        todo_list.todos = json.load(fp)
except (FileNotFoundError, json.JSONDecodeError):
    todo_list.todos = []

while True:
    print("\n1. Show todos")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Exit")
    print("Make a choice:", end=' ')
    choice = int(input())
    if choice == 1:
        todo_list.show_todos()
    elif choice == 2:
        print("Enter task to be added:", end=' ')
        todo_task = input()
        todo_list.add_todo(todo_task)
        print(f"Task {todo_task} added")
        with open("todos.json", "w") as fp:
            json.dump(todo_list.todos, fp)
    elif choice == 3:
        print("Enter task number to be marked as done:", end=' ')
        task_no = int(input())
        if task_no > len(todo_list.todos):
            print("Enter a valid task number")
        else:
            todo_list.mark_todo_as_done(task_no)
            print(f"Task {task_no} marked as done")
        with open("todos.json", "w") as fp:
            json.dump(todo_list.todos, fp)
    elif choice == 4:
        break
    else:
        print("Please input a valid choice")