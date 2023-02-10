from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QFileDialog
from functions import readPDFContents


class Backend(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.file_name = "None selected"



