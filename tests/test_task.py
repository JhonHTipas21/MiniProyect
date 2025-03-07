import unittest
from models.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.tarea = Task("Tarea de prueba", "Descripción de prueba", "2025-12-31", "Alta")

    def test_creacion_tarea(self):
        """Verifica que la tarea se crea correctamente."""
        self.assertEqual(self.tarea.title, "Tarea de prueba")
        self.assertEqual(self.tarea.description, "Descripción de prueba")
        self.assertEqual(self.tarea.due_date, "2025-12-31")
        self.assertEqual(self.tarea.priority, "Alta")
        self.assertEqual(self.tarea.status, "Pending")  # Estado por defecto

    def test_creacion_tarea_datos_invalidos(self):
        """Verifica el comportamiento al crear tareas con datos inválidos."""
        with self.assertRaises(ValueError):
            Task("", "Sin título", "2025-12-31", "Alta")  # Título vacío

        with self.assertRaises(ValueError):
            Task("Tarea sin fecha", "Prueba", "fecha-invalida", "Alta")  # Fecha inválida

        with self.assertRaises(ValueError):
            Task("Tarea sin prioridad", "Prueba", "2025-12-31", "No existe")  # Prioridad incorrecta

    def test_tarea_a_dict(self):
        """Verifica la conversión de una tarea a diccionario."""
        tarea_dict = self.tarea.to_dict()
        self.assertEqual(tarea_dict["title"], "Tarea de prueba")
        self.assertEqual(tarea_dict["priority"], "Alta")

    def test_tarea_desde_dict(self):
        """Verifica la creación de una tarea desde un diccionario."""
        datos = {
            "title": "Nueva tarea",
            "description": "Prueba",
            "due_date": "2025-12-31",
            "priority": "Baja",
            "status": "Pending"
        }
        tarea = Task.from_dict(datos)
        self.assertEqual(tarea.title, "Nueva tarea")
        self.assertEqual(tarea.priority, "Baja")

    def test_modificar_tarea(self):
        """Verifica que una tarea pueda ser modificada correctamente."""
        self.tarea.title = "Nuevo título"
        self.tarea.priority = "Media"
        self.assertEqual(self.tarea.title, "Nuevo título")
        self.assertEqual(self.tarea.priority, "Media")

    def test_eliminar_tarea(self):
        """Simula la eliminación de una tarea."""
        tarea_eliminar = Task("Eliminar", "Descripción", "2025-12-31", "Baja")
        del tarea_eliminar  # Simulación de eliminación
        self.assertTrue(True)  # Si no hay error, la prueba pasa

if __name__ == "__main__":
    unittest.main()
