import os
import shutil

from src.core.exceptions import FolderDoesNotExistException


def create_folder(dir_path: str) -> str or None:
    try:
        if not folder_exists(dir_path):
            os.makedirs(dir_path)
            return dir_path
    except OSError:
        print(f'Error creating directory "{dir_path}"')
        return None


def folder_exists(dir_path: str) -> bool:
    return os.path.isdir(dir_path)


def is_directory_empty(dir_path: str) -> bool:
    return len(os.listdir(dir_path)) == 0


def delete_folder(picture_directory_path: str) -> bool:
    try:
        shutil.rmtree(picture_directory_path)
        return True
    except Exception as e:
        print(e)
        return False


def get_filename(file_path: str) -> str:
    """
    Given the full path to a file, extracts only the name of the file with its extension
    """
    base_path, file_extension = os.path.splitext(file_path)
    filename = f'{base_path[base_path.rfind(os.path.sep) + 1:]}{file_extension}'
    return filename


def is_audio_file(file_path: str) -> bool:
    return get_file_extension(file_path) in ('.mp3', '.wav')


def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()


def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)


def move_file(file_path: str, other_folder: str) -> bool:
    if not folder_exists(other_folder):
        raise FolderDoesNotExistException(f'The folder {other_folder} does not exist.')

    try:
        shutil.move(file_path, other_folder)
        return True
    except Exception as e:
        print(e)
        return False


def clear_folder(folder_path: str) -> bool:
    try:
        file_list = [f for f in os.listdir(folder_path)]
        for f in file_list:
            os.remove(os.path.join(folder_path, f))
        return True
    except Exception as e:
        print(e)
        return False
