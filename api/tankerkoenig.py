import requests

class Tankerkoenig():

    def getGasStationData() -> dict:
        url = "https://creativecommons.tankerkoenig.de/json/list.php?lat=48.78330569993326&lng=9.166720315342262&rad=2&sort=price&type=e5&apikey=c831ea13-3104-5cbe-0896-950187d5bc0d"
        response = requests.get(url).json()
        #df = pd.DataFrame.from_dict(response.get('stations'))
        #for i in df.index:
         #   if(df['price'][i] < dfLowestPrice['price']):
         #       dfLowestPrice = df.iloc[i]
        lowest = None
        for station in response['stations']:
            if lowest:
                if lowest['price'] > station['price']:
                    lowest = station
            else:
                lowest = station
        return lowest

