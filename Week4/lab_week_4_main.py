# Week 4 Practical Lab – To-Do List
from tasklist import TaskList
from task import Task
import datetime


def main() -> None:
    task_list = TaskList("User")

    while True:
        print("To-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. View overdue tasks")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            task = Task(title, date_object)
            task_list.add_task(task)
            print(f"'{title}' has been added to your to-do list.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            task_list.view_tasks()
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
            print(f"Task {ix} has been removed.")

        elif choice == "4":
            task_list.view_tasks()
            ix = int(input("Enter the index of the task to edit: "))
            if 0 <= ix < len(task_list.tasks):
                task = task_list.tasks[ix]
                print("1. Change title")
                print("2. Change due date")
                print("3. Mark completed")
                sub_choice = input("Enter your choice: ")
                if sub_choice == "1":
                    new_title = input("Enter new title: ")
                    task.change_title(new_title)
                elif sub_choice == "2":
                    new_date = input("Enter new due date (YYYY-MM-DD): ")
                    task.change_date_due(datetime.datetime.strptime(new_date, "%Y-%m-%d"))
                elif sub_choice == "3":
                    task.mark_completed()
                else:
                    print("Invalid choice.")
            else:
                print("Invalid task index.")

        elif choice == "5":
            task_list.view_overdue_tasks()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1–6.")

if __name__ == "__main__":
    main()
