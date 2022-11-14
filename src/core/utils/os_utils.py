import os
import shutil
import time

from src.core.exceptions import FolderDoesNotExistException
from pathlib import Path


def create_folder(dir_path):
    try:
        if not folder_exists(dir_path):
            os.makedirs(dir_path)
            return dir_path
    except OSError:
        print(f'Error creating directory "{dir_path}"')
        return None


def folder_exists(dir_path):
    return os.path.isdir(dir_path)


def is_directory_empty(dir_path):
    return len(os.listdir(dir_path)) == 0


def delete_folder(directory_path):
    try:
        shutil.rmtree(directory_path)
        return True
    except Exception as e:
        print(e)
        return False


def get_filename(file_path):
    """
    Given the full path to a file, extracts only the name of the file with its extension
    """
    base_path, file_extension = os.path.splitext(file_path)
    filename = f'{base_path[base_path.rfind(os.path.sep) + 1:]}{file_extension}'
    return filename


def is_audio_file(file_path):
    return get_file_extension(file_path) in ('.mp3', '.wav')


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def file_exists(file_path):
    return os.path.isfile(file_path)


def move_file(file_path, other_folder):
    if not folder_exists(other_folder):
        raise FolderDoesNotExistException(f'The folder {other_folder} does not exist.')

    try:
        shutil.move(file_path, other_folder)
        return True
    except Exception as e:
        print(e)
        return False


def clear_folder(folder_path):
    try:
        file_list = [file for file in os.listdir(folder_path)]
        for file in file_list:
            os.remove(os.path.join(folder_path, file))
        return True
    except Exception as e:
        print(e)
        return False


def delete_file(file_path):
    try:
        os.remove(file_path)
        return file_path
    except Exception as e:
        print(e)
        return None


def rename_file(original_filepath, new_file_name):
    original_filename = get_filename(original_filepath)
    new_file = original_filepath.replace(original_filename, new_file_name)
    os.rename(original_filepath, new_file)


def get_file_directory(filepath):
    path = Path(filepath)
    return path.parent


def current_milli_time():
    return round(time.time() * 1000)
