from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget

from src.ui.widgets.youtube_video_card import styles


class YoutubeVideoCard(QWidget):
    def __init__(self, index, thumbnail_path, title, views, duration, parent=None):
        super(YoutubeVideoCard, self).__init__(parent)
        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setSpacing(15)

        self.index_add_to_playlist_button = QLabel(index)
        self.index_add_to_playlist_button.setFixedWidth(30)
        self.index_add_to_playlist_button.setFixedHeight(45)
        self.index_add_to_playlist_button.setAlignment(Qt.AlignCenter)

        self.video_thumbnail = QLabel()
        self.video_thumbnail.setFixedHeight(45)
        self.video_thumbnail.setFixedWidth(45)
        self.set_thumbnail_image(thumbnail_path)

        self.video_title = QLabel(title)
        self.video_title.setFixedHeight(45)

        self.video_views = QLabel(views)
        self.video_views.setFixedHeight(45)

        self.video_duration = QLabel(duration)
        self.video_duration.setFixedHeight(45)

        self.allQHBoxLayout.addWidget(self.index_add_to_playlist_button)
        self.allQHBoxLayout.addWidget(self.video_thumbnail)
        self.allQHBoxLayout.addWidget(self.video_title)
        self.allQHBoxLayout.addWidget(self.video_views)
        self.allQHBoxLayout.addWidget(self.video_duration)
        self.setLayout(self.allQHBoxLayout)
        self.set_styles()

    def set_styles(self):
        self.index_add_to_playlist_button.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_thumbnail.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_title.setStyleSheet(styles.REGULAR_WHITE_TEXT_14)
        self.video_views.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_duration.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)

    def set_thumbnail_image(self, image_path):
        self.video_thumbnail.setPixmap(QPixmap(image_path))
