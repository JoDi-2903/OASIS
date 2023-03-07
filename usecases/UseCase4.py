from usecases.UseCaseInterface import UseCaseInterface
from datetime import datetime
import urllib.request
import json
import vlc
import time


class UseCase4(UseCaseInterface):
    def __init__(self):
        pass

    def run() -> None:
        # News Report
        ## Wish a good evening and tell the current time
        current_time = datetime.now().strftime("%H:%M")
        print(f"Good evening. It's {current_time} o'clock. Here is your news summary of the day.")
        
        ## Play the user the news of the day
        with urllib.request.urlopen("https://www.tagesschau.de/api/multimedia/video/ondemand100~_type-video.json") as url:
            news_data = json.load(url)
            tagesschau_video_url = news_data["videos"][0]["mediadata"][0]["h264s"]
        
            media_player = vlc.MediaPlayer()
            media_player.set_media(vlc.Media(tagesschau_video_url))
            media_player.play()
        
            time.sleep(5)
            while media_player.is_playing():
                time.sleep(2)

        # Movie recommendation

        # Cocktail recommendation


        pass

    def is_triggered() -> bool:
        pass
