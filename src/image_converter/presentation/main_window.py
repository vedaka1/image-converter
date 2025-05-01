from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from image_converter.presentation.widgets.convert_file import ConvertFileWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Image Converter')
        self.setMinimumWidth(300)

        container = QWidget()
        layout = QVBoxLayout(container)
        self.setCentralWidget(container)
        container.setLayout(layout)

        widgets = (ConvertFileWidget(),)
        for widget in widgets:
            layout.addWidget(widget)
