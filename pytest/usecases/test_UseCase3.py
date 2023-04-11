import os
import pytest

from spotipy.exceptions import SpotifyException

from api.SpoonacularAPI import SpoonacularAPI, cleanup_recipe_summary, Recipe
from api.TripAdvisorAPI import TripAdvisorAPI, get_directions, format_restaurant_description, get_location, Restaurant
from api.SpotifyAPI import SpotifyAPI
from utils import Config


def get_usecase3_config():
    config = Config()
    config.set("diet", "")
    config.set("playlist_id", "37i9dQZF1DXbm6HfkbMtFZ")
    config.set("SPOTIFY_USERNAME", os.getenv("SPOTIFY_USERNAME"))
    config.set("SPOTIFY_CLIENT_ID", os.getenv("SPOTIFY_CLIENT_ID"))
    config.set("SPOTIFY_CLIENT_SECRET", os.getenv("SPOTIFY_CLIENT_SECRET"))
    config.set("SPOONACULAR_KEY", os.getenv("SPOONACULAR_KEY"))
    config.set("RAPIDAPI_KEY", os.getenv("RAPIDAPI_KEY"))
    return config


# --- TripAdvisorAPI ---

def test_cleanup_recipe_summary_edge_cases():
    testString = "<p>This is a <b>test</b> string.</p> This is the end of the string that should not be included."
    assert cleanup_recipe_summary(
        testString) == "This is a test string"


def test_getRecipeList():
    assert SpoonacularAPI.getRecipeList(get_usecase3_config()) is not None


def test_recipe_class():
    test_recipe = Recipe("Test title", "Test summary", "https://example.com")
    assert test_recipe.title == "Test title"
    assert test_recipe.summary == "Test summary"
    assert test_recipe.link == "https://example.com"


# --- SpotifyAPI ---

def test_spotifyAuth():
    spotify = SpotifyAPI(get_usecase3_config())
    token = spotify.connectToSpotify()
    assert token is not None


def test_spotify_no_active_device():
    with pytest.raises(SpotifyException) as exc_info:
        spotify = SpotifyAPI(get_usecase3_config())
        spotify.startPlayback()

    assert exc_info.value.http_status == 404
    assert "Player command failed: No active device found" in str(
        exc_info.value)


# --- TripAdvisorAPI ---

def test_restaurant_class():
    test_restaurant = Restaurant(
        "Test name", "Test description", 48.782536, 9.176995)
    assert test_restaurant.name == "Test name"
    assert test_restaurant.description == "Test description"
    assert test_restaurant.latitude == 48.782536
    assert test_restaurant.longitude == 9.176995


def test_get_directions():
    assert get_directions(
        Restaurant("test name", "This is a description", 48.782536, 9.176995)) is not None


def test_get_location():
    assert get_location() is not None


def test_format_restaurant_description_edge_cases():
    test_description = "$$ - $$$ • This is a test title • This is a test description"
    assert format_restaurant_description(
        test_description) == "medium expensive, This is a test title , This is a test description"


def test_getRestaurantList():
    restaurantList = TripAdvisorAPI.getRestaurantList(get_usecase3_config())
    assert restaurantList is not None and len(restaurantList) > 0
