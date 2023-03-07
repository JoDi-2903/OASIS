import json
import random
import urllib.request


class TMDB():
    def __init__(self):
        pass

    def genre_to_id(genre_str) -> int:
        tmdb_genre_codes = {
            "Action": 28,
            "Adventure": 12,
            "Animation": 16,
            "Comedy": 35,
            "Crime": 80,
            "Documentary": 99,
            "Drama": 18,
            "Family": 10751,
            "Fantasy": 14,
            "History": 36,
            "Horror": 27,
            "Music": 10402,
            "Mystery": 9648,
            "Romance": 10749,
            "Science Fiction": 878,
            "TV Movie": 10770,
            "Thriller": 53,
            "War": 10752,
            "Western": 37
        }
        return tmdb_genre_codes[genre_str]
    
    def recommend_random_movie(question_genre) -> dict:
        random_page_number = random.randint(1, 100)
        random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=5221e1317dbf91f51363a72bc6c98904&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(TMDB.genre_to_id(question_genre))) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]
        
        return random_movie