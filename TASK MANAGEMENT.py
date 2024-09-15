import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    for task_id, task in tasks.items():
        print(f"ID: {task_id}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print("-" * 20)

def add_task(tasks):
    """Add a new task."""
    task_id = str(len(tasks) + 1)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status (e.g., Pending, Completed): ")

    tasks[task_id] = {
        'title': title,
        'description': description,
        'status': status
    }
    print("Task added successfully.")

def update_task(tasks):
    """Update an existing task."""
    task_id = input("Enter the ID of the task to update: ")
    if task_id in tasks:
        title = input("Enter new task title (leave blank to keep current): ")
        description = input("Enter new task description (leave blank to keep current): ")
        status = input("Enter new task status (leave blank to keep current): ")

        if title:
            tasks[task_id]['title'] = title
        if description:
            tasks[task_id]['description'] = description
        if status:
            tasks[task_id]['status'] = status

        print("Task updated successfully.")
    else:
        print("Task not found.")

def delete_task(tasks):
    """Delete a task."""
    task_id = input("Enter the ID of the task to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def main():
    """Main function to run the task management system."""
    tasks = load_tasks()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting. Tasks saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
