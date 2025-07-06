# initialize an empty list to store tasks
tasks = []

# create function to add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

# create function to view current tasks in the list
def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# create function to remove a task from the list
def remove_task():
    task_to_remove = input("Enter the exact task to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"'{task_to_remove}' has been removed.")
    else:
        print(f"'{task_to_remove}' was not found in your to-do list.")

# main program loop to display the menu
while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1–4): ")

    # use conditionals to execute the appropriate function
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")