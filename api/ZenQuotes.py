import json
import random
import urllib.request


class ZenQuotes():
    def __init__(self):
        pass

    # dict, where 'q' is quote and 'a' is the author
    def get_daily_quote() -> dict:
        with urllib.request.urlopen("https://zenquotes.io/api/today") as url:
            quote = json.load(url)
        return quote[0]
