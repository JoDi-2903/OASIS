import validators
from api.FitBit import FitBitApi
from api.YogaApi import YogaApi
from api.ZenQuotes import ZenQuotes
from usecases.UseCase2 import UseCase2 

# --- test FitbitAPI ---

# --- test YogaApi ---
def test_yoga_api_random_exercise_english_name():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['english_name'] != ''

def test_yoga_api_random_exercise_pose_benefits():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['pose_benefits'] != ''

def test_yoga_api_random_exercise_pose_description():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['pose_description'] != ''

# --- test ZenQuotesAPI ---
def test_zen_quotes_daily_quote_quote():
    quote = ZenQuotes.get_daily_quote()
    assert quote['q'] != ''

def test_zen_quotes_daily_quote_author():
    quote = ZenQuotes.get_daily_quote()
    assert quote['a'] != ''

# --- test UseCase2 ---