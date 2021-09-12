from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget


class QCustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.allQHBoxLayout = QHBoxLayout()

        self.index_add_to_playlist_button = QLabel()
        self.video_thumbnail = QLabel()
        self.video_title = QLabel()
        self.video_views = QLabel()
        self.video_likes = QLabel()
        self.video_duration = QLabel()

        self.allQHBoxLayout.addWidget(self.index_add_to_playlist_button)
        self.allQHBoxLayout.addWidget(self.video_thumbnail)
        self.allQHBoxLayout.addWidget(self.video_title)
        self.allQHBoxLayout.addWidget(self.video_views)
        self.allQHBoxLayout.addWidget(self.video_duration)
        self.setLayout(self.allQHBoxLayout)

    def set_styles(self):
        pass

    def setTextUp (self, text):
        self.index_add_to_playlist_button.setText(text)

    def setTextDown (self, text):
        self.video_thumbnail.setText(text)

    def setIcon (self, imagePath):
         pass
         #self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))