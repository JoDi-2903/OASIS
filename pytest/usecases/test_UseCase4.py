import validators
from api.Tagesschau import Tagesschau
from api.TMDB import TMDB
from api.TheCocktailDB import TheCocktailDB
from usecases.UseCase4 import UseCase4
from datetime import datetime


# API - Tagesschau
def test_tagesschau_url():
   tagesschau_video_url = Tagesschau.get_tagesschau_100_seconds_url()
   assert validators.url(tagesschau_video_url)


# API - TMDB
# genre_to_id()
def test_genre_to_id_action():
   genre_code = TMDB.genre_to_id("action")
   assert genre_code == 28

def test_genre_to_id_adventure():
   genre_code = TMDB.genre_to_id("adventure")
   assert genre_code == 12

def test_genre_to_id_animation():
   genre_code = TMDB.genre_to_id("animation")
   assert genre_code == 16

def test_genre_to_id_comedy():
   genre_code = TMDB.genre_to_id("comedy")
   assert genre_code == 35

def test_genre_to_id_crime():
   genre_code = TMDB.genre_to_id("crime")
   assert genre_code == 80

def test_genre_to_id_documentary():
   genre_code = TMDB.genre_to_id("documentary")
   assert genre_code == 99

def test_genre_to_id_drama():
   genre_code = TMDB.genre_to_id("drama")
   assert genre_code == 18

def test_genre_to_id_family():
   genre_code = TMDB.genre_to_id("family")
   assert genre_code == 10751

def test_genre_to_id_fantasy():
   genre_code = TMDB.genre_to_id("fantasy")
   assert genre_code == 14

def test_genre_to_id_history():
   genre_code = TMDB.genre_to_id("history")
   assert genre_code == 36

def test_genre_to_id_horror():
   genre_code = TMDB.genre_to_id("horror")
   assert genre_code == 27

def test_genre_to_id_music():
   genre_code = TMDB.genre_to_id("music")
   assert genre_code == 10402

def test_genre_to_id_mystery():
   genre_code = TMDB.genre_to_id("mystery")
   assert genre_code == 9648

def test_genre_to_id_romance():
   genre_code = TMDB.genre_to_id("romance")
   assert genre_code == 10749

def test_genre_to_id_science_fiction():
   genre_code = TMDB.genre_to_id("science fiction")
   assert genre_code == 878

def test_genre_to_id_tv_movie():
   genre_code = TMDB.genre_to_id("tv movie")
   assert genre_code == 10770

def test_genre_to_id_thriller():
   genre_code = TMDB.genre_to_id("thriller")
   assert genre_code == 53

def test_genre_to_id_war():
   genre_code = TMDB.genre_to_id("war")
   assert genre_code == 10752

def test_genre_to_id_western():
   genre_code = TMDB.genre_to_id("western")
   assert genre_code == 37

def test_genre_to_id_action():
   genre_code = TMDB.genre_to_id("AcTIon")
   assert genre_code == 28

def test_genre_to_id_action():
   genre_code = TMDB.genre_to_id(" action ")
   assert genre_code == 28

def test_genre_to_id_action():
   genre_code = TMDB.genre_to_id("action, please")
   assert genre_code == 28

def test_genre_to_id_error():
   genre_code = TMDB.genre_to_id("")
   assert genre_code == 0

def test_genre_to_id_error():
   genre_code = TMDB.genre_to_id("lorem ipsum")
   assert genre_code == 0


# id_to_genre()
def test_id_to_genre_28():
   genre_string = TMDB.id_to_genre(28)
   assert genre_string == "action"

def test_id_to_genre_12():
   genre_string = TMDB.id_to_genre(12)
   assert genre_string == "adventure"

def test_id_to_genre_16():
   genre_string = TMDB.id_to_genre(16)
   assert genre_string == "animation"

def test_id_to_genre_35():
   genre_string = TMDB.id_to_genre(35)
   assert genre_string == "comedy"

def test_id_to_genre_80():
   genre_string = TMDB.id_to_genre(80)
   assert genre_string == "crime"

def test_id_to_genre_99():
   genre_string = TMDB.id_to_genre(99)
   assert genre_string == "documentary"

def test_id_to_genre_18():
   genre_string = TMDB.id_to_genre(18)
   assert genre_string == "drama"

def test_id_to_genre_10751():
   genre_string = TMDB.id_to_genre(10751)
   assert genre_string == "family"

def test_id_to_genre_14():
   genre_string = TMDB.id_to_genre(14)
   assert genre_string == "fantasy"

def test_id_to_genre_36():
   genre_string = TMDB.id_to_genre(36)
   assert genre_string == "history"

def test_id_to_genre_27():
   genre_string = TMDB.id_to_genre(27)
   assert genre_string == "horror"

def test_id_to_genre_10402():
   genre_string = TMDB.id_to_genre(10402)
   assert genre_string == "music"

def test_id_to_genre_9648():
   genre_string = TMDB.id_to_genre(9648)
   assert genre_string == "mystery"

def test_id_to_genre_10749():
   genre_string = TMDB.id_to_genre(10749)
   assert genre_string == "romance"

def test_id_to_genre_878():
   genre_string = TMDB.id_to_genre(878)
   assert genre_string == "science fiction"

def test_id_to_genre_10770():
   genre_string = TMDB.id_to_genre(10770)
   assert genre_string == "tv movie"

def test_id_to_genre_53():
   genre_string = TMDB.id_to_genre(53)
   assert genre_string == "thriller"

def test_id_to_genre_10752():
   genre_string = TMDB.id_to_genre(10752)
   assert genre_string == "war"

def test_id_to_genre_37():
   genre_string = TMDB.id_to_genre(37)
   assert genre_string == "western"

# watch_provider_to_id()
def test_watch_provider_to_id_1():
   watch_provider_codes = TMDB.watch_provider_to_id(["Netflix"])
   assert watch_provider_codes == "8"

def test_watch_provider_to_id_2():
   watch_provider_codes = TMDB.watch_provider_to_id(["Netflix", "Disney Plus"])
   assert watch_provider_codes == "8|337"

def test_watch_provider_to_id_5():
   watch_provider_codes = TMDB.watch_provider_to_id(["Apple TV Plus", "Amazon Prime Video", "Paramount Plus", "Disney Plus", "Netflix"])
   assert watch_provider_codes == "350|9|531|337|8"

# recommend_random_movie()
def test_recommend_random_movie_title():
   random_movie = TMDB.recommend_random_movie("5221e1317dbf91f51363a72bc6c98904", 28)
   assert random_movie['title'] != ""

def test_recommend_random_movie_release_date():
   random_movie = TMDB.recommend_random_movie("5221e1317dbf91f51363a72bc6c98904", 12)
   assert validators.between(int(random_movie['release_date'][:4]), min=1750, max=2050)

def test_recommend_random_movie_vote_average():
   random_movie = TMDB.recommend_random_movie("5221e1317dbf91f51363a72bc6c98904", 16)
   assert validators.between(float(random_movie['vote_average']), min=0.0, max=10.0)

def test_recommend_random_movie_vote_count():
   random_movie = TMDB.recommend_random_movie("5221e1317dbf91f51363a72bc6c98904", 35)
   assert validators.between(int(random_movie['vote_count']), min=0)

def test_recommend_random_movie_overview():
   random_movie = TMDB.recommend_random_movie("5221e1317dbf91f51363a72bc6c98904", 80)
   assert random_movie['overview'] != ""

# recommend_random_movie_by_watch_provider()
def test_recommend_random_movie_title_N():
   random_movie = TMDB.recommend_random_movie_by_watch_provider("5221e1317dbf91f51363a72bc6c98904", 28, "Netflix")
   assert random_movie['title'] != ""

def test_recommend_random_movie_title_A():
   random_movie = TMDB.recommend_random_movie_by_watch_provider("5221e1317dbf91f51363a72bc6c98904", 12, "Apple TV Plus")
   assert random_movie['title'] != ""

def test_recommend_random_movie_title_NDA():
   random_movie = TMDB.recommend_random_movie_by_watch_provider("5221e1317dbf91f51363a72bc6c98904", 99, "Netflix, Disney Plus, Amazon Prime Video")
   assert random_movie['title'] != ""

# API - TheCocktailDB
def test_recommend_random_cocktail_alcoholic_strDrink():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(True)
   assert random_cocktail['strDrink'] != ""

def test_recommend_random_cocktail_alcoholic_ingredient_str():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(True)
   assert random_cocktail['ingredient_str'] != ""

def test_recommend_random_cocktail_alcoholic_strInstructions():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(True)
   assert random_cocktail['strInstructions'] != ""

def test_recommend_random_cocktail_non_alcoholic_strDrink():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(False)
   assert random_cocktail['strDrink'] != ""

def test_recommend_random_cocktail_non_alcoholic_ingredient_str():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(False)
   assert random_cocktail['ingredient_str'] != ""

def test_recommend_random_cocktail_non_alcoholic_strInstructions():
   random_cocktail = TheCocktailDB.recommend_random_cocktail(False)
   assert random_cocktail['strInstructions'] != ""


# UseCase4 - isTriggered()
def test_trigger4():
   trigger_4 = UseCase4.is_triggered(UseCase4)
   trigger_test = False 
   if datetime.now().strftime("%H:%M") == "20:00": trigger_test = True
   assert trigger_test == trigger_4
