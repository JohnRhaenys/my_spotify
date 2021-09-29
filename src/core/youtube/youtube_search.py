import typing

from src.core.youtube.youtube_video import YouTubeVideo
from youtubesearchpython import VideosSearch


def search_for_videos(search_string: str) -> typing.List[YouTubeVideo]:
    videos = []
    try:
        result = VideosSearch(search_string, limit=10).result().get('result')

        for data in result:
            video_id = data['id']
            video_url = data['link']
            thumbnail_url = data['thumbnails'][0]['url']
            title = data['title']
            views = int((data['viewCount']['text']).replace(' views', '').replace(',', ''))
            views_extense = data['viewCount']['short']
            duration = data['duration']

            youtube_video = YouTubeVideo(
                id=video_id,
                url=video_url,
                thumbnail_url=thumbnail_url,
                title=title,
                views=views,
                views_extense=views_extense,
                duration=duration
            )
            videos.append(youtube_video)
    except Exception as e:
        raise Exception(e)

    return videos
