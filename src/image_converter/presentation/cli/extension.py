import os

from image_converter.application.types import FileExtension


def get_available_extensions() -> tuple[str, dict[int, FileExtension]]:
    available_extensions = ''
    number = 1
    input_map = {}
    for extension in FileExtension:
        available_extensions += f'{number}: .{extension.value}\n'
        input_map[number] = extension
        number += 1
    return available_extensions, input_map


def get_from_and_to_extension(path: str) -> tuple[FileExtension, FileExtension]:
    if not os.path.exists(path):
        raise Exception('folder or file not found')

    extensions, input_map = get_available_extensions()
    if os.path.isdir(path):
        from_extension_number = int(input(f'from format:\n{extensions}number: '))
        from_extension = input_map[from_extension_number]
    else:
        from_extension = FileExtension(path.rsplit('.', 1)[-1])
    to_extension_number = int(input(f'to format:\n{extensions}number: '))
    to_extension = input_map[to_extension_number]
    return from_extension, to_extension
