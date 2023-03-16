import http.client
import json
import webbrowser
import geocoder
import requests


class Restaurant():
    def __init__(self, name, description, latitude, longitude):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Restaurant: {self.latitude}, {self.longitude}"


class TripAdvisorAPI():
    def __init__(self):
        pass

    def getRestaurantList():
        conn = http.client.HTTPSConnection("travel-advisor.p.rapidapi.com")
        latitude, longitude = get_location()
        radius = 0.1
        payload = {
            "geoId": 293928,
            "partySize": 2,
            "reservationTime": "2022-03-07T20:00",
            "sort": "POPULARITY",
            "sortOrder": "desc",
            "filters": [
                {
                    "id": "establishment",
                    "value": [
                        "10591"
                    ]
                }
            ],
            "boundingBox": {
                "northEastCorner": {
                    "latitude": latitude + radius,
                    "longitude": longitude + radius
                },
                "southWestCorner": {
                    "latitude": latitude - radius,
                    "longitude": longitude - radius
                }
            },
            "updateToken": ""
        }

        headers = {
            'content-type': "application/json",
            'X-RapidAPI-Key': "419a62092amsh70be100a5b4e0f2p161fbfjsnb9d9a7cd6452",
            'X-RapidAPI-Host': "travel-advisor.p.rapidapi.com"
        }

        conn.request("POST", "/restaurants/v2/list?lang=en_US",
                     json.dumps(payload), headers)

        res = conn.getresponse()
        data = res.read()
        sections = json.loads(data.decode(
            "utf-8"))['data']['AppPresentation_queryAppListV2'][0]
        restaurants = []
        section_index = 0
        pin_index = 0

        while (len(restaurants) < 10):
            if ('listSingleCardContent' in sections['sections'][section_index]):
                temp_restaurant = sections['sections'][section_index]['listSingleCardContent']
                pin = sections['mapSections'][0]['pins'][pin_index]['geoPoint']
                restaurants.append(
                    Restaurant(temp_restaurant['cardTitle']['string'], format_restaurant_description(temp_restaurant['primaryInfo']['text']), pin['latitude'], pin['longitude']))
                pin_index += 1
            section_index += 1

        return restaurants


def get_directions(restaurant: Restaurant) -> str:
    starting_lat, starting_lng = get_location()

    ending_lat = restaurant.latitude
    ending_lng = restaurant.longitude

    # Format the URL with the coordinates
    return f'https://www.google.com/maps/dir/{starting_lat},{starting_lng}/{ending_lat},{ending_lng}/'


def get_location():
    # Get the user's IP address
    ip = requests.get('https://api.ipify.org').text

    # Use IP-API to get the user's restaurant
    g = geocoder.ip(ip)

    return g.latlng[0], g.latlng[1]


def format_restaurant_description(description: str) -> str:
    temp_description = description.split('•')
    price_ranges = {
        '$$ - $$$ ': "medium expensive",
        '$': "very cheap",
        '$$': "cheap",
        '$$$': "expensive",
        '$$$$': "very expensive",
    }
    for key in price_ranges:
        if (temp_description[0].startswith(key)):
            temp_description[0] = price_ranges[key]
            break
    return ','.join(temp_description)
