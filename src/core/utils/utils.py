def get_youtube_video_id(video_url):
    key = '?v='
    return video_url[video_url.rfind(key) + len(key):]
