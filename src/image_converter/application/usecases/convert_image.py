from dataclasses import dataclass

from PIL import Image
from pillow_heif import register_heif_opener

from image_converter.application.types import FileExtension

register_heif_opener()


def convert_image(filepath: str, to_extension: FileExtension, result_path: str | None = None) -> None:
    filename = filepath.rsplit('.', 1)[0]
    new_filepath = f'{filename}.{to_extension.value}'
    if result_path:
        new_filepath = f'{result_path}/{filename.rsplit("/", 1)[-1]}.{to_extension.value}'

    try:
        image = Image.open(filepath)
        image.save(new_filepath, format=to_extension.name)
    except Exception:
        raise Exception(f'Can not convert file {filepath} to {to_extension.value}')


@dataclass(kw_only=True, slots=True, eq=False)
class ConvertImageUseCase:
    def execute(self, filepath: str, to_extension: FileExtension, result_path: str | None = None) -> None:
        filename = filepath.rsplit('.', 1)[0]
        new_filepath = f'{filename}.{to_extension.value}'
        if result_path:
            new_filepath = f'{result_path}/{filename.rsplit("/", 1)[-1]}.{to_extension.value}'

        try:
            image = Image.open(filepath)
            image.save(new_filepath, format=to_extension.name)
        except Exception:
            raise Exception(f'Can not convert file {filepath} to {to_extension.value}')
