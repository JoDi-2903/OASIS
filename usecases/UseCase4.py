from usecases.UseCaseInterface import UseCaseInterface
from api.Tagesschau import Tagesschau
from api.TMDB import TMDB
from api.TheCocktailDB import TheCocktailDB
from datetime import datetime
import vlc
import time


class UseCase4(UseCaseInterface):
    def __init__(self):
        pass

    def run() -> None:
        # 01 News Report
        # Wish a good evening and tell the current time
        current_time = datetime.now().strftime("%H:%M")
        output_str = "Good evening. It's " + current_time + " o'clock. Here is your news summary of the day."
        print(output_str)

        # Play the user the news of the day
        tagesschau_video_url = Tagesschau.get_tagesschau_100_seconds_url()

        #*** TMP: Output function for audio files ***
        media_player = vlc.MediaPlayer()
        media_player.set_media(vlc.Media(tagesschau_video_url))
        media_player.play()

        time.sleep(5)
        while media_player.is_playing():
            time.sleep(1)
        #*********************************************

        # 02 Movie recommendation
        # Ask the user what movie genre they are in the mood for today
        output_str = "So much for the latest news. What genre of movie are you in the mood for today?"
        print(output_str)
        question_genre = "Action"

        # Give the user a movie recommendation
        random_movie = TMDB.recommend_random_movie(question_genre)
        output_str = "Good choice! From the genre " + question_genre + " I recommend you today the movie " + random_movie['title'] + " released in " + random_movie['release_date'][:4] + ". The film currently has an average rating of " + random_movie['vote_average'] + " with " + random_movie['vote_count'] + "reviews. I will now give you a brief plot overview: " + random_movie['overview']
        print(output_str)

        # 03 Cocktail recommendation
        # Ask the user if he wants to have a cocktail with the movie
        output_str = "May I recommend you a cocktail with the movie?"
        print(output_str)
        question_cocktail = True
        
        # Give the user a cocktail recommendation
        if question_cocktail:
            output_str = "All right. Should the cocktail contain alcohol?"
            print(output_str)
            question_alcohol = True

            random_cocktail = TheCocktailDB.recommend_random_cocktail(question_alcohol)
            output_str = "As cocktail of the day I recommend " + random_cocktail['strDrink'] + ". For this you need " + random_cocktail['ingredient_str'] + ". Now to the preparation: " + random_cocktail['strInstructions']
            print(output_str)
        else:
            output_str = "Okay. Have a great movie night."
            print(output_str)

    def is_triggered() -> bool:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "20:00":
            return True
        else:
            return False
