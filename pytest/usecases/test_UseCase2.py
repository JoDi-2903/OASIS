from datetime import datetime
import validators
from api.FitBit import FitBitApi
from api.YogaApi import YogaApi
from api.ZenQuotes import ZenQuotes
from usecases.UseCase2 import UseCase2 

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

def test_yoga_api_random_exercise_id():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['id'] != ''

def test_yoga_api_random_exercise_sanskrit_name_adapted():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['sanskrit_name_adapted'] != ''

def test_yoga_api_random_exercise_sanskrit_name():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['sanskrit_name'] != ''

def test_yoga_api_random_exercise_translation_name():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['translation_name'] != ''

def test_yoga_api_random_exercise_url_svg():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['url_svg'] != ''

def test_yoga_api_random_exercise_url_png():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['url_png'] != ''

def test_yoga_api_random_exercise_url_svg_alt():
    exercise = YogaApi.get_random_yoga_exercise()
    assert exercise['url_svg_alt'] != ''


# --- test ZenQuotesAPI ---
def test_zen_quotes_daily_quote_quote():
    quote = ZenQuotes.get_daily_quote()
    assert quote['q'] != ''

def test_zen_quotes_daily_quote_author():
    quote = ZenQuotes.get_daily_quote()
    assert quote['a'] != ''

def test_zen_quotes_daily_quote_formatted_text():
    quote = ZenQuotes.get_daily_quote()
    assert quote['h'] != ''

# --- test UseCase2 ---
def test_usecase2_trigger2():
    trigger_2 = UseCase2.is_triggered(UseCase2)
    trigger_test = False
    if datetime.now().strftime("%H:%M") == "15:00": trigger_test = True
    assert trigger_test == trigger_2

def test_usecase2_get_fitness_exercise():
    exercise = UseCase2.get_fitness_exercise(UseCase2)
    assert exercise != ''

def test_usecase2_get_zen_quote():
    quote = UseCase2.get_zen_quote(UseCase2)
    assert quote != ''

def test_usecase2_convert_pounds_to_kg():
    pounds = 10
    kilo = UseCase2.convert_pounds_to_kg(UseCase2, pounds)
    assert kilo == 4.54

def test_usecase2_convert_pounds_to_kg_0():
    pounds = 0
    kilo = UseCase2.convert_pounds_to_kg(UseCase2, pounds)
    assert kilo == 0

def test_usecase2_convert_pounds_to_kg_minus():
    pounds = -10
    kilo = UseCase2.convert_pounds_to_kg(UseCase2, pounds)
    assert kilo == -4.54
