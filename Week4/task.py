import datetime

class Task:

    def __init__(self, title: str, date_due: datetime.datetime):
        # create a new Task object with title and due date and sets creation date and completion status.
        self.title = title
        self.date_due = date_due
        self.date_created = datetime.datetime.now()
        self.completed = False

    def mark_completed(self) -> None:
        self.completed = True

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def __str__(self) -> str:
        # show the task output when run in readable format
        return f"Task: {self.title} | Due: {self.date_due.date()} | Completed: {self.completed}"
