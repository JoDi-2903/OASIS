import json
import random
import urllib.request


class TheCocktailDB():
    def recommend_random_cocktail(question_alcohol) -> dict:
        max_elements = 99 if question_alcohol else 57
        random_element_number = random.randint(0, max_elements)

        with urllib.request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?a="+("Alcoholic" if question_alcohol else "Non_Alcoholic")) as url:
            tcdb_data = json.load(url)
            random_cocktail_id = tcdb_data["drinks"][random_element_number]["idDrink"]

        with urllib.request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+str(random_cocktail_id)) as url:
            tcdb_data = json.load(url)
            random_cocktail = tcdb_data["drinks"][0]

        cocktail_ingredient = []
        for i in range(1, 16):
            if random_cocktail['strMeasure'+str(i)] and random_cocktail['strIngredient'+str(i)]:
                cocktail_ingredient.append(random_cocktail['strMeasure'+str(i)] + random_cocktail['strIngredient'+str(i)])
            elif random_cocktail['strIngredient'+str(i)]:
                cocktail_ingredient.append(random_cocktail['strIngredient'+str(i)])
            else:
                cocktail_ingredient_str = ', '.join(cocktail_ingredient)
                cocktail_ingredient_str = ' and '.join(
                    cocktail_ingredient_str.rsplit(', ', 1))
                random_cocktail['ingredient_str'] = cocktail_ingredient_str
                break

        return random_cocktail
