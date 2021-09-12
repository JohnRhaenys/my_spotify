import os
import pickle

from src.core.utils.os_utils import file_exists

DEFAULT_FILEPATH = 'playlists.pkl'
DEFAULT_DIR = os.getcwd()


class DataManager:
    """
    This class contains a dictionary (hash table) with the following structure:

     Key   -> id of the playlist
     Value -> a playlist object which is related to that id
    """

    def __init__(self):
        self.data = self.load_data_from_file()
        self.filepath = DEFAULT_FILEPATH

    def add_person(self, person):
        self.data[person.id] = person

    def remove_song(self, person_id):
        if self.is_empty() or not self.is_person_registered(person_id=person_id):
            return False

        self.data.pop(person_id)
        return True

    def is_empty(self):
        return self.data is None or not self.data

    def get_all_people(self):
        return None if self.is_empty() else list(self.data.values())

    def get_all_ids(self):
        return [self.data.keys()]

    def get_person(self, person_id):
        return self.data.get(person_id)

    def is_person_registered(self, person_id):
        return not self.is_empty() and self.data.get(person_id) is not None

    def total_num_of_people(self):
        return len(self.data)

    def save_data_to_file(self):
        file_path = os.path.join(DEFAULT_DIR, DEFAULT_FILEPATH)
        with open(file_path, 'wb') as f:
            pickle.dump(self.data, f, pickle.HIGHEST_PROTOCOL)

    def load_data_from_file(self):
        file_path = os.path.join(DEFAULT_DIR, DEFAULT_FILEPATH)
        if not file_exists(file_path=file_path):
            return {}

        with open(file_path, 'rb') as f:
            try:
                data = pickle.load(f)
                return data
            except EOFError:
                return {}
