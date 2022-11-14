from src.core.youtube.youtube_video import YouTubeVideo
from youtubesearchpython import VideosSearch


def search_for_videos(search_string):
    try:
        result = VideosSearch(search_string, limit=10).result().get('result')
    except Exception as e:
        print(e)
        raise Exception(e)

    return [
        YouTubeVideo(
            id=data['id'],
            url=data['link'],
            thumbnail_url=data['thumbnails'][0]['url'],
            title=data['title'],
            views=int((data['viewCount']['text']).replace(' views', '').replace(',', '')),
            views_extense=data['viewCount']['short'],
            duration=data['duration']
        ) for data in result]
