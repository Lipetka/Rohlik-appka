from PySide6.QtWidgets import QLineEdit


class Customer:
    def __init__(self, name, bought_items) -> None:
        self.name_le: QLineEdit = QLineEdit()
        self.name_le.textChanged.connect(self.name_le_changed_clbk)
        self._name: str = ""
        self.name = name
        self.bought_items: dict = bought_items
        self._bought_portions = [0 for item in bought_items]
        self.bought_portions_le: list[QLineEdit] = [
            QLineEdit() for item in bought_items
        ]
        for line_edit in self.bought_portions_le:
            line_edit.setMaximumWidth(40)

    def name_le_changed_clbk(self, new_name):
        self.name = new_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self.name_le.setText(self._name)
