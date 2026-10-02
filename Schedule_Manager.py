import json
from datetime import datetime


FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ YOUR TASKS ------")

    for task in tasks:
        status = "✓ Done" if task["completed"] else "✗ Pending"

        print(
            f"""
                ID: {task['id']}
                Task: {task['name']}
                Priority: {task['priority']}
                Deadline: {task['deadline']}
                Status: {status}
                ------------------------
                """
             )


# Add a task
def add_task(tasks):
    name = input("Enter task name: ")

    priority = input("Priority (high/medium/low): ").lower()

    deadline = input("Deadline (YYYY-MM-DD): ")

    new_task = {
        "id": len(tasks) + 1,
        "name": name,
        "priority": priority,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully.")



# Edit task
def edit_task(tasks):

    show_tasks(tasks)

    try:
        task_id = int(input("Enter task ID to edit: "))

        for task in tasks:
            if task["id"] == task_id:

                task["name"] = input("New task name: ")

                task["priority"] = input("New priority: ")

                task["deadline"] = input("New deadline: ")

                save_tasks(tasks)

                print("Task updated.")
                return

        print("Task not found.")

    except ValueError:
        print("Invalid ID.")



# Remove task
def remove_task(tasks):

    show_tasks(tasks)

    try:
        task_id = int(input("Enter task ID to remove: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)

                # Reset IDs
                for i, t in enumerate(tasks):
                    t["id"] = i + 1

                save_tasks(tasks)

                print("Task removed.")
                return

        print("Task not found.")

    except ValueError:
        print("Invalid ID.")



# Mark completed
def complete_task(tasks):

    task_id = int(input("Enter task ID completed: "))

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task completed.")
            return

    print("Task not found.")



# Search tasks
def search_task(tasks):

    keyword = input("Search keyword: ").lower()

    results = [
        task for task in tasks
        if keyword in task["name"].lower()
    ]

    show_tasks(results)



# Sort tasks
def sort_tasks(tasks):

    print("""
1. Sort by priority
2. Sort by deadline
""")

    choice = input("Choose: ")

    if choice == "1":

        order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        tasks.sort(key=lambda x: order[x["priority"]])

    elif choice == "2":

        tasks.sort(key=lambda x: x["deadline"])

    show_tasks(tasks)



# Main program

tasks = load_tasks()


while True:

    print("""
========= SCHEDULE MANAGER =========

1. Add Task
2. Show Tasks
3. Edit Task
4. Remove Task
5. Complete Task
6. Search Task
7. Sort Tasks
8. Exit

================================
""")

    choice = input("Choose option: ")

    match choice:

        case "1":
            add_task(tasks)

        case "2":
            show_tasks(tasks)

        case "3":
            edit_task(tasks)

        case "4":
            remove_task(tasks)

        case "5":
            complete_task(tasks)

        case "6":
            search_task(tasks)

        case "7":
            sort_tasks(tasks)

        case "8":
            print("\nGoodbye!")
            break

        case _:
            print("Invalid option.")



print("\nToday's tasks:")

for task in tasks:
    if not task["completed"]:
        print("-", task["name"])