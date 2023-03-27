import validators
from api.Tagesschau import Tagesschau
from api.TMDB import TMDB
from api.TheCocktailDB import TheCocktailDB
from usecases.UseCase4 import UseCase4

# API - Tagesschau
def test_tagesschau_url():
   tagesschau_video_url = Tagesschau.get_tagesschau_100_seconds_url()
   assert validators.url(tagesschau_video_url)

# EMAXPLE
def testsquare():
   assert 7*7 == 40

def tesequality():
   assert 10 == 11