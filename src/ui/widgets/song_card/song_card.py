import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QPushButton, QApplication, QMessageBox

from src.core.constants import STORAGE_SONGS_FOLDER
from src.core.database import data_manager
from src.core.utils import utils, os_utils
from src.ui.widgets.dialog_box.dialog_box import DialogBox
from src.ui.widgets.song_card import styles


class SongCard(QWidget):
    def __init__(
            self, id, index, name,
            date_added, duration, playlist_id, video_id,
            main_window_reference,
            thumbnail_path='assets/images/default_thumbnail.png',
            parent=None,
    ):
        super(SongCard, self).__init__(parent)

        self.main_window_reference = main_window_reference

        self.enterEvent = self.on_mouse_hover
        self.leaveEvent = self.on_mouse_leave

        self.id = id
        self.playlist_id = playlist_id
        self.video_id = video_id
        self.index = index
        self.song_thumbnail_path = thumbnail_path

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setSpacing(15)

        self.index_play_pause_button = QLabel(str(index))
        self.index_play_pause_button.setFixedWidth(25)
        self.index_play_pause_button.setFixedHeight(25)
        self.index_play_pause_button.setAlignment(Qt.AlignCenter)
        self.index_play_pause_button.enterEvent = self.on_index_play_pause_button_mouse_hover
        self.index_play_pause_button.mousePressEvent = self.play_pause_song

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
        self.remove_song_button.setText('Remove')
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

    def play_pause_song(self, _) -> None:
        if self.index != self.main_window_reference.audio_controller.current_song_index:
            self.main_window_reference.audio_controller.current_song_status.setText('Playing')
            self.main_window_reference.audio_controller.song_name.setText(self.song_name.text())
            self.main_window_reference.audio_controller.play(
                song_thumbnail_path=self.song_thumbnail_path,
                song_index=self.index, resume=False
            )
        else:
            if self.main_window_reference.audio_controller.playing:
                self.main_window_reference.audio_controller.current_song_status.setText('Paused')
                self.main_window_reference.audio_controller.pause()
            else:
                self.main_window_reference.audio_controller.current_song_status.setText('Playing')
                self.main_window_reference.audio_controller.song_name.setText(self.song_name.text())
                self.main_window_reference.audio_controller.play(
                    song_thumbnail_path=self.song_thumbnail_path,
                    song_index=self.index, resume=True
                )

    def remove_song_button_pressed(self, _) -> None:
        answer = QMessageBox.question(
            self,
            'Remove song',
            'Are you sure you want to remove this song from your playlist?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if answer == QMessageBox.No:
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            # Remove the song from the playlist
            data_manager.remove_song_from_playlist(playlist_id=self.playlist_id, song_id=self.id)

            # If the song is not linked to any playlists, remove it from the songs table as well
            song_removed_completely = data_manager.remove_song_if_not_in_any_playlist(song_id=self.id)

            if song_removed_completely:
                # Remove the song from the storage folder since we no longer need it
                os_utils.delete_folder(os.path.join(STORAGE_SONGS_FOLDER, self.video_id))

            QApplication.restoreOverrideCursor()
            DialogBox(
                icon='success',
                title='Ok',
                message=f'The song "{self.song_name.text()}" has been successfully REMOVED from your playlist!'
            )
        except Exception as e:
            print(e)
            QApplication.restoreOverrideCursor()
            DialogBox(
                icon='danger',
                title='Oops',
                message=f'Something went wrong removing the song from your playlist:\n{e}')
        QApplication.restoreOverrideCursor()
        self.main_window_reference.populate_songs_list(self.playlist_id)

    def on_mouse_hover(self, _) -> None:
        pixmap_image = QPixmap('assets/images/play_white.png')
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
