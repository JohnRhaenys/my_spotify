class SongAlreadyExistsException(Exception):
    def __init__(self, message):
        self.message = message


class FolderDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message


class SongAlreadyInPlaylistException(Exception):
    def __init__(self, message):
        self.message = message
