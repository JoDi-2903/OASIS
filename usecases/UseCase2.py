from usecases.UseCaseInterface import UseCaseInterface
import http.client


#Use case for midday health routine, containing:
#   Inspirational quote (https://docs.zenquotes.io/zenquotes-documentation/#call-today)
#   Yoga or fitness exercise (some exercise)
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)
class UseCase2(UseCaseInterface):
    def __init__(self):
        print('tewst')
        pass

    def run(self) -> None:
        self.get_fitness_excercise()

    def is_triggered(self) -> bool:
        pass

    def get_fitness_excercise(self) -> None:
        conn = http.client.HTTPSConnection("https://api.api-ninjas.com/v1/")

        headers = {
            'X-RapidAPI-Key': "6f4dd6f642msh16d8ee2b9cb9552p118908jsn8d1f88a21ff3",
            'X-RapidAPI-Host': "exercisedb.p.rapidapi.com"
            }

        conn.request("GET", "/exercises/exercise/1739", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

#Idee: https://api-ninjas.com/api/exercises


test = UseCase2()
test.run()