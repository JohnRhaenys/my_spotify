from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QHBoxLayout


class ListWidget(QWidget):
    def __init__(self, items=None, parent=None):
        super(ListWidget, self).__init__(parent)
        if items is None:
            items = []
        layout = QHBoxLayout()
        self.items = items
        self.list = QListWidget(self)
        layout.addWidget(self.list)
        self.set_styles()
        self.setLayout(layout)
        self.set_items(self.items)

    def set_styles(self):
        pass

    def set_thumbnail_image(self, image_path):
        self.video_thumbnail.setPixmap(QPixmap(image_path))

    def set_items(self, items):
        self.clear()
        if all(isinstance(item, str) for item in items):
            self.list.addItems(items)
        else:
            for item in items:
                widget_item = QListWidgetItem(self.list)
                widget_item.setSizeHint(item.sizeHint())
                self.list.addItem(widget_item)
                self.list.setItemWidget(widget_item, item)

    def clear(self):
        self.list.clear()
