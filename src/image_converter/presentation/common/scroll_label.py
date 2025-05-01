from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget


class ScrollLabel(QScrollArea):
    def __init__(self, minw: int = 300, minh: int = 100, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setMinimumSize(minw, minh)
        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)
        layout = QVBoxLayout(content)

        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)
