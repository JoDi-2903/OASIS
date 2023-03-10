import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAPI():
    sp = None
    USERNAME = 'diepoldstr'
    CLIENT_ID = '927a5dd3a29a4c93808569a6056f3b66'
    CLIENT_SECRET = '870601bbddb34463a186f7524f2852dd'
    REDIRECT_URI = 'http://localhost:8888/callback'
    SCOPE = 'user-modify-playback-state'

    def __init__(self):
        auth_manager = SpotifyOAuth(
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            self.REDIRECT_URI,
            scope=self.SCOPE,
            username=self.USERNAME
        )
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

    def playDiningPlaylist(self):
        playlist_id = '37i9dQZF1DXbm6HfkbMtFZ'

        # token = util.prompt_for_user_token(username)
        token = util.prompt_for_user_token(
            username=self.USERNAME,
            scope=self.SCOPE,
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            redirect_uri=self.REDIRECT_URI
        )

        if token:
            self.sp.trace = False
            self.sp.start_playback(
                device_id=None, context_uri=f'spotify:playlist:{playlist_id}'
            )
            print("Playing dining playlist...")
        else:
            print("Can't get token for", self.USERNAME)
