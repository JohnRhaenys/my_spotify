import os

from pytube import YouTube
from youtubesearchpython import Video
from youtubesearchpython.internal.constants import ResultMode


def download_video_in_mp3(video_url, filename, destination_folder=os.getcwd()):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=destination_folder, filename=filename)
        return True
    except Exception as e:
        print(e)
        return False


def get_video_information(video_url):
    info = {}
    video = Video.get(video_url, mode=ResultMode.json)
    info['id'] = video.get('id')
    info['title'] = video.get('title')
    return info


def get_video_id(video_url):
    key = '?v='
    return video_url[video_url.rfind(key) + len(key):]
