import json
import os
from models.task import Task

TASKS_FILE = "tasks.json"

class TaskController:
    def __init__(self):
        """Carga las tareas desde el archivo JSON al iniciar el controlador"""
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Carga las tareas desde el archivo JSON si existe"""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                try:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(t) for t in data]
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Guarda las tareas en el archivo JSON"""
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date, priority):
        """Agrega una nueva tarea a la lista y la guarda"""
        new_task = Task(title, description, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()

    def get_task(self, index):
        """Obtiene una tarea específica por su índice"""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def update_task(self, index, title, description, due_date, priority):
        """Actualiza una tarea existente con nuevos datos"""
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.title = title
            task.description = description
            task.due_date = due_date
            task.priority = priority
            self.save_tasks()

    def remove_task(self, index):
        """Elimina una tarea por índice"""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def list_tasks(self):
        """Devuelve la lista de tareas"""
        return self.tasks

    def complete_task(self, index):
        """Marca una tarea como completada"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            self.save_tasks()