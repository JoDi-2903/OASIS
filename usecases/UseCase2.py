from usecases.UseCaseInterface import UseCaseInterface
from api.YogaApi import YogaApi


#Use case for midday health routine, containing:
#   Inspirational quote (https://docs.zenquotes.io/zenquotes-documentation/#call-today)
#   Yoga or fitness exercise (https://yoga-api-nzy4.onrender.com/v1/poses)
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)
class UseCase2(UseCaseInterface):
    def __init__(self):
        pass

    def run(self) -> None:
        self.get_fitness_exercise()

    def is_triggered(self) -> bool:
        pass

    def get_fitness_exercise(self) -> None:
        yoga_exercise = YogaApi.get_random_yoga_exercise()



test = UseCase2()
test.run()