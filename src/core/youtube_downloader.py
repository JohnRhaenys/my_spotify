from pytube import YouTube
import os

from src.core.utils import utils


def download_mp3(video_url, destination_folder=os.getcwd()):
    yt = YouTube(video_url)

    video = yt.streams.filter(only_audio=True).first()

    downloaded_file_path = video.download(destination_folder)

    separator = os.path.sep
    refactored_file_path = downloaded_file_path[:downloaded_file_path.rfind(separator)]
    video_id = utils.get_youtube_video_id(video_url)

    new_file_path = f'{refactored_file_path}{separator}{video_id}.mp3'

    os.rename(downloaded_file_path, new_file_path)
