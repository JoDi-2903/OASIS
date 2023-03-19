import json
import requests

url = "https://forecast9.p.rapidapi.com/rapidapi/forecast/48.78296637144953/9.166677400021946/summary/"

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "forecast9.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

response.get('forecast').get('items')[0].get('weather').get('text')

print(response.text)

