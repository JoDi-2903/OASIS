import logging
import webbrowser

from usecases.UseCaseInterface import UseCaseInterface
from api.SpoonacularAPI import SpoonacularAPI
from api.SpotifyAPI import SpotifyAPI
from api.TripAdvisorAPI import TripAdvisorAPI, get_directions
from utils import Config, Voice


class UseCase3(UseCaseInterface):
    def __init__(self, voice: Voice, config: Config):
        self.voice = voice
        self.config = config

    def run(self) -> None:
        self.voice.speak("Do you want to cook today?")

        if self.voice.getUserConfirmation():
            is_chosen_recipe = False
            is_init = True
            # show recipes
            logging.info("Getting recipe...")
            while (not is_chosen_recipe):
                recipe = SpoonacularAPI.getRecipeList()
                if is_init:
                    temp_promt = "Here is a recipe I found"
                    is_init = False
                else:
                    temp_promt = "Here is another recipe I found"

                self.voice.speak(
                    f"{temp_promt}: {recipe.title}. Do you want to hear the summary?")
                if self.voice.getUserConfirmation():
                    self.voice.speak(
                        "Okay, here is the summary." + recipe.summary)

                self.voice.speak("Do you want to cook this one?")
                if self.voice.getUserConfirmation():
                    is_chosen_recipe = True

            self.voice.speak(
                "Do you want me to open the recipe in your browser?")
            if self.voice.getUserConfirmation():
                webbrowser.open_new_tab(recipe.link)

            self.voice.speak("Do you want to listen to music while cooking?")
            if self.voice.getUserConfirmation():
                # play spotify playlist
                spotify = SpotifyAPI(self.config)
                spotify.playDiningPlaylist()
        else:
            # show restaurants
            restaurants = TripAdvisorAPI.getRestaurantList()
            is_init = True
            is_chosen_restaurant = False

            for restaurant in restaurants:
                if (is_init):
                    temp_promt = "Here is a restaurant I found: "
                    is_init = False
                else:
                    temp_promt = "What about "
                self.voice.speak(temp_promt + restaurant.name +
                                 ". Do you want to hear the description?")
                if self.voice.getUserConfirmation():
                    self.voice.speak(
                        "Okay, here is the description." + restaurant.description)

                self.voice.speak("Do you want to go to this restaurant?")
                if self.voice.getUserConfirmation():
                    is_chosen_restaurant = True
                    break

            if (is_chosen_restaurant):
                self.voice.speak(
                    "Do you want me to open the restaurant directions in your browser?")
                if self.voice.getUserConfirmation():
                    webbrowser.open_new_tab(get_directions(restaurants[0]))
            else:
                self.voice.speak(
                    "You are way to picky today. I guess you'll just starve. Goodbye.")

    def is_triggered(self) -> bool:
        return True
        answer = self.voice.hear()
        if ("it's lunchtime" in answer or
            "it's lunch time" in answer or
            "it's dinnertime" in answer or
            "it's dinner time" in answer or
                "it's time to eat" in answer):
            return True
        return False
