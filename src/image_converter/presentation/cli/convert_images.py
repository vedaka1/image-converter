from image_converter.application.usecases.convert_image import convert_image
from image_converter.presentation.cli.extension import get_from_and_to_extension
from image_converter.presentation.path import format_path, get_filepaths


def convert_images_from_path() -> None:
    try:
        path = format_path(str(input('folder of file path: ')))
        from_extension, to_extension = get_from_and_to_extension(path)
        filepaths = get_filepaths(path=path, from_extension=from_extension)
        print(f'{len(filepaths)} files will be converted to {to_extension.value}')
        for filepath in filepaths:
            convert_image(filepath=filepath, to_extension=to_extension)
    except Exception as e:
        print(e)
