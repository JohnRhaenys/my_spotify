import os
from pytube import YouTube


def download_video_in_mp3(video_url, filename, destination_folder=os.getcwd()):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=destination_folder, filename=f'{filename}.mp3')
        return True
    except Exception as e:
        print(e)
        return False
