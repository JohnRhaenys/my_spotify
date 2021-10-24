import typing

from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel, QSpacerItem, \
    QVBoxLayout, QLayout, QPushButton

from src.ui.main_window import styles
from src.ui.widgets.slider.slider import Slider


class AudioControllerWidget(QWidget):
    def __init__(self, parent=None):
        super(AudioControllerWidget, self).__init__(parent)

        # THE PLAYLIST
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)
        self.playing = False
        self.current_song_index = 1  # Control variable. We start from 1 because this is the first ID
        self.current_song_thumbnail_path = 'assets/images/default_thumbnail.png'
        self.current_song = None

        # FRONTEND
        layout = QHBoxLayout()
        self.bottom_area = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_area.sizePolicy().hasHeightForWidth())
        self.bottom_area.setSizePolicy(sizePolicy)
        self.bottom_area.setStyleSheet(styles.BOTTOM_AREA)
        self.player_area = QHBoxLayout(self.bottom_area)
        self.player_area.setContentsMargins(4, 4, 4, 4)

        # BOTTOM PLAYER VIEW AREA ---------------------------------------------------------------------
        self.player_view_area = QWidget(self.bottom_area)
        self.player_view_area.setMinimumSize(QSize(200, 0))
        self.player_view_area.setMaximumSize(QSize(200, 16777215))

        self.player_info_area = QVBoxLayout(self.player_view_area)
        self.player_info_area.setSizeConstraint(QLayout.SetNoConstraint)

        self.current_song_status = QLabel(self.player_view_area)
        self.current_song_status.setText('No songs playing')
        self.current_song_status.setStyleSheet(styles.GRAY_TEXT)

        self.player_info_area.addWidget(self.current_song_status)
        self.player_view_area_hbox = QHBoxLayout()

        self.song_thumbnail = QLabel(self.player_view_area)
        self.song_thumbnail.setMinimumSize(QSize(55, 55))
        self.song_thumbnail.setMaximumSize(QSize(55, 55))
        self.song_thumbnail.setText('')
        self.set_thumbnail('assets/images/default_thumbnail.png')
        self.song_thumbnail.setScaledContents(True)
        self.song_thumbnail.setWordWrap(False)
        self.player_view_area_hbox.addWidget(self.song_thumbnail)

        self.song_name = QLabel(self.player_view_area)
        self.song_name.setText('')
        self.song_name.setStyleSheet(styles.LIGHT_TEXT)
        self.player_view_area_hbox.addWidget(self.song_name)
        self.player_info_area.addLayout(self.player_view_area_hbox)

        # BOTTOM PLAYER CONTROLS AREA ---------------------------------------------------------------------
        self.player_area.addWidget(self.player_view_area)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.player_area.addItem(spacerItem)
        self.player_controls_area_2 = QWidget(self.bottom_area)
        self.player_controls_area_2.setMinimumSize(QSize(0, 0))
        self.player_controls_area_2.setMaximumSize(QSize(16777215, 16777215))
        self.player_controls_area = QVBoxLayout(self.player_controls_area_2)

        self.player_control_buttons_area = QWidget(self.player_controls_area_2)
        self.player_control_buttons_area.setMinimumSize(QSize(250, 0))
        self.player_control_buttons_area.setMaximumSize(QSize(999999, 16777215))

        self.player_controls_hbox_1 = QHBoxLayout(self.player_control_buttons_area)
        self.player_controls_hbox_1.setSpacing(20)

        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.player_controls_hbox_1.addItem(spacerItem1)

        self.previous_button = QPushButton(self.player_control_buttons_area)
        icon = QIcon()
        icon.addPixmap(QPixmap('assets/images/previous_song.png'), QIcon.Normal, QIcon.Off)
        self.previous_button.setIcon(icon)
        self.previous_button.setStyleSheet(styles.HIDDEN_BUTTON_PREVIOUS)
        self.previous_button.setFixedWidth(40)
        self.previous_button.setFixedHeight(40)
        self.previous_button.setIconSize(QSize(13, 13))
        self.player_controls_hbox_1.addWidget(self.previous_button)

        self.play_pause_button = QPushButton(self.player_control_buttons_area)
        icon = QIcon()
        icon.addPixmap(QPixmap('assets/images/play.png'), QIcon.Normal, QIcon.Off)
        self.play_pause_button.setIcon(icon)
        self.play_pause_button.setStyleSheet(styles.ROUND_BUTTON)
        self.play_pause_button.setFixedWidth(40)
        self.play_pause_button.setFixedHeight(40)
        self.play_pause_button.setIconSize(QSize(10, 10))
        self.player_controls_hbox_1.addWidget(self.play_pause_button)
        self.play_pause_button.setStyleSheet(styles.ROUND_BUTTON)

        self.next_button = QPushButton(self.player_control_buttons_area)
        icon = QIcon()
        icon.addPixmap(QPixmap('assets/images/next_song.png'), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setStyleSheet(styles.HIDDEN_BUTTON_NEXT)
        self.next_button.setFixedWidth(40)
        self.next_button.setFixedHeight(40)
        self.next_button.setIconSize(QSize(13, 13))
        self.player_controls_hbox_1.addWidget(self.next_button)

        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.player_controls_hbox_1.addItem(spacerItem2)

        self.player_controls_area.addWidget(self.player_control_buttons_area)
        self.player_controls_hbox_2 = QHBoxLayout()

        self.current_song_time = QLabel(self.player_controls_area_2)
        self.current_song_time.setText('0:00')
        self.current_song_time.setStyleSheet(styles.GRAY_TEXT)
        self.player_controls_hbox_2.addWidget(self.current_song_time)

        self.time_slider = Slider(
            min_width=400,
            max_width=400,
            parent=self.player_controls_area_2,
            value_changed=lambda value: self.time_slider_moved(value)
        )
        self.player_controls_hbox_2.addWidget(self.time_slider)

        self.song_total_time = QLabel(self.player_controls_area_2)
        self.song_total_time.setText('0:00')
        self.song_total_time.setStyleSheet(styles.GRAY_TEXT)
        self.player_controls_hbox_2.addWidget(self.song_total_time)

        self.player_controls_area.addLayout(self.player_controls_hbox_2)
        self.player_area.addWidget(self.player_controls_area_2)

        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.player_area.addItem(spacerItem3)

        # BOTTOM VOLUME AREA ---------------------------------------------------------------------
        self.player_volume_area_2 = QWidget(self.bottom_area)
        self.player_volume_area_2.setMinimumSize(QSize(200, 0))
        self.player_volume_area_2.setMaximumSize(QSize(200, 16777215))
        self.player_volume_area = QHBoxLayout(self.player_volume_area_2)

        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.player_volume_area.addItem(spacerItem4)

        self.volume_button = QPushButton(self.player_volume_area_2)
        icon = QIcon()
        icon.addPixmap(QPixmap('assets/images/volume.png'), QIcon.Normal, QIcon.Off)
        self.volume_button.setIcon(icon)
        self.volume_button.setStyleSheet(styles.HIDDEN_BUTTON_NEXT)
        self.volume_button.setFixedWidth(40)
        self.volume_button.setFixedHeight(40)
        self.volume_button.setIconSize(QSize(15, 15))
        self.player_volume_area.addWidget(self.volume_button)

        self.volume_slider = Slider(
            min_width=100,
            max_width=100,
            default_value=50,
            parent=self.player_volume_area_2,
            value_changed=lambda volume: self.volume_slider_moved(volume)
        )
        self.player_volume_area.addWidget(self.volume_slider)
        self.player_area.addWidget(self.player_volume_area_2)

        layout.addWidget(self.bottom_area)
        self.setLayout(layout)
        self.set_listeners()
        self.player.setVolume(self.volume_slider.get_value())

    def set_listeners(self) -> None:
        self.previous_button.clicked.connect(self.previous_button_clicked)
        self.play_pause_button.clicked.connect(self.play_pause_button_clicked)
        self.next_button.clicked.connect(self.next_button_clicked)
        self.volume_button.clicked.connect(self.volume_button_clicked)

    def time_slider_moved(self, position: int) -> None:
        self.player.setPosition(position)

    def volume_slider_moved(self, volume: int) -> None:
        self.player.setVolume(volume)

    def previous_button_clicked(self) -> None:
        self.player.playlist().previous()

    def play_pause_button_clicked(self) -> None:
        if self.playing:
            self.pause()
            self.switch_play_pause_button_icon('play')
            self.current_song_status.setText('Paused')
        else:
            self.play(song_thumbnail_path=self.current_song_thumbnail_path, resume=True)
            self.switch_play_pause_button_icon('pause')
            self.current_song_status.setText('Playing')

    def next_button_clicked(self) -> None:
        self.player.playlist().next()

    def volume_button_clicked(self) -> None:
        if self.volume_slider.get_value() == 0:
            self.volume_slider.set_value(100)
            self.player.setVolume(100)
        else:
            self.volume_slider.set_value(0)
            self.player.setVolume(0)

    def populate_playlist(self, songs_paths: typing.List[str]):
        self.playlist.clear()
        url = QUrl()
        for path in songs_paths:
            media_url = url.fromLocalFile(path)
            self.playlist.addMedia(QMediaContent(media_url))

    def play(
            self,
            song_thumbnail_path='assets/images/default_thumbnail.png',
            song_index=None,
            resume=False
    ):
        if resume:
            self.player.play()
        else:
            self.current_song_index = song_index
            self.playlist.setCurrentIndex(song_index - 1)
            self.set_thumbnail(song_thumbnail_path)
        self.playing = True

    def pause(self):
        self.player.pause()
        self.playing = False

    def set_thumbnail(self, thumbnail_path):
        self.song_thumbnail.setPixmap(QPixmap(thumbnail_path))

    def switch_play_pause_button_icon(self, state):
        icon = QIcon()
        if state == 'play':
            icon.addPixmap(QPixmap('assets/images/play.png'), QIcon.Normal, QIcon.Off)
        else:
            icon.addPixmap(QPixmap('assets/images/pause.png'), QIcon.Normal, QIcon.Off)
        self.play_pause_button.setIcon(icon)
