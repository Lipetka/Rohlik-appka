from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLineEdit,
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

CUSTOMER_N_DEFAULT_VALUE = 4


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

        upper_bar, customer_n_le = self.create_upper_bar()

        # =========================
        (
            items_and_recap_wgt,
            items_list_wgt,
            payment_info_label,
        ) = self.create_items_and_recap_wgt()

        main_widget_layout.addWidget(upper_bar)
        main_widget_layout.addWidget(items_and_recap_wgt)

        self.backend.items_wgt_container = items_list_wgt
        self.backend.payment_info_label = payment_info_label
        self.backend.customers_n_le = customer_n_le

        # Set default value
        customer_n_le.setText(str(CUSTOMER_N_DEFAULT_VALUE))

        self.setCentralWidget(main_widget)

    #
    #**************************CREATE WIDGETS METHODS***************************
    #
    def create_items_and_recap_wgt(self):
        items_and_recap_wgt = QSplitter()
        items_and_recap_wgt.setLayout(QHBoxLayout())

        # Items list form
        items_list_wgt, item_list_scroll = self.create_items_list_wgt()
        # =========================
        # Recap widget
        recap_widget, payment_info_label = self.create_recap_wgt()

        items_and_recap_wgt.layout().addWidget(item_list_scroll)
        items_and_recap_wgt.layout().addWidget(recap_widget)

        return items_and_recap_wgt, items_list_wgt, payment_info_label

    def create_recap_wgt(self):
        recap_widget = QWidget()
        recap_widget.setStyleSheet("background-color: white")
        recap_widget.setLayout(QVBoxLayout())
        recap_widget.setMinimumWidth(300)

        payment_info_label = QLabel()
        payment_info_label.setFont(QFont("Courier New", 12))

        recap_widget.layout().addWidget(QLabel("To pay:"))
        recap_widget.layout().addWidget(payment_info_label)
        recap_widget.layout().addStretch()

        return recap_widget, payment_info_label

    def create_items_list_wgt(self):
        items_list_wgt = QWidget()
        items_list_wgt.setLayout(QGridLayout())
        item_list_scroll = QScrollArea()
        item_list_scroll.setWidgetResizable(True)
        item_list_scroll.setWidget(items_list_wgt)
        return items_list_wgt, item_list_scroll

    def create_upper_bar(self):
        upper_bar = QWidget()
        upper_bar.setLayout(QVBoxLayout())
        # Load Receipts bar
        load_receipts_bar = self.create_load_receipts_bar()

        # Additional settings bar
        additional_settings, customer_n_le = self.create_additional_settings_bar()

        upper_bar.layout().addWidget(load_receipts_bar)
        upper_bar.layout().addWidget(additional_settings)

        return upper_bar, customer_n_le

    def create_additional_settings_bar(self):
        additional_settings = QWidget()
        additional_settings.setLayout(QHBoxLayout())

        customer_n_le = QLineEdit()
        customer_n_le.setMaximumWidth(80)
        customer_n_le.textChanged.connect(self.backend.set_n_customers)

        self.calculate_cost_btn = self.create_transparent_btn(
            "Calculate cost", self.backend.calculate_prices
        )
        self.calculate_cost_btn.setEnabled(False)

        additional_settings.layout().addStretch()
        additional_settings.layout().addWidget(QLabel("How many people? :"))
        additional_settings.layout().addWidget(customer_n_le)
        additional_settings.layout().addWidget(self.calculate_cost_btn)

        return additional_settings, customer_n_le

    def create_load_receipts_bar(
        self,
    ):
        load_receipts_bar = QWidget()
        load_receipts_bar.setStyleSheet("background-color: white")
        load_receipts_bar_layout = QHBoxLayout()
        load_receipts_bar.setLayout(load_receipts_bar_layout)

        self.path_to_file_lb = QLabel("File selected: " + self.backend.file_name)

        choose_file_btn = self.create_transparent_btn("Choose file", self.choose_file)
        self.load_receipt_btn = self.create_transparent_btn(
            "Load receipt", self.load_receipt
        )
        self.load_receipt_btn.setEnabled(False)

        load_receipts_bar_layout.addWidget(self.path_to_file_lb)
        load_receipts_bar_layout.addWidget(choose_file_btn)
        load_receipts_bar_layout.addWidget(self.load_receipt_btn)

        return load_receipts_bar

    def create_transparent_btn(self, name, clbk):
        choose_file_btn = QPushButton(name)
        choose_file_btn.setStyleSheet("background-color: none")
        choose_file_btn.setMaximumWidth(120)
        choose_file_btn.clicked.connect(clbk)
        return choose_file_btn

    @Slot()
    def choose_file(self):
        path = QFileDialog.getOpenFileName(
            self, "Open PDF", filter="Rohlik.cz receipt (*.pdf)"
        )
        if not path[0]:
            return
        self.backend.file_name = path[0]
        self.path_to_file_lb.setText("File selected: " + self.backend.file_name)
        self.load_receipt_btn.setEnabled(True)

    @Slot()
    def load_receipt(self):
        self.backend.clear_layout(self.backend.items_wgt_container.layout())
        self.backend.scan_receipt()
        self.backend.fill_items_wgt_container()

        if self.backend.is_items_wgt_filled:
            self.calculate_cost_btn.setEnabled(True)
