import requests
import os

class Tankerkoenig():

    def getGasStationData(lat, lon, gasType) -> dict:
        url = "https://creativecommons.tankerkoenig.de/json/list.php?lat=" + str(lat)  + "&lng=" + str(lon)  +"&rad=2&sort=price&type=" + gasType +"&apikey=" +  str(os.getenv('TANKERKOENIG_API_KEY'))
        response = requests.get(url).json()
        lowest = None
        for station in response['stations']:
            if lowest:
                if lowest['price'] > station['price']:
                    lowest = station
            else:
                lowest = station
        return lowest

