# GUÍA DE INSTALACIÓN Y EJECUCIÓN 

## 📋 Requisitos Previos

Antes de instalar este gestor de tareas, asegúrate de tener lo siguiente:

- Python 3.10 o superior instalado.
- pip (el gestor de paquetes de Python).
- Git (opcional, si deseas clonar el repositorio desde GitHub).

## ✅ Librerías necesarias

Estas son las librerías requeridas por el proyecto:

- `PyQt5` (Para la interfaz gráfica basada en Qt)
- `argparse` (incluida por defecto)
- `unittest` (incluida por defecto)
- `sqlite3` (incluida por defecto)

> ✅ PyQt5 sera la unica librería externa que tendras que instalar manuelmente.

### ✅ Instalar PyQt5

Abre tu terminal y ejecuta:

```bash
pip install PyQt5
```

## ✅ Clonar el repositorio

Abre tu terminal y ejecuta el siguiente comando:

```bash
git clone https://github.com/JhonHTipas21/MiniProyect.git
```

## ✅ Estructura del Proyecto

```plaintext
MiniProyect/
├── Docs/
├── Guia_Usuario_Instalacion/
├── controllers/
├── models/
├── views/
├── tests/
├── ARQUITECTURA.md
├── main.py
├── README_RULES.md
├── README.md
```

## ▶️ Ejecutar el programa

Desde la terminal, navega a la carpeta raíz del proyecto y ejecuta:

```bash
python main.py
```

Esto iniciará la aplicación y podrás comenzar a interactuar con ella.

## ▶️ Ejecutar pruebas

Para correr las pruebas unitarias:

```bash
cd tests
python -m unittest test_task.py
```

---

> 📌 Si tienes algún problema ejecutando el programa, revisa que estés en la carpeta correcta y tengas Python correctamente instalado.
