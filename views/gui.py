from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QComboBox
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from controllers.controller import TaskController
import sys

class TaskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = TaskController()
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz gráfica mejorada"""
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #FAFAFA; padding: 15px;")

        layout = QVBoxLayout()

        # Título
        self.title_label = QLabel("Gestor de Tareas", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #1565C0;")
        layout.addWidget(self.title_label)

        # Lista de tareas
        self.task_list = QListWidget()
        self.task_list.setStyleSheet("background-color: white; border: 1px solid #1565C0; border-radius: 8px; padding: 8px; font-size: 14px;")
        self.update_task_list()
        layout.addWidget(self.task_list)

        # Campos de entrada con estilos
        input_style = "padding: 10px; border: 1px solid #1565C0; border-radius: 5px; font-size: 14px; background-color: #E3F2FD;"

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Título de la tarea")
        self.title_input.setStyleSheet(input_style)
        layout.addWidget(self.title_input)

        self.desc_input = QLineEdit(self)
        self.desc_input.setPlaceholderText("Descripción")
        self.desc_input.setStyleSheet(input_style)
        layout.addWidget(self.desc_input)

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Fecha de vencimiento (YYYY-MM-DD)")
        self.date_input.setStyleSheet(input_style)
        layout.addWidget(self.date_input)

        self.priority_input = QComboBox(self)
        self.priority_input.addItems(["Alta", "Media", "Baja"])
        self.priority_input.setStyleSheet(input_style)
        layout.addWidget(self.priority_input)

        # Botones con estilo
        button_style = "border-radius: 5px; padding: 12px; font-size: 14px; font-weight: bold; color: white;"

        self.add_button = QPushButton("Agregar Tarea", self)
        self.add_button.setStyleSheet(button_style + "background-color: #2E7D32;")
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Modificar Tarea", self)
        self.edit_button.setStyleSheet(button_style + "background-color: #FF8F00;")
        self.edit_button.clicked.connect(self.edit_task)
        layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Eliminar Tarea Seleccionada", self)
        self.delete_button.setStyleSheet(button_style + "background-color: #C62828;")
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)

        # Nuevo botón para marcar como completada
        self.complete_button = QPushButton("Marcar como Completada", self)
        self.complete_button.setStyleSheet(button_style + "background-color: #1976D2;")
        self.complete_button.clicked.connect(self.complete_task)
        layout.addWidget(self.complete_button)

        self.setLayout(layout)

    def update_task_list(self):
        """Actualiza la lista de tareas en la interfaz"""
        self.task_list.clear()
        for task in self.controller.list_tasks():
            status = "✓" if task.is_completed() else task.status
            self.task_list.addItem(f"{task.title} - {task.priority} - {task.due_date} ({status})")

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

    def edit_task(self):
        """Carga la tarea seleccionada en los campos de entrada para su modificación"""
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            task = self.controller.get_task(selected_index)
            self.title_input.setText(task.title)
            self.desc_input.setText(task.description)
            self.date_input.setText(task.due_date)
            self.priority_input.setCurrentText(task.priority)
            
            self.add_button.setText("Guardar Cambios")
            self.add_button.clicked.disconnect()
            self.add_button.clicked.connect(lambda: self.update_task(selected_index))

    def update_task(self, index):
        """Actualiza la tarea en la lista con los nuevos valores"""
        title = self.title_input.text()
        description = self.desc_input.text()
        due_date = self.date_input.text()
        priority = self.priority_input.currentText()

        if title and due_date:
            self.controller.update_task(index, title, description, due_date, priority)
            self.update_task_list()
            self.title_input.clear()
            self.desc_input.clear()
            self.date_input.clear()
            self.add_button.setText("Agregar Tarea")
            self.add_button.clicked.disconnect()
            self.add_button.clicked.connect(self.add_task)

    def delete_task(self):
        """Elimina la tarea seleccionada en la interfaz gráfica"""
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            self.controller.remove_task(selected_index)
            self.update_task_list()

    def complete_task(self):
        """Marca la tarea seleccionada como completada"""
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            self.controller.complete_task(selected_index)
            self.update_task_list()

def run_app():
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    sys.exit(app.exec_())