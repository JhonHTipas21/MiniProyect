from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QComboBox
from controllers.controller import TaskController
import sys

class TaskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = TaskController()
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz gráfica"""
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Lista de tareas
        self.task_list = QListWidget()
        self.update_task_list()
        layout.addWidget(self.task_list)

        # Campos de entrada
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Título de la tarea")
        layout.addWidget(self.title_input)

        self.desc_input = QLineEdit(self)
        self.desc_input.setPlaceholderText("Descripción")
        layout.addWidget(self.desc_input)

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Fecha de vencimiento (YYYY-MM-DD)")
        layout.addWidget(self.date_input)

        self.priority_input = QComboBox(self)
        self.priority_input.addItems(["Alta", "Media", "Baja"])
        layout.addWidget(self.priority_input)

        # Botones
        self.add_button = QPushButton("Agregar Tarea", self)
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Eliminar Tarea Seleccionada", self)
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def update_task_list(self):
        """Actualiza la lista de tareas en la interfaz"""
        self.task_list.clear()
        for task in self.controller.list_tasks():
            self.task_list.addItem(f"{task.title} - {task.priority} - {task.due_date} ({task.status})")

    def add_task(self):
        """Añade una tarea desde la interfaz gráfica"""
        title = self.title_input.text()
        description = self.desc_input.text()
        due_date = self.date_input.text()
        priority = self.priority_input.currentText()

        if title and due_date:
            self.controller.add_task(title, description, due_date, priority)
            self.update_task_list()
            self.title_input.clear()
            self.desc_input.clear()
            self.date_input.clear()

    def delete_task(self):
        """Elimina la tarea seleccionada en la interfaz gráfica"""
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            self.controller.remove_task(selected_index)
            self.update_task_list()

def run_app():
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    sys.exit(app.exec_())
