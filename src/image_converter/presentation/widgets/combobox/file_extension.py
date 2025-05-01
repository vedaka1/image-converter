from PyQt6.QtWidgets import QComboBox

from image_converter.application.types import FileExtension

_ALL_FILES_EXTENSION = 'All files (*)'


class FileExtensionComboBox(QComboBox):
    def __init__(self, extensions: list[str], default: FileExtension | None = None) -> None:
        super().__init__()
        self.selected = default if default else None

        for extension in extensions:
            self.addItem(extension)

        self.currentTextChanged.connect(self.extension_choice_changed)

    def extension_choice_changed(self, text: str) -> None:
        if text == _ALL_FILES_EXTENSION:
            self.selected = None
        else:
            self.selected = FileExtension(text)
