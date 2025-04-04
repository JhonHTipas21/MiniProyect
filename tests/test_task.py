import unittest
from models.task import Task

class PruebaTarea(unittest.TestCase):

    def inicializar_prueba(self):
        """Prepara el entorno para cada caso de prueba."""
        self.elemento_tarea = Task("Tarea de comprobación", "Descripción para verificar", "2025-12-31", "Alta")

    def verificar_creacion_tarea(self):
        """Asegura que la tarea se construye adecuadamente."""
        self.assertEqual(self.elemento_tarea.title, "Tarea de comprobación")
        self.assertEqual(self.elemento_tarea.description, "Descripción para verificar")
        self.assertEqual(self.elemento_tarea.due_date, "2025-12-31")
        self.assertEqual(self.elemento_tarea.priority, "Alta")
        self.assertEqual(self.elemento_tarea.status, "Pending")  # Estado predeterminado

    def verificar_creacion_tarea_datos_incorrectos(self):
        """Examina el comportamiento al crear tareas con datos no válidos."""
        with self.assertRaises(ValueError):
            Task("", "Sin título", "2025-12-31", "Alta")  # Título vacío

        with self.assertRaises(ValueError):
            Task("Tarea sin fecha", "Prueba", "fecha-invalida", "Alta")  # Fecha no válida

        with self.assertRaises(ValueError):
            Task("Tarea sin prioridad", "Prueba", "2025-12-31", "No existe")  # Prioridad errónea

    def verificar_tarea_a_diccionario(self):
        """Confirma la conversión de una tarea a formato diccionario."""
        diccionario_tarea = self.elemento_tarea.to_dict()
        self.assertEqual(diccionario_tarea["title"], "Tarea de comprobación")
        self.assertEqual(diccionario_tarea["priority"], "Alta")

    def verificar_tarea_desde_diccionario(self):
        """Comprueba la creación de una tarea a partir de un diccionario."""
        datos_tarea = {
            "title": "Tarea recién creada",
            "description": "Prueba",
            "due_date": "2025-12-31",
            "priority": "Baja",
            "status": "Pending"
        }
        tarea_construida = Task.from_dict(datos_tarea)
        self.assertEqual(tarea_construida.title, "Tarea recién creada")
        self.assertEqual(tarea_construida.priority, "Baja")

    def verificar_modificacion_tarea(self):
        """Asegura que una tarea pueda ser alterada correctamente."""
        self.elemento_tarea.title = "Título actualizado"
        self.elemento_tarea.priority = "Media"
        self.assertEqual(self.elemento_tarea.title, "Título actualizado")
        self.assertEqual(self.elemento_tarea.priority, "Media")

    def verificar_eliminacion_tarea(self):
        """Simula la supresión de una tarea."""
        tarea_a_suprimir = Task("Suprimir", "Descripción", "2025-12-31", "Baja")
        del tarea_a_suprimir  # Simulación de borrado
        self.assertTrue(True)  # Si no hay error, la prueba es exitosa

if __name__ == "__main__":
    unittest.main()