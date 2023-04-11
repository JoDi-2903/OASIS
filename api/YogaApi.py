import json
import random
import urllib.request

class YogaApi():
    def __init__(self):
        pass

    def get_random_yoga_exercise() -> dict:
        with urllib.request.urlopen("https://yoga-api-nzy4.onrender.com/v1/poses") as url:
            yoga_exercises = json.load(url)
            exercise_recommendation = yoga_exercises[random.randrange(0, len(yoga_exercises))]
        return exercise_recommendation