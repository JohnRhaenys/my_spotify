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
    def __init__(self, song, card_index, playlist_id, main_window_reference, parent=None):
        super(SongCard, self).__init__(parent)

        # CONTROL VARIABLES --------------------------------------------------------------
        self.song = song
        self.index = card_index
        self.playlist_id = playlist_id
        self.main_window_reference = main_window_reference

        # FRONT-END LAYOUT VARIABLES --------------------------------------------------------------
        self.enterEvent = self.on_mouse_hover
        self.leaveEvent = self.on_mouse_leave

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setSpacing(15)

        self.index_play_pause_button = QLabel(str(card_index))
        self.index_play_pause_button.setFixedWidth(25)
        self.index_play_pause_button.setFixedHeight(25)
        self.index_play_pause_button.setAlignment(Qt.AlignCenter)
        self.index_play_pause_button.enterEvent = self.on_index_play_pause_button_mouse_hover
        self.index_play_pause_button.mousePressEvent = self.play_pause_song
        self.index_play_pause_button.setScaledContents(True)
        self.index_play_pause_button.setAlignment(Qt.AlignCenter)

        self.song_thumbnail = QLabel()
        self.song_thumbnail.setFixedHeight(45)
        self.song_thumbnail.setFixedWidth(45)
        self.song_thumbnail.setScaledContents(True)
        self.set_thumbnail_image(self.song.thumbnail_path)

        self.song_name = QLabel(str(self.song.name))
        self.song_name.setFixedHeight(45)
        self.song_name.setFixedWidth(600)

        self.date_added = QLabel(str(utils.date_formatter(str(self.song.created_at))))
        self.date_added.setFixedHeight(45)
        self.date_added.setFixedWidth(90)

        self.song_duration = QLabel(utils.time_formatter(self.song.duration_in_seconds))
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
                song=data_manager.get_song(self.song.id),
                song_index=self.index,
                resume=False
            )
        else:
            if self.main_window_reference.audio_controller.playing:
                self.main_window_reference.audio_controller.current_song_status.setText('Paused')
                self.main_window_reference.audio_controller.pause()
                pixmap_image = QPixmap('assets/images/play_white.png')
                self.main_window_reference.audio_controller.switch_play_pause_button_icon('play')
            else:
                self.main_window_reference.audio_controller.current_song_status.setText('Playing')
                self.main_window_reference.audio_controller.song_name.setText(self.song_name.text())
                self.main_window_reference.audio_controller.play(
                    song=data_manager.get_song(self.song.id),
                    song_index=self.index,
                    resume=not self.main_window_reference.audio_controller.first_time
                )
                pixmap_image = QPixmap('assets/images/pause_white.png')
                self.main_window_reference.audio_controller.switch_play_pause_button_icon('pause')
            self.index_play_pause_button.setPixmap(pixmap_image)
        self.main_window_reference.audio_controller.song_total_time.setText(self.song_duration.text())

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
            data_manager.remove_song_from_playlist(playlist_id=self.playlist_id, song_id=self.song.id)

            # If the song is not linked to any playlists, remove it from the songs table as well
            song_removed_completely = data_manager.remove_song_if_not_in_any_playlist(song_id=self.song.id)

            if song_removed_completely:
                # Delete the song from the storage folder since we no longer need it
                path = os.path.join(STORAGE_SONGS_FOLDER, self.song.video_id)
                os_utils.delete_folder(directory_path=path)

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
        if self.index == self.main_window_reference.audio_controller.current_song_index:
            if self.main_window_reference.audio_controller.playing:
                pixmap_image = QPixmap('assets/images/pause_white.png')
            else:
                pixmap_image = QPixmap('assets/images/play_white.png')
        else:
            pixmap_image = QPixmap('assets/images/play_white.png')

        self.index_play_pause_button.setPixmap(pixmap_image)
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
