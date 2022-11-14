import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication, QPushButton
from pytube import YouTube

from src.core import web_browser
from src.core.constants import STORAGE_SONGS_FOLDER, STORAGE_TEMP_THUMBNAILS_FOLDER
from src.core.database import data_manager
from src.core.database.models.song_model import Song
from src.core.exceptions import SongAlreadyExistsException, SongAlreadyInPlaylistException
from src.core.utils import os_utils, utils
from src.ui.widgets.dialog_box.dialog_box import DialogBox
from src.ui.widgets.youtube_video_card import styles


class YoutubeVideoCard(QWidget):
    def __init__(self, index, thumbnail_path, title, views, duration, video_id, video_url, parent=None):
        super(YoutubeVideoCard, self).__init__(parent)

        self.enterEvent = self.on_mouse_hover
        self.leaveEvent = self.on_mouse_leave

        self.video_id = video_id
        self.video_url = video_url
        self.index = index

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setSpacing(15)

        self.open_browser_button = QLabel(index)
        self.open_browser_button.setFixedWidth(25)
        self.open_browser_button.setFixedHeight(25)
        self.open_browser_button.setAlignment(Qt.AlignCenter)
        self.open_browser_button.enterEvent = lambda event: self.on_browser_icon_mouse_hover(event)
        self.open_browser_button.mousePressEvent = lambda event: web_browser.browse(self.video_url)

        self.video_thumbnail = QLabel()
        self.video_thumbnail.setFixedHeight(45)
        self.video_thumbnail.setFixedWidth(45)
        self.video_thumbnail.setScaledContents(True)
        if thumbnail_path is None:
            thumbnail_path = "assets/images/default_thumbnail.png"
        self.set_thumbnail_image(thumbnail_path)

        self.video_title = QLabel(title)
        self.video_title.setFixedHeight(45)
        self.video_title.setFixedWidth(500)

        self.video_views = QLabel(views)
        self.video_views.setFixedHeight(45)
        self.video_views.setFixedWidth(90)

        self.video_duration = QLabel(duration)
        self.video_duration.setFixedHeight(45)
        self.video_duration.setFixedWidth(85)

        self.add_song_button = QPushButton()
        self.add_song_button.setText("Add")
        self.add_song_button.setFixedHeight(40)
        self.add_song_button.setFixedWidth(100)
        self.add_song_button.setHidden(True)
        self.add_song_button.mousePressEvent = self.add_to_playlist_button_pressed

        self.allQHBoxLayout.addWidget(self.open_browser_button)
        self.allQHBoxLayout.addWidget(self.video_thumbnail)
        self.allQHBoxLayout.addWidget(self.video_title)
        self.allQHBoxLayout.addWidget(self.video_views)
        self.allQHBoxLayout.addWidget(self.video_duration)
        self.allQHBoxLayout.addWidget(self.add_song_button)
        self.setLayout(self.allQHBoxLayout)
        self.set_styles()

    def add_to_playlist_button_pressed(self, _):

        if self.already_exists():
            DialogBox(icon='warning', title='Info', message='This song is already in your playlist')
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            folder_path = f'{os.path.join(STORAGE_SONGS_FOLDER, self.video_id)}'
            file_path = f'{os.path.join(folder_path, self.video_id)}.mp3'

            # Download the video in MP3 format
            self.download_mp3()

            # Move the thumbnail to the same folder as the song
            temp_thumbnail_path = f'{os.path.join(STORAGE_TEMP_THUMBNAILS_FOLDER, self.video_id)}.jpg'
            os_utils.move_file(temp_thumbnail_path, folder_path)
            final_thumbnail_path = f'{os.path.join(folder_path, self.video_id)}.jpg'

            # Insert the data into the database
            song = Song(
                thumbnail_path=final_thumbnail_path,
                name=self.video_title.text(),
                duration_in_seconds=utils.get_duration_in_seconds(self.video_duration.text()),
                video_id=self.video_id,
                file_path=file_path
            )

            song_id = data_manager.insert_song(song)
            if song_id == -1:
                QApplication.restoreOverrideCursor()
                DialogBox(
                    icon='warning',
                    title='Error',
                    message=f'Something went wrong adding the song "{song.name}" to your playlist'
                )
                return

            try:
                data_manager.insert_song_into_playlist(playlist_id=1, song_id=song_id)
                QApplication.restoreOverrideCursor()
                DialogBox(
                    icon='success',
                    title='Ok',
                    message=f'The song "{self.video_title.text()}" has been successfully added to your playlist!'
                )
            except SongAlreadyInPlaylistException as e1:
                QApplication.restoreOverrideCursor()
                DialogBox(icon='information', title='Oops', message=e1.message)

        except SongAlreadyExistsException as e2:
            QApplication.restoreOverrideCursor()
            DialogBox(icon='danger', title='Oops', message=e2.message)

        except Exception as e3:
            QApplication.restoreOverrideCursor()
            DialogBox(
                icon='danger',
                title='Oops',
                message=f'Something went wrong adding the song to your playlist:\n{e3}')

        QApplication.restoreOverrideCursor()

    def download_mp3(self):
        try:
            yt = YouTube(self.video_url)
            video = yt.streams.filter(only_audio=True).first()
            file_name = self.video_id

            # Download the mp3 file and store it in the songs folder
            video.download(
                output_path=f'{os.path.join(STORAGE_SONGS_FOLDER, self.video_id)}',
                filename=f'{file_name}.mp3'
            )
        except Exception as e:
            print(e)
            raise Exception(e)

    def already_exists(self):
        folder = f'{os.path.join(STORAGE_SONGS_FOLDER, self.video_id)}'
        return os_utils.folder_exists(folder)

    def on_mouse_hover(self, _):
        pixmap_image = QPixmap("assets/images/browser.png")
        self.open_browser_button.setPixmap(pixmap_image)
        self.open_browser_button.setScaledContents(True)
        self.open_browser_button.setAlignment(Qt.AlignCenter)
        self.add_song_button.setHidden(False)

    def on_browser_icon_mouse_hover(self, _):
        self.open_browser_button.setCursor(QCursor(Qt.PointingHandCursor))

    def on_mouse_leave(self, _):
        self.open_browser_button.setText(str(self.index))
        self.add_song_button.setHidden(True)

    def set_styles(self):
        self.open_browser_button.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_thumbnail.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_title.setStyleSheet(styles.REGULAR_WHITE_TEXT_14)
        self.video_views.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.video_duration.setStyleSheet(styles.REGULAR_GRAY_TEXT_14)
        self.add_song_button.setStyleSheet(styles.ADD_BUTTON)

    def set_thumbnail_image(self, image_path):
        pix_map = QPixmap(image_path).scaled(45, 45)
        self.video_thumbnail.setPixmap(pix_map)

    def get_video_id(self):
        return self.video_id

    def get_video_url(self):
        return self.video_url
