from usecases.UseCaseInterface import UseCaseInterface
from datetime import datetime
from api.Tankerkoenig import Tankerkoenig
from api.OpenWeather import OpenWeather
from api.GoogleCalendar import GoogleCalendar
from utils import Config, Voice
from datetime import datetime

class UseCase1(UseCaseInterface):
    def __init__(self, voice: Voice, config: Config):
        self.voice = voice
        self.config = config

    def run(self) -> None:
        current_time = datetime.now().strftime("%H:%M")
        self.voice.speak(
            f"Good morning. It's {current_time} o'clock and it's time to wake up."
        )
        
        # Google API
        events = GoogleCalendar.getCalenderEvents()
        if not events:
            self.voice.speak(
                f"You don't have any events today"
            )
        else:
            self.voice.speak(
                f"You first event today is {events[0]['summary']}. It starts at { datetime.fromisoformat(events[0]['start'].get('dateTime')).strftime('%H:%M') } o'clock and ends at { datetime.fromisoformat(events[0]['end'].get('dateTime')).strftime('%H:%M')}"
            )

        # Open weather API
        weatherInfo, currentTemp, minTemp, maxTemp = OpenWeather.getWeatherData(48.7833056999332, 9.166720315342262, self.config.get('WEATHER_API_KEY'))
        self.voice.speak(
            f"Now to the weather. The weather today is {weatherInfo} and the current temperature is {currentTemp}. The minimum temperature {minTemp} and the maximum temperature is {maxTemp}"
        )
        
        # Gas station recommendation
        self.voice.speak("All right. Do you want to know the cheapest gas station for today?")
        question_gastStation = self.voice.getUserConfirmation()
        if question_gastStation:            
            gasStation = Tankerkoenig.getGasStationData(48.7833056999332, 9.166720315342262, "e5", self.config.get('TANKERKOENIG_API_KEY')) 
            self.voice.speak(
                f"The cheapest gas station around you is from {gasStation['brand']} and cost {gasStation['price']} euro. The adress is {gasStation['street']} {gasStation['houseNumber']} in {gasStation['place']}"
            )

        self.voice.speak("That was all. I wish you a nice morning")
        
    def is_triggered(self) -> bool:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "22:59":
            return True
        else:
            return False
