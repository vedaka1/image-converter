import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

from image_converter.presentation.main_window import MainWindow
from resources import resource_path


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon(resource_path('icons/icon.png')))
    window.show()
    app.exec()


main()
