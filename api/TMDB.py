import json
import random
import urllib.request


class TMDB():
    def __init__(self):
        pass

    def genre_to_id(question_genre) -> int:
        tmdb_genre_codes = {
            "action": 28,
            "adventure": 12,
            "animation": 16,
            "comedy": 35,
            "crime": 80,
            "documentary": 99,
            "drama": 18,
            "family": 10751,
            "fantasy": 14,
            "history": 36,
            "horror": 27,
            "music": 10402,
            "mystery": 9648,
            "romance": 10749,
            "science Fiction": 878,
            "tv movie": 10770,
            "thriller": 53,
            "war": 10752,
            "western": 37
        }
        return tmdb_genre_codes[question_genre.lower()]
    
    def recommend_random_movie(question_genre) -> dict:
        random_page_number = random.randint(1, 100)
        random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=5221e1317dbf91f51363a72bc6c98904&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(TMDB.genre_to_id(question_genre))) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]
        
        return random_movie