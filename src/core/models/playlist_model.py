from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent


class Playlist(QMediaPlaylist):

    SEQUENCE = 0
    LOOP_LIST = 1
    LOOP_CURRENT = 2

    def __init__(self, id, name, songs):
        super().__init__()
        self.id = id
        self.name = name
        self.songs = songs
        self.current = None
        self.playing = False
        self.set_mode(Playlist.SEQUENCE)
        self.populate()
        print(self.currentMedia().canonicalUrl())

    def set_mode(self, mode):
        if mode == Playlist.SEQUENCE:
            self.setPlaybackMode(QMediaPlaylist.Sequential)
        elif mode == Playlist.LOOP_CURRENT:
            self.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        elif mode == Playlist.LOOP_LIST:
            self.setPlaybackMode(QMediaPlaylist.Loop)

    def delete_song(self, song_id):
        del self.songs[song_id]
        if self.playing:
            current_song_index = self.currentIndex()
            self.removeMedia(current_song_index)
            self.populate()

    def play(self):
        if not self.playing:
            self.current.play()

    def pause(self):
        if self.playing:
            self.current.pause()

    def add_song(self, song_object):
        self.songs[song_object.id] = song_object

    def set_current_song(self, song_id):
        if self.playing:
            self.playing = False
            self.current = self.songs[song_id]

    def play_current(self):
        if self.current is not None:
            self.current.play()

    def pause_current(self):
        if self.current is not None:
            self.current.pause()

    def populate(self):
        self.clear()
        for index in self.songs:
            song = self.songs.get(index)
            path = song.path
            media = QMediaContent(QUrl.fromLocalFile(path))
            self.addMedia(media)
