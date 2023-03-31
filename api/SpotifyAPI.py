import logging
import time
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import CacheFileHandler
from spotipy.exceptions import SpotifyException


class SpotifyAPI():
    sp = None
    USERNAME = 'diepoldstr'
    CLIENT_ID = '927a5dd3a29a4c93808569a6056f3b66'
    CLIENT_SECRET = '870601bbddb34463a186f7524f2852dd'
    REDIRECT_URI = 'http://localhost:8888/callback'
    SCOPE = 'user-modify-playback-state'

    def __init__(self, config):
        self.sp = self.connectToSpotify()
        self.config = config

    def playDiningPlaylist(self):
        playlist_id = '37i9dQZF1DXbm6HfkbMtFZ'
        playing = False
        while not playing:
            try:
                self.sp.trace = False
                self.sp.shuffle(state=True)
                self.sp.start_playback(
                    device_id=None,
                    context_uri=f'spotify:playlist:{playlist_id}'
                )
                logging.info("Playing dining playlist...")
                playing = True
            except SpotifyException:
                logging.info("Open Spotify on your device and try again.")
                time.sleep(5)
                self.__init__(self.config)

    def connectToSpotify(self):
        auth_manager = SpotifyOAuth(
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            self.REDIRECT_URI,
            scope=self.SCOPE,
            # username=self.USERNAME
        )
        return spotipy.Spotify(auth_manager=auth_manager)
