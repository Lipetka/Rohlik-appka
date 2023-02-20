from PySide6.QtWidgets import QLineEdit


class Customer:
    def __init__(self, name, bought_items) -> None:
        self.name_le: QLineEdit = QLineEdit()
        self.name_le.textChanged.connect(self.name_le_changed_clbk)
        self._name: str = ""
        self.name = name
        self.bought_items: dict = bought_items
        self.money_spent: dict = {}
        self.bought_portions_le: list[QLineEdit] = [
            QLineEdit() for item in bought_items
        ]
        for line_edit in self.bought_portions_le:
            line_edit.setMaximumWidth(40)

    def name_le_changed_clbk(self, new_name):
        self.name = new_name

    def get_total_cost(self) -> float:
        total_cost = 0.0
        item_prices = list(self.bought_items.values())
        for i, bought_portion_le in enumerate(self.bought_portions_le):
            if not bought_portion_le.text():
                value = 0.0
            else:
                value = float(bought_portion_le.text())*item_prices[i]
            total_cost += value

        return total_cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self.name_le.setText(self._name)

        