from usecases.UseCaseInterface import UseCaseInterface
from api.YogaApi import YogaApi
from api.ZenQuotes import ZenQuotes

#Use case for midday health routine, containing:
#   Inspirational quote (https://docs.zenquotes.io/zenquotes-documentation/#call-today)
#   Yoga or fitness exercise (https://yoga-api-nzy4.onrender.com/v1/poses)
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)

class UseCase2(UseCaseInterface):
    def __init__(self, voice):
        self.voice = voice

    def run(self) -> None:
        routine_text = "Good afternoon. This is your health routine. First, your daily Zen Quote: "
        routine_text += self.get_zen_quote()
        routine_text += " We'll continue with an exercise.  "
        routine_text += self.get_fitness_exercise()
        routine_text += " Now to your health information. Do you want to hear it?"
        self.voice.speak(routine_text)
        
        print(routine_text)

    def is_triggered(self) -> bool:
        pass

    def get_fitness_exercise(self) -> str:
        yoga_exercise = YogaApi.get_random_yoga_exercise()
        return_string = "Your daily Yoga exercise is " + yoga_exercise['english_name'] + ". "
        return_string += " The benefits are: " + yoga_exercise['pose_benefits'] + ". "
        return_string += "The description: " + yoga_exercise['pose_description']
        return return_string

    def get_zen_quote(self) -> str:
        zen_quote = ZenQuotes.get_daily_quote()
        return_string = zen_quote['a'] + " once said: "
        return_string += zen_quote['q']
        return return_string

test = UseCase2()
test.run()