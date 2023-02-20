from PySide6.QtCore import QObject, Slot, Qt
from PySide6.QtWidgets import QFileDialog, QWidget, QLabel, QCheckBox, QLineEdit
from functions import readPDFContents
from customer import Customer


class Backend(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.file_name: str = "None selected"
        self.items_wgt_container: QWidget
        self.bought_items: dict
        self.n_customers: int = 4
        self.names: list[QLineEdit] = []
        self.customers: list[Customer] = []

    def scan_receipt(self):
        raw_receipt = readPDFContents.getContents(self.file_name)
        self.bought_items = readPDFContents.extractOrderedItems(raw_receipt)

    def fill_items_wgt_container(self):
        if not self.items_wgt_container:
            raise NameError(
                "items_wgt_container was not given to the Backend object from GUI."
            )

        self._create_header()
        self._fill_items()

        row_count = self.items_wgt_container.layout().rowCount()
        col_count = self.items_wgt_container.layout().columnCount()
        # Set columns and rows somewhat equally sized
        for i in range(row_count):
            self.items_wgt_container.layout().setRowStretch(i, 1)
        for i in range(col_count):
            self.items_wgt_container.layout().setColumnStretch(i, 1)

    def _create_header(self):
        """Create a header with names"""
        items_label = QLabel("Items")
        self.items_wgt_container.layout().addWidget(items_label, 0, 0)
        for i in range(self.n_customers):
            self.customers.append(Customer(f"Name {i}", self.bought_items))
            self.items_wgt_container.layout().addWidget(
                self.customers[i].name_le, 0, i + 1
            )

    def _fill_items(self):
        for i, item in enumerate(self.bought_items):
            customer_line_edits = [
                customer.bought_portions_le[i] for customer in self.customers
            ]
            self.items_wgt_container.layout().addWidget(QLabel(item), i + 1, 0)

            for j, line_edit in enumerate(customer_line_edits):
                self.items_wgt_container.layout().addWidget(
                    line_edit, i + 1, j + 1, Qt.AlignRight
                )
