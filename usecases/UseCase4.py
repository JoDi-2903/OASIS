from usecases.UseCaseInterface import UseCaseInterface
from datetime import datetime
import urllib.request
import json
import vlc
import time
import random


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
        ## Ask the user what movie genre they are in the mood for today
        print("So much for the latest news. What genre of movie are you in the mood for today?")
        question_genre = "28"

        ## Give the user a movie recommendation
        random_page_number = random.randint(1, 100)
        random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=5221e1317dbf91f51363a72bc6c98904&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(question_genre)) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]
        
        print(f"Good choice! From the genre {question_genre} I recommend you today the movie {random_movie['title']} released in {random_movie['release_date'][:4]}. The film currently has an average rating of {random_movie['vote_average']} with {random_movie['vote_count']} reviews. I will now give you a brief plot overview: {random_movie['overview']}")

        # Cocktail recommendation
        ## Ask the user if he wants to have a cocktail with the movie
        print("May I recommend you a cocktail with the movie?")
        question_cocktail = True
        
        ## Give the user a cocktail recommendation
        if question_cocktail:
            print("All right. Should the cocktail contain alcohol?")
            question_alcohol = True

            max_elements = 99 if question_alcohol else 57
            random_element_number = random.randint(0, max_elements)
        
            with urllib.request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?a="+("Alcoholic" if question_alcohol else "Non_Alcoholic")) as url:
                tcdb_data = json.load(url)
                random_cocktail_id = tcdb_data["drinks"][random_element_number]["idDrink"]
        
            with urllib.request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+str(random_cocktail_id)) as url:
                tcdb_data = json.load(url)
                random_cocktail = tcdb_data["drinks"][0]
        
            cocktail_ingredient = []
            for i in range(1, 16):
                if random_cocktail['strIngredient'+str(i)]:
                    cocktail_ingredient.append(random_cocktail['strMeasure'+str(i)] + random_cocktail['strIngredient'+str(i)])
                else:
                    cocktail_ingredient_str = ', '.join(cocktail_ingredient)
                    cocktail_ingredient_str = ' and '.join(cocktail_ingredient_str.rsplit(', ', 1))
                    break
                
            print(f"As cocktail of the day I recommend {random_cocktail['strDrink']}. For this you need {cocktail_ingredient_str}. Now to the preparation: {random_cocktail['strInstructions']}")
        else:
            print("Okay. Have a great movie night.")

    def is_triggered() -> bool:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "20:00":
            return True
        else:
            return False
