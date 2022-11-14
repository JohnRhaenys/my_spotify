from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget

from src.ui import colors
from src.ui.widgets.playlist_card import styles


class PlaylistCard(QWidget):
    def __init__(self, id, name, parent=None):
        super(PlaylistCard, self).__init__(parent)
        self.allQHBoxLayout = QHBoxLayout()

        self.id = id

        self.name = QLabel()
        self.name.setMaximumSize(QSize(150, 25))
        self.name.setAlignment(Qt.AlignLeft)

        self.name.enterEvent = self.on_mouse_hover
        self.name.leaveEvent = self.on_mouse_leave

        self.allQHBoxLayout.addWidget(self.name)
        self.setLayout(self.allQHBoxLayout)

        self.set_name(name)
        self.set_styles()

    def set_focus(self):
        self.name.setStyleSheet(f"color: {colors.WHITE}")

    def remove_focus(self):
        self.name.setStyleSheet(f"color: {colors.GRAY}")

    def on_mouse_hover(self, _):
        self.set_focus()

    def on_mouse_leave(self, _):
        self.remove_focus()

    def set_styles(self):
        self.name.setStyleSheet(styles.GRAY_TEXT)

    def set_name(self, value):
        self.name.setText(value)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name.text()
