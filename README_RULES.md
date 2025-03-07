# 📌 **Convenciones de Código para el Proyecto**  

Este documento establece las reglas y buenas prácticas que deben seguirse en el desarrollo del código para garantizar la claridad, mantenibilidad y calidad del software.  

---

## 📂 **1. Organización del Proyecto**  

El código estará organizado en una estructura de carpetas que refleje la separación de responsabilidades:  

```
MiniProyect/
│── controllers/   # Lógica de negocio y manipulación de datos
│   ├── controller.py
│
│── models/        # Definición de las estructuras de datos
│   ├── task.py
│
│── views/         # Interfaz gráfica del usuario (GUI)
│   ├── gui.py
│
│── tests/         # Pruebas automatizadas del sistema
│   ├── test_task.py # Archivo que contiene pruebas unitarias para verificar el correcto funcionamiento del modelo `Task`.
│
│── main.py        # Punto de entrada del programa
│── README.md      # Documentación principal del proyecto
│── requirements.txt # Dependencias del proyecto
```

### 📌 **Explicación de cada carpeta**
- **`controllers/`**: Contiene la lógica de negocio y la gestión de datos.
- **`models/`**: Define las estructuras de datos y modelos del proyecto.
- **`views/`**: Maneja la interfaz gráfica del usuario.
- **`tests/`**: Almacena las pruebas automatizadas para validar la funcionalidad del código.

Cada archivo debe contener **una única responsabilidad**. Por ejemplo, `controller.py` debe manejar la lógica del negocio, y `gui.py` solo la interfaz gráfica.

---

## 📌 **2. Convenciones de Nomenclatura**  

Es fundamental seguir un esquema de nombres coherente para mejorar la legibilidad y mantenimiento del código.  

### ✅ **Reglas generales de nombres:**  
| Elemento                   | Reglas para nombrar elementos  | Ejemplos en el Proyecto|
|----------------------------|--------------------------------|------------------------|
| **Clases**                 | `CamelCase`                    | `TaskController`       |
| **Variables**              | `snake_case`                   | `task_list`, `due_date`|
| **Funciones**              | `snake_case`                   | `get_task_list()`      |
| **Métodos**                | `snake_case`                   | `add_task()`           |
| **Constantes**             | `MAYÚSCULAS_CON_GUIONES_BAJOS` | `MAX_TASKS = 100`      |
| **Módulos (archivos .py)** | `snake_case.py`                | `task_manager.py`      |

---

## 📝 **3. Formato y Estilo del Código**  

Todo el código debe seguir las **reglas de PEP 8** para garantizar un formato estándar.  

### 🔹 **Identación**  
- Se deben usar **4 espacios** por nivel de indentación.  
- **No usar tabulaciones (`\t`)**, solo espacios.  

```python
def example_function():
    if True:
        print("Ejemplo con indentación correcta")
```

### 🔹 **Longitud de línea**  
- No superar los **79 caracteres** por línea.  
- Si es necesario, dividir líneas largas con `\` o usando paréntesis.  

```python
query = ("SELECT id, name, email FROM users "
         "WHERE active = 1")
```

### 🔹 **Espaciado**  
- Incluir **un espacio** antes y después de los operadores (`=`, `+`, `-`, etc.).  
- No usar espacios antes de `:` en funciones o estructuras de control.  

```python
x = 5  # ✅ Correcto
y=10   # ❌ Incorrecto
```

### 🔹 **Importaciones**  
- Siempre organizar los imports en este orden:  
  1. **Módulos estándar de Python**  
  2. **Librerías de terceros (PyQt5, etc.)**  
  3. **Módulos internos del proyecto**  

```python
import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget

from controllers.controller import TaskController
from models.task import Task
```

---

## 🔧 **4. Buenas Prácticas de Programación**  

### ✅ **Modularidad y reutilización de código**  
- Cada función/método debe **tener una única responsabilidad** (Principio **SRP**).  
- No duplicar código innecesariamente, sino usar funciones reutilizables.  

```python
def format_date(date):
    """Convierte una fecha en formato YYYY-MM-DD a DD/MM/YYYY."""
    return date.strftime("%d/%m/%Y")
```

### ✅ **Uso de Docstrings**  
- Toda función, clase y módulo debe llevar una descripción clara de su propósito.  

```python
def add_task(title: str, description: str, due_date: str, priority: str):
    """
    Agrega una nueva tarea a la lista.

    :param title: Título de la tarea.
    :param description: Descripción de la tarea.
    :param due_date: Fecha límite (YYYY-MM-DD).
    :param priority: Prioridad ('Alta', 'Media', 'Baja').
    """
```

### ✅ **Uso de f-strings para cadenas**  
- En lugar de `+` para concatenar, usar **f-strings** por ser más eficientes y legibles.  

```python
task_info = f"Tarea: {task.title} | Fecha: {task.due_date} | Prioridad: {task.priority}"
```

### ✅ **Manejo de errores**  
- Siempre capturar excepciones para evitar que el programa se detenga de forma inesperada.  

```python
try:
    result = int(input("Ingrese un número: "))
except ValueError:
    print("Error: Debe ingresar un número válido.")
```

---

## 🛠 **5. Uso de Git y Control de Versiones**  

- Cada cambio importante debe ir en un **commit bien documentado**.  
- Mensajes de commit claros y en presente:  
  - ✅ `"Agrega función para eliminar tareas"`  
  - ❌ `"Añadí función de eliminar"`  
- Usar ramas (`branches`) para el desarrollo de nuevas funcionalidades antes de fusionarlas con `main`.

---

## 📌 **Conclusión**  

Este conjunto de reglas garantizará que el código del proyecto sea **ordenado, legible y mantenible**, facilitando la colaboración entre desarrolladores.  
