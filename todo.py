import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            display_tasks(load_tasks())
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
