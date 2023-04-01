import json
import requests

class OpenWeather():

    def __init__(self):
        pass

    def getWeatherData():        
        url = "https://api.openweathermap.org/data/2.5/weather?lat=48.7833056999332&lon=9.166720315342262&appid=4a4c9909084f86cec6007e0c8cb5880f"

        response = requests.get(url).json()
        weatherInfo = response["weather"][0]["main"]
        currentTemp = int(response["main"]["temp"] - 273.15)
        minTemp = int(response["main"]["temp_min"] - 273.15)
        maxTemp = int(response["main"]["temp_max"] - 273.15)
        return weatherInfo, currentTemp, minTemp, maxTemp


