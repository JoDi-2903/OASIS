import json
import random
import urllib.request


class ZenQuotes():
    def __init__(self):
        pass

    def get_random_quote(self) -> dict:
        with urllib.request.urlopen("https://zenquotes.io/api/quotes") as url:
            list_of_quotes = json.load(url)
            zen_quote = list_of_quotes[random.randrange(0, len(list_of_quotes))]
        return zen_quote

    # dict, where 'q' is quote and 'a' is the author
    def get_daily_quote() -> dict:
        with urllib.request.urlopen("https://zenquotes.io/api/today") as url:
            quote = json.load(url)
        return quote[0]

#print(ZenQuotes().get_random_quote())  