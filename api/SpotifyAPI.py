import logging
import time
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import CacheFileHandler
from spotipy.exceptions import SpotifyException


class SpotifyAPI():
    sp = None
    REDIRECT_URI = 'http://localhost:8888/callback'
    SCOPE = 'user-modify-playback-state'

    def __init__(self, config):
        self.config = config
        self.USERNAME = self.config.get('SPOTIFY_USERNAME')
        self.CLIENT_ID = self.config.get('SPOTIFY_CLIENT_ID')
        self.CLIENT_SECRET = self.config.get('SPOTIFY_CLIENT_SECRET')
        self.playlist_id = self.config.get('playlist_id')
        self.sp = self.connectToSpotify()

    def playDiningPlaylist(self):
        playing = False
        while not playing:
            try:
                self.startPlayback()
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

    def startPlayback(self):
        self.sp.trace = False
        self.sp.shuffle(state=True)
        self.sp.start_playback(
            device_id=None,
            context_uri=f'spotify:playlist:{self.playlist_id}'
        )
        logging.info("Playing dining playlist...")
