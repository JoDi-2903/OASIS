import validators
from api.Tankerkoenig import Tankerkoenig
from api.OpenWeather import OpenWeather
from api.GoogleCalendar import GoogleCalendar

# --- Tankerkoenig ---

def test_with_e5_gas():
    gasStation = Tankerkoenig.getGasStationData(48.7833056999332, 9.166720315342262, "e5")   
    assert gasStation is not None

def test_with_e10_gas():
    gasStation = Tankerkoenig.getGasStationData(48.7833056999332, 9.166720315342262, "e10")   
    assert gasStation is not None

def test_with_diesel_gas():
    gasStation = Tankerkoenig.getGasStationData(48.7833056999332, 9.166720315342262, "diesel")   
    assert gasStation is not None

def test_all_station_fields_filled():
    gasStation = Tankerkoenig.getGasStationData(48.7833056999332, 9.166720315342262, "e5") 
    assert gasStation['brand'] != ''
    assert gasStation['price'] > 0
    assert gasStation['street'] != ''
    assert gasStation['houseNumber'] != ''
    assert gasStation['place'] != ''

# --- OpenWeather ---
def test_getWeatherData():
    assert OpenWeather.getWeatherData(48.7833056999332, 9.166720315342262) is not None

def test_WeatherData():
    weatherInfo, currentTemp, minTemp, maxTemp =  OpenWeather.getWeatherData(48.7833056999332, 9.166720315342262)
    assert weatherInfo != ''
    assert minTemp < 100 and minTemp > -50
    assert currentTemp < 100 and currentTemp > -50
    assert maxTemp < 100 and maxTemp > -50

# --- GoogleCalendar ---
