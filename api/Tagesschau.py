import json
import urllib.request


class Tagesschau():
    def __init__(self):
        pass

    def get_tagesschau_100_seconds_url() -> str:
        with urllib.request.urlopen("https://www.tagesschau.de/api/multimedia/video/ondemand100~_type-video.json") as url:
            news_data = json.load(url)
            tagesschau_video_url = news_data["videos"][0]["mediadata"][0]["h264s"]
        
        return tagesschau_video_url