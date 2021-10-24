import typing

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from src.core.constants import STORAGE_TEMP_THUMBNAILS_FOLDER
from src.core.database import data_manager
from src.core.database.models.playlist_model import Playlist
from src.core.utils import utils, os_utils
from src.core.youtube import youtube_search
from src.ui.main_window import styles
from src.ui.widgets.audio_controller_widget.audio_controller_widget import AudioControllerWidget
from src.ui.widgets.dialog_box.dialog_box import DialogBox
from src.ui.widgets.list_widget.list_widget import ListWidget
from src.ui.widgets.playlist_card.playlist_card import PlaylistCard
from src.ui.widgets.song_card.song_card import SongCard
from src.ui.widgets.youtube_video_card.youtube_video_card import YoutubeVideoCard


class MainWindow(object):
    def __init__(self, main_window):

        self.main_window = main_window

        # Load the first playlist
        playlist = data_manager.get_playlist(playlist_id=1)
        playlist_card = PlaylistCard(id=playlist.id, name=playlist.name)
        self.current_playlist = playlist_card

        # Main window
        self.main_window.setWindowTitle('Spotify Free')
        self.main_window.showMaximized()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_window.sizePolicy().hasHeightForWidth())
        self.main_window.setSizePolicy(sizePolicy)

        # Central widget
        self.central_widget = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.central_widget.setAutoFillBackground(False)
        self.central_widget.setStyleSheet("")

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)

        # Parent widget
        self.parent = QtWidgets.QWidget(self.central_widget)

        # Outer vertical layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.parent)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)

        # UPPER AREA ---------------------------------------------------------------------
        self.upper_area = QtWidgets.QSplitter(self.parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_area.sizePolicy().hasHeightForWidth())
        self.upper_area.setSizePolicy(sizePolicy)
        self.upper_area.setOrientation(QtCore.Qt.Horizontal)
        self.upper_area.setStyleSheet(styles.SPLITTER)

        # LEFT-UPPER AREA ---------------------------------------------------------------------
        self.left_area_2 = QtWidgets.QWidget(self.upper_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_area_2.sizePolicy().hasHeightForWidth())
        self.left_area_2.setSizePolicy(sizePolicy)
        self.left_area_2.setMinimumSize(QtCore.QSize(225, 0))
        self.left_area_2.setMaximumSize(QtCore.QSize(225, 16777215))
        self.left_area_2.setStyleSheet(styles.LEFT_AREA)
        self.left_area = QtWidgets.QVBoxLayout(self.left_area_2)
        self.left_area.setContentsMargins(12, 12, 12, 12)

        self.playlists_label = QtWidgets.QLabel(self.left_area_2)
        self.playlists_label.setText('PLAYLISTS')
        self.playlists_label.setStyleSheet(styles.GRAY_TEXT_BOLD)

        self.left_area.addWidget(self.playlists_label)
        self.create_playlist_hbox = QtWidgets.QHBoxLayout()

        self.create_playlist_button = QtWidgets.QPushButton(self.left_area_2)
        self.create_playlist_button.setText('Create Playlist')
        self.create_playlist_button.setFixedHeight(40)
        self.create_playlist_button.setStyleSheet(styles.PLAYLIST_BUTTON)
        self.create_playlist_hbox.addWidget(self.create_playlist_button)

        self.line = QtWidgets.QFrame(self.left_area_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setStyleSheet(styles.LINE)
        self.line.setFixedHeight(1)
        self.left_area.addLayout(self.create_playlist_hbox)
        self.left_area.addWidget(self.line)
        self.playlist_list = ListWidget(main_window_reference=self, parent=self.left_area_2)
        self.playlist_list.setStyleSheet(styles.PLAYLIST_LIST)
        self.left_area.addWidget(self.playlist_list)

        # RIGHT UPPER AREA ---------------------------------------------------------------------
        self.right_area_2 = QtWidgets.QWidget(self.upper_area)
        self.right_area_2.setStyleSheet(styles.RIGHT_AREA)
        self.right_area = QtWidgets.QVBoxLayout(self.right_area_2)
        self.right_area.setContentsMargins(12, 12, 12, 12)

        self.search_label = QtWidgets.QLabel(self.right_area_2)
        self.search_label.setText('Search')
        self.search_label.setStyleSheet(styles.GRAY_TEXT_BOLD)
        self.right_area.addWidget(self.search_label)

        self.search_box = QtWidgets.QLineEdit(self.right_area_2)
        self.search_box.setMinimumSize(QtCore.QSize(200, 25))
        self.search_box.setMaximumSize(QtCore.QSize(200, 25))
        self.search_box.setStyleSheet(styles.SEARCH_BOX)
        self.right_area.addWidget(self.search_box)

        self.playlist_name_label = QtWidgets.QLineEdit(self.right_area_2)
        self.playlist_name_label.setStyleSheet(styles.PLAYLIST_TITLE)
        self.playlist_name_label.setAlignment(Qt.AlignLeft)
        self.right_area.addWidget(self.playlist_name_label)

        self.playlist_info_label = QtWidgets.QLabel(self.right_area_2)
        self.playlist_info_label.setStyleSheet(styles.GRAY_TEXT)
        self.right_area.addWidget(self.playlist_info_label)

        self.songs_list = ListWidget(parent=self.right_area_2, main_window_reference=self)
        self.right_area.addWidget(self.songs_list)
        self.verticalLayout_2.addWidget(self.upper_area)
        self.songs_list.setStyleSheet(styles.SONGS_LIST)

        # BOTTOM AREA ---------------------------------------------------------------------
        self.audio_controller = AudioControllerWidget(parent=self.parent)
        self.verticalLayout_2.addWidget(self.audio_controller.bottom_area)

        self.gridLayout.addWidget(self.parent, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # BACKEND ---------------------------------------------------------------------
        self.set_listeners()
        self.populate_playlist_list()
        self.populate_songs_list(self.current_playlist.get_id())

    def set_listeners(self) -> None:
        self.create_playlist_button.clicked.connect(self.create_playlist_button_clicked)
        self.search_box.returnPressed.connect(self.enter_key_pressed)
        self.playlist_name_label.returnPressed.connect(self.playlist_name_label_enter_pressed)

    def playlist_name_label_enter_pressed(self) -> None:
        data_manager.edit_playlist_name(self.current_playlist.get_id(), new_name=self.playlist_name_label.text())
        self.populate_playlist_list()
        DialogBox(icon='success', title='Ok', message='Your playlist name has changed!')

    def create_playlist_button_clicked(self) -> None:
        QApplication.setOverrideCursor(Qt.WaitCursor)
        new_playlist = Playlist(name='New playlist')
        data_manager.insert_new_playlist(playlist=new_playlist)
        QApplication.restoreOverrideCursor()
        DialogBox(icon='success', title='Ok', message='A new playlist has been created!')
        self.populate_playlist_list()

    def enter_key_pressed(self) -> None:
        current_playlist_name = self.playlist_name_label.text()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.playlist_name_label.setText('Searching ...')
        self.playlist_info_label.setHidden(True)
        QApplication.processEvents()
        try:
            self.clear_temp_thumbnails()
            search_string = self.search_box.text()
            videos = youtube_search.search_for_videos(search_string)
            if len(videos) == 0:
                QApplication.restoreOverrideCursor()
                DialogBox(icon='danger', title='Oops', message='No videos have been found')
                self.playlist_name_label.setText(current_playlist_name)
                self.playlist_info_label.setHidden(False)
                return

            # Sort the videos by view count in descending order
            videos.sort(key=lambda vid: vid.views, reverse=True)

            video_cards = []
            for index, video in enumerate(videos):
                thumbnail_path = video.download_thumbnail()
                video_card = YoutubeVideoCard(
                    index=str(index + 1),
                    thumbnail_path=thumbnail_path,
                    title=video.title,
                    views=video.views_extense,
                    duration=video.duration,
                    video_id=video.id,
                    video_url=video.url
                )
                video_cards.append(video_card)
            self.populate_video_card_list(video_cards)
            self.playlist_name_label.setText(f'Results for "{search_string}"')

        except Exception as e:
            DialogBox(icon='danger', title='Error', message=f'Something went wrong searching for the videos\n{e}')
            print(e)
            self.playlist_name_label.setText(current_playlist_name)
            self.playlist_info_label.setHidden(False)
        QApplication.restoreOverrideCursor()

    def clear_temp_thumbnails(self) -> None:
        os_utils.clear_folder(STORAGE_TEMP_THUMBNAILS_FOLDER)

    def populate_playlist_list(self) -> None:
        self.playlist_list.clear()
        data = data_manager.get_all_playlists()
        playlists = []
        if data is not None:
            for playlist in data:
                playlist_card = PlaylistCard(id=playlist.id, name=playlist.name)
                playlists.append(playlist_card)
        self.playlist_list.set_items(playlists)

    def populate_songs_list(self, playlist_id: int) -> None:
        self.songs_list.clear()
        playlist = data_manager.get_playlist(playlist_id=playlist_id)
        self.playlist_name_label.setText(playlist.name)
        song_list = []
        songs_paths = []
        if playlist is not None:
            songs = playlist.get_songs(data_manager.engine)
            playlist_total_time = 0
            for index, song_id in enumerate(songs):
                song = data_manager.get_song(song_id)
                song_card = SongCard(
                    song=song,
                    card_index=index + 1,
                    playlist_id=playlist_id,
                    parent=self.songs_list,
                    main_window_reference=self
                )
                playlist_total_time += song.duration_in_seconds
                song_list.append(song_card)
                songs_paths.append(song.file_path)
            self.playlist_info_label.setHidden(False)
            self.playlist_info_label.setText(f'{str(len(songs))} songs, {utils.time_formatter_extense(playlist_total_time)}')
        self.songs_list.set_items(song_list)
        self.audio_controller.populate_playlist(songs_paths)

    def populate_video_card_list(self, video_cards: typing.List[YoutubeVideoCard]) -> None:
        self.songs_list.set_items(video_cards)
