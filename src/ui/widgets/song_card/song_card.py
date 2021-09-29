from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QPushButton

from src.core.utils import utils
from src.ui.widgets.song_card import styles


class SongCard(QWidget):
    def __init__(
            self, id, index, name,
            date_added, duration, thumbnail_path="assets/images/default_thumbnail.png",
            parent=None
    ):
        super(SongCard, self).__init__(parent)

        self.enterEvent = self.on_mouse_hover
        self.leaveEvent = self.on_mouse_leave

        self.id = id
        self.index = index

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setSpacing(15)

        self.index_play_pause_button = QLabel(str(index))
        self.index_play_pause_button.setFixedWidth(25)
        self.index_play_pause_button.setFixedHeight(25)
        self.index_play_pause_button.setAlignment(Qt.AlignCenter)
        self.index_play_pause_button.enterEvent = lambda event: self.on_index_play_pause_button_mouse_hover(event)
        self.index_play_pause_button.mousePressEvent = lambda event: self.play_song()

        self.song_thumbnail = QLabel()
        self.song_thumbnail.setFixedHeight(45)
        self.song_thumbnail.setFixedWidth(45)
        self.song_thumbnail.setScaledContents(True)
        self.set_thumbnail_image(thumbnail_path)

        self.song_name = QLabel(str(name))
        self.song_name.setFixedHeight(45)
        self.song_name.setFixedWidth(600)

        self.date_added = QLabel(str(date_added))
        self.date_added.setFixedHeight(45)
        self.date_added.setFixedWidth(90)

        self.song_duration = QLabel(utils.time_formatter(duration))
        self.song_duration.setFixedHeight(45)

        self.remove_song_button = QPushButton()
        self.remove_song_button.setText("Remove")
        self.remove_song_button.setFixedHeight(40)
        self.remove_song_button.setFixedWidth(100)
        self.remove_song_button.setHidden(True)
        self.remove_song_button.mousePressEvent = self.remove_song_button_pressed

        self.allQHBoxLayout.addWidget(self.index_play_pause_button)
        self.allQHBoxLayout.addWidget(self.song_thumbnail)
        self.allQHBoxLayout.addWidget(self.song_name)
        self.allQHBoxLayout.addWidget(self.date_added)
        self.allQHBoxLayout.addWidget(self.song_duration)
        self.allQHBoxLayout.addWidget(self.remove_song_button)
        self.setLayout(self.allQHBoxLayout)
        self.set_styles()

    def play_song(self) -> None:
        print(f'Playing song: {self.song_name.text()}')

    def remove_song_button_pressed(self, _) -> None:
        print(f'Removing song {self.song_name.text()} from playlist')

    def on_mouse_hover(self, _) -> None:
        pixmap_image = QPixmap("assets/images/play_white.png")
        self.index_play_pause_button.setPixmap(pixmap_image)
        self.index_play_pause_button.setScaledContents(True)
        self.index_play_pause_button.setAlignment(Qt.AlignCenter)
        self.remove_song_button.setHidden(False)

    def on_index_play_pause_button_mouse_hover(self, _) -> None:
        self.index_play_pause_button.setCursor(QCursor(Qt.PointingHandCursor))

    def on_mouse_leave(self, _) -> None:
        self.index_play_pause_button.setText(str(self.index))
        self.remove_song_button.setHidden(True)

    def set_styles(self) -> None:
        self.index_play_pause_button.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.song_thumbnail.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.song_name.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.date_added.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.song_duration.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.remove_song_button.setStyleSheet(styles.REMOVE_BUTTON)

    def set_thumbnail_image(self, image_path: str) -> None:
        self.song_thumbnail.setPixmap(QPixmap(image_path))
