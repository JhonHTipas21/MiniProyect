import json
from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority="media", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else datetime.now().strftime("%Y-%m-%d")
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)
