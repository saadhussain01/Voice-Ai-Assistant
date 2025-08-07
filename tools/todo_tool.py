TODO_FILE = "memory/todo.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    return "Task added."

def view_tasks():
    try:
        with open(TODO_FILE, "r") as f:
            return f.read() or "No tasks found."
    except FileNotFoundError:
        return "No tasks found."
