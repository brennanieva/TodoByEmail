
#!/usr/bin/env python3
import os
from datetime import date

# Define the directory and file path for the tasks
todo_dir = os.path.join(os.path.expanduser("~"), "scripts", "todos")
file_path = os.path.join(todo_dir, f"tasks_{date.today()}.txt")

# Make sure the directory exists
if not os.path.exists(todo_dir):
    os.makedirs(todo_dir)

def add_task(task):
    with open(file_path, "a") as file:
        file.write(f"[ ] {task}\n")

def mark_task_as_done(task):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if task in line:
                file.write(line.replace("[ ]", "[X]"))
            else:
                file.write(line)

def show_tasks():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = file.read()
            if tasks:
                print(tasks)
            else:
                print("No tasks for today!")
    else:
        print("No tasks for today!")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please specify a command: add, done, or show")
        exit()

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task(sys.argv[2])
    elif command == "done" and len(sys.argv) > 2:
        mark_task_as_done(sys.argv[2])
    elif command == "show":
        show_tasks()
    else:
        print(f"Unknown command: {command}")

