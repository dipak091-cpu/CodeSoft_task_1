# Simple TO-DO List Application

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list!")
    else:
        print("\n--- Your Tasks ---")
        for i, (task, status) in enumerate(tasks, start=1):
            status_text = "✓" if status else "✗"
            print(f"{i}. {task} [{status_text}]")

def add_task(tasks):
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append((task, False))
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task[0]}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"Task '{task}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            print("\nThank you for using the TO-DO List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
