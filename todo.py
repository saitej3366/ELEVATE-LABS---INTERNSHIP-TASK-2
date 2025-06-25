# todo.py

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print()

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
