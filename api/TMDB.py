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
        "science fiction": 878,
        "tv movie": 10770,
        "thriller": 53,
        "war": 10752,
        "western": 37
    }

    # Definition of the watch_provider codes from TMDB
    watch_provider_codes = {
        "Amazon Prime Video": 9,
        "Apple TV Plus": 350,
        "Disney Plus": 337,
        "Paramount Plus": 531,
        "Netflix": 8
    }

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
    
    def watch_provider_to_id(watch_providers) -> str:
        watch_provider_codes = []
        
        for wp in watch_providers:
            if wp in TMDB.watch_provider_codes:
                watch_provider_codes.append(str(TMDB.watch_provider_codes[wp]))

        return '|'.join(watch_provider_codes)
    
    def recommend_random_movie(api_key, genre_id) -> dict:
        random_page_number = random.randint(1, 100)
        random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key="+str(api_key)+"&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(genre_id)) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]

        return random_movie
    
    def recommend_random_movie_by_watch_provider(api_key, genre_id, watch_providers) -> dict:
        watch_providers_dict = watch_providers.split(", ")
        watch_provider_params = "&with_watch_providers="+TMDB.watch_provider_to_id(watch_providers_dict)+"&watch_region=DE&with_watch_monetization_types=flatrate"

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key="+str(api_key)+"&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&with_genres="+str(genre_id)+str(watch_provider_params)) as url:
            tmdb_data = json.load(url)
            total_pages = tmdb_data["total_pages"]
            total_results = tmdb_data["total_results"]

        random_page_number = random.randint(1, total_pages)
        # There are 20 movies on a full page. But the last page is not necessarily complete.
        if random_page_number == total_pages:
            random_element_number = random.randint(0, (total_results%20)-1)
        else:
            random_element_number = random.randint(0, 19)

        with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key="+str(api_key)+"&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(random_page_number)+"&with_genres="+str(genre_id)+str(watch_provider_params)) as url:
            tmdb_data = json.load(url)
            random_movie = tmdb_data["results"][random_element_number]

        return random_movie
