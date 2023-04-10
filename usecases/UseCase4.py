from usecases.UseCaseInterface import UseCaseInterface
from api.Tagesschau import Tagesschau
from api.TMDB import TMDB
from api.TheCocktailDB import TheCocktailDB
from datetime import datetime
from utils import Config, Voice


class UseCase4(UseCaseInterface):
    def __init__(self, voice: Voice, config: Config):
        self.voice = voice
        self.config = config

    def run(self) -> None:
        # 01 News Report
        # Wish a good evening and tell the current time
        current_time = datetime.now().strftime("%H:%M")
        self.voice.speak(
            f"Good evening, {self.config.get('name')}. It's {current_time} o'clock. Here is your news summary of the day."
        )

        # Play the user the news of the day
        tagesschau_video_url = Tagesschau.get_tagesschau_100_seconds_url()
        self.voice.play(tagesschau_video_url)

        # 02 Movie recommendation
        # Ask the user what movie genre they are in the mood for today
        self.voice.speak(
            "So much for the latest news. What genre of movie are you in the mood for today?"
        )
        question_genre = self.voice.hear()
        genre_id = TMDB.genre_to_id(question_genre)

        while genre_id == 0:
            self.voice.speak(
                "Sorry, I didn't understand that. Please repeat your choice.")
            question_genre = self.voice.hear()
            genre_id = TMDB.genre_to_id(question_genre)

        # Read movie_providers from config file and give the user a movie recommendation
        if self.config.get('watch_providers'):
            random_movie = TMDB.recommend_random_movie_by_watch_provider(self.config.get('TMDB_API_KEY'), genre_id, self.config.get('watch_providers'))
        else:
            random_movie = TMDB.recommend_random_movie(self.config.get('TMDB_API_KEY'), genre_id)
        
        self.voice.speak(
            f"Good choice! From the genre {TMDB.id_to_genre(genre_id)} I recommend you today the movie {random_movie['title']} released in {random_movie['release_date'][:4]}. The film currently has an average rating of {random_movie['vote_average']} with {random_movie['vote_count']} reviews. I will now give you a brief plot overview: {random_movie['overview']}"
        )

        # 03 Cocktail recommendation
        # Ask the user if he wants to have a cocktail with the movie
        self.voice.speak("May I recommend you a cocktail with the movie?")
        question_cocktail = self.voice.getUserConfirmation()
        # Give the user a cocktail recommendation
        if question_cocktail:
            self.voice.speak("All right. Should the cocktail contain alcohol?")
            question_alcohol = self.voice.getUserConfirmation()

            random_cocktail = TheCocktailDB.recommend_random_cocktail(
                question_alcohol
            )
            self.voice.speak(
                f"As cocktail of the day I recommend {random_cocktail['strDrink']}. For this you need {random_cocktail['ingredient_str']}. Now to the preparation: {random_cocktail['strInstructions']}")
        else:
            self.voice.speak(f"Okay. Have a great movie night, {self.config.get('name')}.")

    def is_triggered(self) -> bool:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == self.config.get('starttime_usecase_4'):
            return True
        else:
            return False
