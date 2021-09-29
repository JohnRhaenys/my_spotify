from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QSizePolicy

from src.ui.main_window import styles


class Slider(QWidget):
    def __init__(
            self, min_width, max_width, default_value=0,
            orientation=Qt.Horizontal, style=styles.SLIDER, parent=None):
        super(Slider, self).__init__(parent)
        layout = QHBoxLayout()
        self.slider = QSlider(self)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())

        self.slider.setSizePolicy(sizePolicy)
        self.slider.setMinimumSize(QSize(min_width, 0))
        self.slider.setMaximumSize(QSize(max_width, 16777215))
        self.slider.setOrientation(orientation)
        self.set_value(default_value)

        if style is not None:
            self.set_style(style)

        layout.addWidget(self.slider)
        self.setLayout(layout)

    def set_style(self, style) -> None:
        self.slider.setStyleSheet(style)

    def get_value(self) -> int:
        return self.slider.value()

    def set_value(self, value) -> None:
        self.slider.setValue(value)
