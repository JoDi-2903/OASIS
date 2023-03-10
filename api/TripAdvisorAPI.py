import http.client
import json


class TripAdvisorAPI():
    def __init__(self):
        pass

    def getRestaurantList(latitude, longitude, radius=0.1):
        conn = http.client.HTTPSConnection("travel-advisor.p.rapidapi.com")

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

        return json.loads(data.decode("utf-8"))
