from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self, title: str, text: str = 'Something happened, is that OK?'):
        super().__init__()
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.message = QLabel(text)
        layout.addWidget(self.message)
        self.setLayout(layout)
