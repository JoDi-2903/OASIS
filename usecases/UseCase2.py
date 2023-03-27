import datetime
from usecases.UseCaseInterface import UseCaseInterface
from api.YogaApi import YogaApi
from api.ZenQuotes import ZenQuotes
from api.FitBit import FitBitApi
from utils import Config, Voice
# Use case for midday health routine, containing:
#   Inspirational quote (https://docs.zenquotes.io/zenquotes-documentation/#call-today)
#   Yoga or fitness exercise (https://yoga-api-nzy4.onrender.com/v1/poses)
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)


class UseCase2(UseCaseInterface):
    def __init__(self, voice: Voice, config: Config):
        self.voice = voice
        self.config = config

    def run(self) -> None:
        self.get_fitness_status()
        routine_text = "Good afternoon. This is your health routine. First, your daily Zen Quote: "
        routine_text += self.get_zen_quote()
        routine_text += " We'll continue with an exercise.  "
        routine_text += self.get_fitness_exercise()
        routine_text += " Now to your health information. Do you want to hear it?"
        self.voice.speak(routine_text)

        if self.voice.getUserConfirmation():
            routine_text = " Ok, here is your health status: "
            routine_text += self.get_fitness_status()
        else:
            routine_text = " I understand, the health status is skipped today. "
        routine_text += " The routine is over, you did a great job! Enjoy your afternoon."

        self.voice.speak(routine_text)

    def is_triggered(self) -> bool:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "15:00":
            return True
        else:
            return False

    def get_fitness_status(self) -> str:
        fitness_status = FitBitApi().get_health_status()
        weight = self.convert_pounds_to_kg(
            fitness_status['bodyweight']['weight'][0]['weight'])
        weight_goal = self.convert_pounds_to_kg(
            fitness_status['bodyweightgoal']['goal']['weight'])
        weight_goal_difference = weight - weight_goal
        return_string = "Your recent weight is " + str(weight) + ". "
        return_string += " Your weight goal is  " + str(weight_goal) + ". "
        return_string += " The difference between your goal and your weight is " + \
            str(round(weight_goal_difference, 2)) + ". "
        return return_string

    def get_fitness_exercise(self) -> str:
        yoga_exercise = YogaApi.get_random_yoga_exercise()
        return_string = "Your daily Yoga exercise is " + \
            yoga_exercise['english_name'] + ". "
        return_string += " The benefits are: " + \
            yoga_exercise['pose_benefits'] + ". "
        return_string += "The description: " + \
            yoga_exercise['pose_description']
        return return_string

    def get_zen_quote(self) -> str:
        zen_quote = ZenQuotes.get_daily_quote()
        return_string = zen_quote['a'] + " once said: "
        return_string += zen_quote['q']
        return return_string

    def convert_pounds_to_kg(self, pounds) -> float:
        return (round((pounds / 2.205), 2))
