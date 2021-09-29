from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QHBoxLayout

from src.ui.widgets.list_widget import item_data_manager
from src.ui.widgets.playlist_card.playlist_card import PlaylistCard


class ListWidget(QWidget):
    def __init__(self, main_window_reference, items=None, parent=None):
        super(ListWidget, self).__init__(parent)

        self.main_window_reference = main_window_reference

        if items is None:
            items = []

        layout = QHBoxLayout()

        self.items = items
        self.list = QListWidget(self)
        layout.addWidget(self.list)
        self.setLayout(layout)

        self.set_items(self.items)
        self.set_styles()
        self.set_listeners()

    def set_styles(self):
        pass

    def set_listeners(self):
        self.list.itemClicked.connect(self.item_clicked)

    def set_thumbnail_image(self, image_path):
        self.video_thumbnail.setPixmap(QPixmap(image_path))

    def set_items(self, items):
        self.clear()
        if all(isinstance(item, str) for item in items):
            self.list.addItems(items)
        else:
            for item in items:
                q_list_item = QListWidgetItem(self.list)
                q_list_item.setSizeHint(item.sizeHint())

                self.list.addItem(q_list_item)
                self.list.setItemWidget(q_list_item, item)

                data = item_data_manager.construct_item_data(item)
                q_list_item.setData(Qt.UserRole, data)

    def item_clicked(self, item):
        item_info = item_data_manager.fetch_item_data(item)
        if item_info['classname'] == PlaylistCard.__name__:
            playlist_id = item_info['data']['id']
            self.main_window_reference.populate_songs_list(playlist_id=playlist_id)

    def clear(self):
        self.list.clear()
