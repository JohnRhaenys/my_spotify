import os
import shutil


def create_folder(dir_path):
    try:
        if not is_valid_directory(dir_path):
            os.makedirs(dir_path)
    except OSError:
        print(f'Error creating directory "{dir_path}"')


def is_valid_directory(dir_path):
    return os.path.isdir(dir_path)


def is_directory_empty(dir_path):
    return len(os.listdir(dir_path)) == 0


def delete_folder(picture_directory_path):
    try:
        shutil.rmtree(picture_directory_path)
        return True
    except Exception:
        return False


def get_filename(file_path):
    """
    Given the full path to a file, extracts only the name of the file with its extension
    """
    base_path, file_extension = os.path.splitext(file_path)
    filename = base_path[base_path.rfind('/') + 1:base_path.rfind('.')]
    return filename


def is_audio_file(file_path):
    return get_file_extension(file_path) in ('.mp3', '.wav')


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def file_exists(file_path):
    return os.path.isfile(file_path)
