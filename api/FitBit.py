import api.gather_keys_oauth2 as Oauth2
import fitbit
import datetime

#   using modules: fitbit and cherrypy, installed by requirements.txt
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)
class FitBitApi():
    CLIENT_ID = ''
    CLIENT_SECRET = ''

    def __init__(self, CLIENT_ID, CLIENT_SECRET):
        self.authorize_with_api()
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET

    def get_health_status(self) -> dict:
        date = datetime.date.today().strftime("%Y-%m-%d")
        sleepData = self.auth2_client.sleep(date=date)
        foodData = self.auth2_client.recent_foods()
        bodyWeight = self.auth2_client.get_bodyweight()
        bodyWeightGoal = self.auth2_client.body_weight_goal()
        return {
            'bodyweight': bodyWeight,
            'bodyweightgoal': bodyWeightGoal,
            'sleepdata': sleepData,
            'fooddata': foodData 
        }

    def authorize_with_api(self):
        server=Oauth2.OAuth2Server(self.CLIENT_ID, self.CLIENT_SECRET)
        server.browser_authorize()
        ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
        self.auth2_client=fitbit.Fitbit(self.CLIENT_ID,self.CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)
