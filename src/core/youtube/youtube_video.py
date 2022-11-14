import os
import requests
from src.core.constants import STORAGE_TEMP_THUMBNAILS_FOLDER


class YouTubeVideo:
    def __init__(self, id, url, thumbnail_url, title, views, views_extense, duration):
        self.id = id
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.views = views
        self.views_extense = views_extense
        self.duration = duration

    def __repr__(self):
        return f'<YouTubeVideo:' \
               f' id=[{self.id}], ' \
               f'url=[{self.url}], ' \
               f'thumbnail_url=[{self.thumbnail_url}], ' \
               f'title=[{self.title}],' \
               f' views=[{self.views}], ' \
               f' views_extense=[{self.views_extense}], ' \
               f'duration=[{self.duration}]> '

    def download_thumbnail(self):
        try:
            response = requests.get(self.thumbnail_url)
            if response.ok:
                path = f'{os.path.join(STORAGE_TEMP_THUMBNAILS_FOLDER, self.id)}.jpg'
                file = open(path, 'wb')
                file.write(response.content)
                file.close()
                return path
            else:
                return None
        except Exception as e:
            print(e)
            return None
