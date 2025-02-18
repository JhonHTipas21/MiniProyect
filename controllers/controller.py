import json
import os
from models.task import Task

FILE_PATH = "tasks.json"

class TaskController:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                return [Task.from_dict(task) for task in json.load(file)]
        return []

    def save_tasks(self):
        with open(FILE_PATH, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()
