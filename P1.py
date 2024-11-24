# Simple To-Do List Application

todo_list = []
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("Your To-Do List is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_no = int(input("Enter the task number to remove: "))
            removed_task = todo_list.pop(task_no - 1)
            print(f"Task '{removed_task}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number! Please try again.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
