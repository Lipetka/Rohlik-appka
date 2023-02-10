from PySide6.QtWidgets import QApplication
from gui import Window
from backend import Backend

if __name__ == "__main__":
    app = QApplication()

    backend = Backend()
    main_window = Window(backend)
    main_window.show()

    app.exec()
