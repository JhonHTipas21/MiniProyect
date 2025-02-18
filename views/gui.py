import tkinter as tk
from controllers.controller import TaskController
from models.task import Task

class TaskApp:
    def __init__(self, root):
        self.controller = TaskController()
        self.root = root
        self.root.title("Gestor de Tareas")
        
        self.label = tk.Label(root, text="Nueva tarea:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.add_button = tk.Button(root, text="Agregar", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        self.update_listbox()

    def add_task(self):
        title = self.entry.get()
        if title:
            task = Task(title)
            self.controller.add_task(task)
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.controller.list_tasks():
            self.listbox.insert(tk.END, f"{task.title} - {'Completada' if task.completed else 'Pendiente'}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
