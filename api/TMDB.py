import json
import random
import urllib.request


class TMDB():
    # Definition of the genre codes from TMDB
    genre_codes = {
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

    def __init__(self):
        pass

    def genre_to_id(question_genre) -> int:
        # Detect genre from user input
        for gnr in TMDB.genre_codes:
            if gnr in question_genre.lower():
                return TMDB.genre_codes[gnr]
        # Genre could not be detected
        return 0 
    
    def id_to_genre(genre_id) -> str:
        inverted_genre_codes = {v: k for k, v in TMDB.genre_codes.items()}
        return inverted_genre_codes[genre_id]
    
    def recommend_random_movie(genre_id) -> dict:
        random_page_number = random.randint(1, 100)
        random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=5221e1317dbf91f51363a72bc6c98904&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(genre_id)) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]
        
        return random_movie