from PyQt5 import QtCore, QtWidgets

from src.core.models.playlist_model import Playlist
from src.core.models.song_model import Song
from src.ui.main_window import styles
from src.ui.widgets.audio_controller_widget.audio_controller_widget import AudioControllerWidget
from src.ui.widgets.list_widget.list_widget import ListWidget
from src.ui.widgets.youtube_video_card.youtube_video_card import YoutubeVideoCard


class MainWindow(object):
    def __init__(self, main_window):

        self.main_window = main_window

        # Main window
        self.main_window.setWindowTitle("Spotify Free")
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
        self.playlists_label.setText("PLAYLISTS")
        self.playlists_label.setStyleSheet(styles.GRAY_TEXT_BOLD)

        self.left_area.addWidget(self.playlists_label)
        self.create_playlist_hbox = QtWidgets.QHBoxLayout()

        self.create_playlist_button = QtWidgets.QPushButton(self.left_area_2)
        self.create_playlist_button.setText("Create Playlist")
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
        self.playlist_list = ListWidget(parent=self.left_area_2)
        self.left_area.addWidget(self.playlist_list)

        # RIGHT UPPER AREA ---------------------------------------------------------------------
        self.right_area_2 = QtWidgets.QWidget(self.upper_area)
        self.right_area_2.setStyleSheet(styles.RIGHT_AREA)
        self.right_area = QtWidgets.QVBoxLayout(self.right_area_2)
        self.right_area.setContentsMargins(12, 12, 12, 12)

        self.search_label = QtWidgets.QLabel(self.right_area_2)
        self.search_label.setText("Search")
        self.search_label.setStyleSheet(styles.GRAY_TEXT_BOLD)
        self.right_area.addWidget(self.search_label)

        self.search_box = QtWidgets.QTextEdit(self.right_area_2)
        self.search_box.setMinimumSize(QtCore.QSize(200, 25))
        self.search_box.setMaximumSize(QtCore.QSize(200, 25))
        self.search_box.setStyleSheet(styles.SEARCH_BOX)
        self.right_area.addWidget(self.search_box)

        self.songs_list = ListWidget(parent=self.right_area_2)
        self.right_area.addWidget(self.songs_list)
        self.verticalLayout_2.addWidget(self.upper_area)
        self.songs_list.setStyleSheet(styles.LIST)

        # BOTTOM AREA ---------------------------------------------------------------------
        playlist = Playlist(
            id=0, name='Playlist teste',
            songs={
                0: Song(id=0, name='Musica teste', date_added='DAta teste',
                        duration='Duracao teste', thumbnail_path='', path='teste')
            })
        self.audio_controller = AudioControllerWidget(playlist=playlist, parent=self.parent)
        self.verticalLayout_2.addWidget(self.audio_controller.bottom_area)

        self.gridLayout.addWidget(self.parent, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.set_listeners()

    def set_listeners(self):
        self.create_playlist_button.clicked.connect(self.create_playlist_button_clicked)

    def create_playlist_button_clicked(self):
        print('Create playlist button')

    def load_data(self):
        # Load current playlist
        pass

    def populate_songs_list(self):
        items = [YoutubeVideoCard('11', '12', '13', '14', '15'), YoutubeVideoCard('21', '22', '23', '24', '25')]
        self.songs_list.set_items(items)
