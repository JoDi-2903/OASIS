import requests


class OpenWeather():

    def getWeatherData(lat, lon, api_key):        
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" +  str(lat) +"&lon=" + str(lon) +"&appid=" + api_key
        response = requests.get(url).json()
        weatherInfo = response["weather"][0]["main"]
        currentTemp = int(response["main"]["temp"] - 273.15)
        minTemp = int(response["main"]["temp_min"] - 273.15)
        maxTemp = int(response["main"]["temp_max"] - 273.15)
        return weatherInfo, currentTemp, minTemp, maxTemp


