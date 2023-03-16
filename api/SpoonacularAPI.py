import requests
import re


class Recipe:
    def __init__(self, title, summary, link):
        self.title = title
        self.summary = summary
        self.link = link


class SpoonacularAPI():
    def __init__(self):
        pass

    def getRecipeList():
        payload = {
            'fillIngredients': False,
            'limitLicense': False,
            # 'number': 1,
            # 'ranking': 1,
            'tags': 'main course'
        }

        api_key = "df9facedb801488cb9ddbef142853b21"

        headers = {
            'content-type': 'application/json',
            'X-Mshape-Key': api_key,
            'X-Mashape-Host': 'mashape host'
        }
        endpoint = "https://api.spoonacular.com/recipes/random?apiKey=" + api_key

        courses = ['main course', 'lunch', 'main dish']

        req = requests.get(endpoint, params=payload, headers=headers)
        recipe = req.json()['recipes'][0]

        return Recipe(recipe['title'], cleanup_recipe_summary(recipe['summary']), recipe['sourceUrl'])


def cleanup_recipe_summary(recipe_summary):
    recipe_summary = re.sub(r"<.*?>", "", recipe_summary)
    index = recipe_summary.rfind(". ", 0, -3)

    if index != -1:
        return recipe_summary[:index]
    else:
        return recipe_summary
