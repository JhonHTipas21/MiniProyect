import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", "This is a test", "2025-12-31", "Alta")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "Pending")

    def test_task_to_dict(self):
        task = Task("Test Task", "Description", "2025-12-31", "Alta")
        task_dict = task.to_dict()
        self.assertEqual(task_dict["title"], "Test Task")

    def test_task_from_dict(self):
        data = {"title": "New Task", "description": "Testing", "due_date": "2025-12-31", "priority": "Baja"}
        task = Task.from_dict(data)
        self.assertEqual(task.title, "New Task")

if __name__ == "__main__":
    unittest.main()
