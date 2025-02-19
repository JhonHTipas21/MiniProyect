import json

class Task:
    def __init__(self, title, description, due_date, priority, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        """Convierte la tarea en un diccionario para guardar en JSON"""
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """Filtra solo los argumentos esperados antes de instanciar Task"""
        allowed_keys = {"title", "description", "due_date", "priority", "status"}
        filtered_data = {k: v for k, v in data.items() if k in allowed_keys}
        return Task(**filtered_data)
