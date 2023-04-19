import requests
import re


class Recipe:
    def __init__(self, title, summary, link):
        self.title = title
        self.summary = summary
        self.link = link


class SpoonacularAPI():
    def getRecipeList(config):
        payload = {
            'fillIngredients': False,
            'limitLicense': False,
            # 'number': 1,
            # 'ranking': 1,
            'tags': 'main course' + config.get("diet")
        }

        api_key = config.get("SPOONACULAR_KEY")

        headers = {
            'content-type': 'application/json',
            'X-Mshape-Key': api_key,
            'X-Mashape-Host': 'mashape host'
        }
        endpoint = "https://api.spoonacular.com/recipes/random?apiKey=" + api_key

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
