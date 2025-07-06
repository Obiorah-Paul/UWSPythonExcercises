from task import Task
import datetime

class TaskList:

    def __init__(self, owner: str):
        self.owner = owner.upper()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        if 0 <= ix < len(self.tasks):
            del self.tasks[ix]

    def view_tasks(self) -> None:
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your current tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")

    def view_overdue_tasks(self) -> None:
        now = datetime.datetime.now()
        print("Overdue Tasks:")
        for i, task in enumerate(self.tasks):
            if task.date_due < now:
                print(f"{i}. {task}")