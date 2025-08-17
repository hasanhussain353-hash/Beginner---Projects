# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task(input("Enter a new task: "))
        elif choice == "3":
            remove_task(int(input("Enter task number to remove: ")))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
