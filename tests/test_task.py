import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Hacer compras", "Comprar frutas", "2025-02-15", "alta")
        self.assertEqual(task.title, "Hacer compras")
        self.assertEqual(task.priority, "alta")

if __name__ == "__main__":
    unittest.main()
