from PyQt5.QtCore import Qt
from src.ui.widgets.playlist_card.playlist_card import PlaylistCard


def construct_item_data(item) -> dict:
    data = {'classname': item.__class__.__name__}
    if isinstance(item, PlaylistCard):
        data['data'] = {'id': item.get_id(), 'name': item.get_name()}
    return data


def fetch_item_data(item) -> dict:
    item_info = item.data(Qt.UserRole)
    return item_info
