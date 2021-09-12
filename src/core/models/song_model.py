class Song:

    def __init__(self, id, name, date_added, duration, thumbnail_path, path):
        self.id = id
        self.name = name
        self.date_added = date_added
        self.duration = duration
        self.thumbnail_path = thumbnail_path
        self.path = path

    def play(self):
        print(f'Playing song {self.name}')

    def pause(self):
        print(f'Paused song {self.name}')
