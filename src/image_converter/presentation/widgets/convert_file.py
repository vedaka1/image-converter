from PyQt6.QtWidgets import QFileDialog, QLabel, QPushButton, QVBoxLayout, QWidget

from image_converter.application.types import FileExtension
from image_converter.application.usecases.convert_image import ConvertImageUseCase
from image_converter.presentation.common.dialog import CustomDialog
from image_converter.presentation.common.scroll_label import ScrollLabel
from image_converter.presentation.path import format_path
from image_converter.presentation.widgets.combobox.file_extension import ALL_FILES_EXTENSION, FileExtensionComboBox


def create_selected_label_text(selected_filenames: list[str], result_folder: str | None = None) -> str:
    if not result_folder:
        if selected_filenames:
            result_folder = selected_filenames[0].rsplit('/', 1)[0]

    destination = f'Файлы будут сохранены в {result_folder}\n' if result_folder else ''
    text = f'{destination}Выбрано {len(selected_filenames)} файлов:\n'
    for item in selected_filenames:
        filename = item.rsplit('/', 1)[-1]
        text += f'{filename}\n'
    return text


class ConvertFileWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.selected_files: list[str] = []
        self.result_path: str | None = None

        layout = QVBoxLayout(self)

        convert_from_label = QLabel('Конвертировать из:')
        self.convert_from_combobox = FileExtensionComboBox(
            extensions=[ALL_FILES_EXTENSION, *(ext.value for ext in FileExtension)],
        )
        convert_to_label = QLabel('Конвертировать в:')
        self.convert_to_combobox = FileExtensionComboBox(
            extensions=[ext.value for ext in FileExtension],
            default=FileExtension.PNG,
        )
        self.selected_label = ScrollLabel()
        self.selected_label.setText(create_selected_label_text(self.selected_files))

        btn_open_files = QPushButton('Выбрать файлы')
        btn_open_files.clicked.connect(self.open_files)

        btn_choose_result_folder = QPushButton('Выбрать папку сохранения')
        btn_choose_result_folder.clicked.connect(self.choose_result_folder)

        btn_convert_files = QPushButton('Конвертировать')
        btn_convert_files.clicked.connect(self.convert_files)

        for widget in (
            convert_from_label,
            self.convert_from_combobox,
            convert_to_label,
            self.convert_to_combobox,
            btn_open_files,
            btn_choose_result_folder,
            self.selected_label,
            btn_convert_files,
        ):
            layout.addWidget(widget)

    def open_files(self):
        filter = f'*.{self.convert_from_combobox.selected.value}' if self.convert_from_combobox.selected else None
        files_paths = QFileDialog.getOpenFileNames(parent=self, caption='Choose folder', filter=filter)
        self.selected_files = [path for path in files_paths[0]]
        self.selected_label.setText(create_selected_label_text(self.selected_files))

    def convert_files(self):
        dlg = CustomDialog(title='Успешно', text=f'Конвертировано {len(self.selected_files)} файлов')
        try:
            for filepath in self.selected_files:
                if not self.convert_to_combobox.selected:
                    raise Exception('Выберите расширение для конвертации')
                use_case = ConvertImageUseCase()
                use_case.execute(
                    filepath=filepath,
                    to_extension=self.convert_to_combobox.selected,
                    result_path=self.result_path,
                )
        except Exception as e:
            dlg.setWindowTitle('Ошибка')
            dlg.message.setText(str(e))
        dlg.exec()

    def choose_result_folder(self) -> None:
        path = QFileDialog.getExistingDirectory(parent=self, caption='Choose folder')
        self.result_path = format_path(path) if path else None
        self.selected_label.setText(create_selected_label_text(self.selected_files, result_folder=self.result_path))
