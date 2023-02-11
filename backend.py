from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QFileDialog, QWidget, QLabel, QCheckBox, QLineEdit
from functions import readPDFContents


class Backend(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.file_name: str = "None selected"
        self.items_wgt_container: QWidget
        self.items: dict
        self.n_people: int = 4
        self.names: list[QLineEdit] = []

    def scan_receipt(self):
        raw_receipt = readPDFContents.getContents(self.file_name)
        self.items = readPDFContents.extractOrderedItems(raw_receipt)

    def fill_items_wgt_container(self):
        self.n_columns = self.n_people + 1  # +1 bcs of item name column
        self.n_rows = len(self.items) + 1  # +1 bcs of header
        if not self.items_wgt_container:
            raise NameError(
                "items_wgt_container was not given to the Backend object from GUI."
            )
        self._create_header()

    def _create_header(self):
        items_label = QLabel("Items")
        self.items_wgt_container.layout().addWidget(items_label, 0, 0)
        for i in range(self.n_people):
            self.names.append(QLineEdit())
            self.names[i].setText(f"Name {1}")
            self.items_wgt_container.layout().addWidget(self.names[i], 0, i + 1)
