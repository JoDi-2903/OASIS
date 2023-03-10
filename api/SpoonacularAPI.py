import requests


class SpoonacularAPI():
    def __init__(self):
        pass

    def getRecipeList():
        payload = {
            'fillIngredients': False,
            'limitLicense': False,
            'number': 5,
            'ranking': 1
        }

        api_key = "df9facedb801488cb9ddbef142853b21"

        headers = {
            'content-type': 'application/json',
            'X-Mshape-Key': api_key,
            'X-Mashape-Host': 'mashape host'
        }
        endpoint = "https://api.spoonacular.com/recipes/random?apiKey=" + api_key

        req = requests.get(endpoint, params=payload, headers=headers)
        return req.json()
