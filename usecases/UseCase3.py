from usecases.UseCaseInterface import UseCaseInterface
from api.TripAdvisorAPI import TripAdvisorAPI
from api.SpoonacularAPI import SpoonacularAPI
from api.SpotifyAPI import SpotifyAPI


class UseCase3(UseCaseInterface):
    def __init__(self):
        pass

    def run(self) -> None:
        # ask wether the user wants to cook or not
        cook = True
        if cook:
            # show recipes
            # print(SpoonacularAPI.getRecipeList())

            # play dining music
            spotify = SpotifyAPI()
            spotify.playDiningPlaylist()
            pass
        else:
            # show restaurants
            print(TripAdvisorAPI.getRestaurantList(48.774511, 9.172553))

    def is_triggered(self) -> bool:
        pass
