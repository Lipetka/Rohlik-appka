from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QFormLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog


class Window(QMainWindow):
    def __init__(self, backend) -> None:
        super().__init__()
        self.backend = backend

        self.main_widget = QWidget()
        self.main_widget_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_widget_layout)
        self.setWindowTitle("Rohlik.cz utility app")

        self.setMinimumSize(800, 600)

        # Load Receipts bar
        self.load_receipts_bar = QWidget()
        self.load_receipts_bar.setStyleSheet("background-color: white")
        self.load_receipts_bar_layout = QHBoxLayout()
        self.load_receipts_bar.setLayout(self.load_receipts_bar_layout)

        self.path_to_file_lb = QLabel("File selected: " + self.backend.file_name)

        self.choose_file_btn = QPushButton("Choose file")
        self.choose_file_btn.setStyleSheet("background-color: none")
        self.choose_file_btn.setMaximumWidth(120)
        self.choose_file_btn.clicked.connect(self.choose_file)

        self.load_receipts_bar_layout.addWidget(self.path_to_file_lb)
        self.load_receipts_bar_layout.addWidget(self.choose_file_btn)

        self.load_receipts_bar.setFixedHeight(50)
        # =========================

        # Items list form
        self.items_list_wgt = QWidget()
        self.items_list_layout = QFormLayout()
        self.items_list_wgt.setLayout(self.items_list_layout)
        self.items_list_layout.addRow(QLabel("Items:"))
        # =========================

        self.main_widget_layout.addWidget(self.load_receipts_bar)
        self.main_widget_layout.addWidget(self.items_list_wgt)

        self.setCentralWidget(self.main_widget)

    @Slot()
    def choose_file(self):
        path = QFileDialog.getOpenFileName(
            self, "Open PDF", filter="Rohlik.cz receipt (*.pdf)"
        )
        if not path[0]:
            return
        self.backend.file_name = path[0]
        self.path_to_file_lb.setText("File selected: " + self.backend.file_name)
        