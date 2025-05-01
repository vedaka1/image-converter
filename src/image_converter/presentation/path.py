import os

from image_converter.application.types import FileExtension


def get_filepaths(path: str, from_extension: FileExtension) -> list[str]:
    if os.path.isdir(path):
        files = []
        for file in os.listdir(path):
            if file.rsplit('.', 1)[-1] == from_extension.value:
                files.append(f'{path}/{file}')
        return files
    else:
        return [path]


def format_path(filepath: str) -> str:
    filepath = filepath.replace('\\', '/')
    if filepath[0] == '"' and filepath[-1] == '"':
        filepath = filepath.replace('"', '')
    return filepath
