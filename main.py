from tkinter import Tk
from views.gui import TaskApp

def main():
    root = Tk()
    app = TaskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
