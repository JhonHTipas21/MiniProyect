# **Principios de Programación Orientada a Objetos (POO) en el Proyecto**

## **Encapsulación**
Cada clase en el proyecto tiene atributos y métodos bien definidos, asegurando que los datos estén protegidos y solo sean accesibles a través de métodos específicos. Esto evita la modificación directa de atributos desde otras partes del código.

Ejemplo:
```python
class Task:
    def __init__(self, title, description, due_date, priority, status="Pendiente"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
```

## **Abstracción**
El código está diseñado para ocultar la implementación interna de las clases y exponer solo lo necesario. Por ejemplo:
- `Task` encapsula los datos de una tarea.
- `TaskController` gestiona la lógica de negocio.
- `TaskApp` maneja la interfaz gráfica sin modificar directamente las tareas.

## **Herencia**
- `TaskApp` hereda de `QWidget` (de PyQt5), lo cual permite el uso de funcionalidades avanzadas de interfaces gráficas.
- No se requieren más herencias, ya que cada clase tiene su responsabilidad específica sin redundancias.

Ejemplo:
```python
from PyQt5.QtWidgets import QWidget

class TaskApp(QWidget):
    def __init__(self):
        super().__init__()
        # Configuración de la interfaz gráfica
```

## **Polimorfismo**
Aunque no se usa sobrecarga de métodos, la estructura permite que los métodos sean reutilizables en distintos contextos, facilitando la extensibilidad del código.

Ejemplo:
```python
def save_tasks(self):
    """Guarda la lista de tareas en un archivo JSON."""
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in self.tasks], file)
```

## **Conclusión**
El diseño del proyecto respeta los principios fundamentales de POO, asegurando modularidad, reutilización y escalabilidad. Esto permite futuras mejoras sin afectar la estructura existente.

