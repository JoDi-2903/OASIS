import requests

class Tankerkoenig():

    def getGasStationData(lat, lon, gasType) -> dict:
        url = "https://creativecommons.tankerkoenig.de/json/list.php?lat=" + str(lat)  + "&lng=" + str(lon)  +"&rad=2&sort=price&type=" + gasType +"&apikey=c831ea13-3104-5cbe-0896-950187d5bc0d"
        response = requests.get(url).json()
        lowest = None
        for station in response['stations']:
            if lowest:
                if lowest['price'] > station['price']:
                    lowest = station
            else:
                lowest = station
        return lowest

