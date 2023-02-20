from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QFormLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QSplitter,
)
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QFont
from backend import Backend


class Window(QMainWindow):
    def __init__(self, backend: Backend) -> None:
        super().__init__()
        self.backend: Backend = backend

        main_widget = QWidget()
        main_widget_layout = QVBoxLayout()
        main_widget.setLayout(main_widget_layout)
        self.setWindowTitle("Rohlik.cz utility app")

        self.setMinimumSize(1000, 500)
        # self.showMaximized()

        # Load Receipts bar
        load_receipts_bar = QWidget()
        load_receipts_bar.setStyleSheet("background-color: white")
        load_receipts_bar_layout = QHBoxLayout()
        load_receipts_bar.setLayout(load_receipts_bar_layout)

        self.path_to_file_lb = QLabel("File selected: " + self.backend.file_name)

        choose_file_btn = QPushButton("Choose file")
        choose_file_btn.setStyleSheet("background-color: none")
        choose_file_btn.setMaximumWidth(120)
        choose_file_btn.clicked.connect(self.choose_file)
        
        self.calculate_cost_btn = QPushButton("Calculate cost")
        self.calculate_cost_btn.setStyleSheet("background-color: none")
        self.calculate_cost_btn.setMaximumWidth(100)
        self.calculate_cost_btn.setEnabled(False)
        self.calculate_cost_btn.clicked.connect(self.backend.calculate_prices)

        load_receipts_bar_layout.addWidget(self.path_to_file_lb)
        load_receipts_bar_layout.addWidget(choose_file_btn)
        load_receipts_bar_layout.addWidget(self.calculate_cost_btn)

        load_receipts_bar.setFixedHeight(50)
        # =========================
        items_and_recap_wgt = QSplitter()
        items_and_recap_wgt.setLayout(QHBoxLayout())
        
        # Items list form
        items_list_wgt = QWidget()
        items_list_layout = QGridLayout()
        items_list_wgt.setLayout(items_list_layout)
        item_list_scroll = QScrollArea()
        item_list_scroll.setWidgetResizable(True)
        item_list_scroll.setWidget(items_list_wgt)
        items_and_recap_wgt.layout().addWidget(item_list_scroll)
        # =========================
        # Recap widget
        recap_widget = QWidget()
        recap_widget.setStyleSheet("background-color: white")
        recap_widget.setLayout(QVBoxLayout())

        to_pay_label = QLabel("To pay:")
        to_pay_label.setMaximumHeight(50)
        to_pay_label.setMinimumWidth(200)

        payment_info_label = QLabel()
        payment_info_label.setFont(QFont("Courier New", 12))

        recap_widget.layout().addWidget(to_pay_label)
        recap_widget.layout().addWidget(payment_info_label)
        recap_widget.layout().addStretch()
        items_and_recap_wgt.layout().addWidget(recap_widget)

        main_widget_layout.addWidget(load_receipts_bar)
        main_widget_layout.addWidget(items_and_recap_wgt)

        self.backend.items_wgt_container = items_list_wgt
        self.backend.payment_info_label = payment_info_label

        self.setCentralWidget(main_widget)

    @Slot()
    def choose_file(self):
        path = QFileDialog.getOpenFileName(
            self, "Open PDF", filter="Rohlik.cz receipt (*.pdf)"
        )
        if not path[0]:
            return
        self.backend.file_name = path[0]
        self.path_to_file_lb.setText("File selected: " + self.backend.file_name)
        self.backend.scan_receipt()
        self.backend.fill_items_wgt_container()

        if self.backend.is_items_wgt_filled:
            self.calculate_cost_btn.setEnabled(True)
