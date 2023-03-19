from PySide6.QtWidgets import QLineEdit


class SearchBarWidget(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setPlaceholderText("Search...")

    def on_text_changed(self, callback):
        self.textChanged.connect(callback)
