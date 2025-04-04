# Documentación de la Arquitectura del Proyecto

## 1. Visión General del Proyecto
Este proyecto es un gestor de tareas diseñado para ayudar a los usuarios a organizar sus actividades de manera eficiente. Su arquitectura modular permite una fácil escalabilidad y mantenimiento.

## 2. Propósito del Proyecto
El propósito de este proyecto es proporcionar una herramienta sencilla pero poderosa para la gestión de tareas, facilitando la organización del tiempo y aumentando la productividad de los usuarios.

## 3. Descripción de la Arquitectura
El proyecto sigue una arquitectura modular para garantizar la mantenibilidad y escalabilidad del código. Se divide en los siguientes módulos:

- **Interfaz gráfica (GUI)**: Maneja la interacción con el usuario.
- **Gestor de Tareas**: Administra la creación, edición y eliminación de tareas.
- **Base de Datos**: Permite el almacenamiento y recuperación de datos de tareas.
- **Módulo de Configuración**: Contiene ajustes personalizables por el usuario.

Estos módulos interactúan entre sí de manera estructurada para garantizar una ejecución eficiente y clara.

## 4. Patrones de Diseño Utilizados
Se han aplicado principios de POO y el principio de modularidad, asegurando que cada componente tenga una responsabilidad bien definida. Además, el proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)** de manera implícita:

- **Modelo** (*base_datos.py*, *gestor_tareas.py*): Se encarga de la lógica y almacenamiento de datos.
- **Vista** (*gui.py*): Muestra la información al usuario y captura sus acciones.
- **Controlador** (*main.py*): Conecta la vista con la lógica del proyecto.

## 5. Estructura del Código y Explicaciones
La estructura del código está organizada en las siguientes carpetas y archivos clave:

```
MiniProyect/
├── Docs/                       # Documentación del proyecto
├── Guia_Usuario_Instalacion/   # Guía de usuario e intalación y ejecución del proyecto
├── main.py                     # Punto de entrada principal del programa
├── controllers/                # Lógica de negocio y controladores
├── task_controller.py          # Controlador para la gestión de tareas
├── models/                     # Modelos de datos
│   ├── task.py                 # Definición de la clase Task
├── views/                      # Interfaz de usuario
│   ├── cli.py                  # Interfaz de línea de comandos (CLI)
├── tests/                      # Pruebas unitarias
│   ├── test_task.py            # Pruebas para la clase Task
├── ARQUITECTURA.md             # Descripción de la arquitectura del proyecto
├── README.md                   # Descripción general del proyecto
├── README_RULES.md             # Reglas primordiales para la generacion de codigo estetico y modular
```

- **main.py**: Es el punto de entrada del programa, donde se inicia la ejecución del sistema.
- **Carpeta controllers/**: Contiene la lógica de negocio y se encarga de gestionar las operaciones de las tareas.
- **Carpeta models/**: Define la estructura de datos utilizada en el sistema.
- **Carpeta views/**: Maneja la interacción con el usuario a través de la CLI.
- **Carpeta tests/**: Contiene pruebas unitarias para garantizar el correcto funcionamiento del sistema.

## 6. Relaciones entre Módulos y Clases
- **main.py** interactúa con **task_controller.py** para procesar las acciones del usuario.
- **task_controller.py** utiliza **task.py** para gestionar la información de las tareas.
- **cli.py** permite al usuario interactuar con el sistema a través de la línea de comandos.
- Las pruebas unitarias en **tests/** verifican que los modelos y controladores funcionen correctamente.

## 7. Flujo de Datos y Procesos Clave
1. El usuario inicia la aplicación ejecutando **main.py**.
2. El usuario interactúa con la interfaz gráfica para agregar o modificar tareas.
3. **main.py** procesa la entrada y la delega a **task_controller.py**.
4. **task_controller.py** interactúa con **task.py** para modificar o recuperar datos.
5. Los resultados se envían a **cli.py**, proporcionando feedback al usuario.

## 8. Tecnologías y Librerías Utilizadas
- **Python 3.x**: Lenguaje de programación principal.
- **argparse**: Para la gestión de argumentos en la CLI.
- **unittest**: Para realizar pruebas unitarias.
- **PyQt5**: Para la interfaz gráfica.
- **SQLite**: Base de datos ligera y eficiente.

