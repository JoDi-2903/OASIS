import api.gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
import datetime


CLIENT_ID = '23QT56'
CLIENT_SECRET = '05ddc878df29ec251ffa5e1801abe0c5'

#   using modules: fitbit and cherrypy, installed by requirements.txt
#   health information (https://dev.fitbit.com/build/reference/web-api/developer-guide/)
class FitBitApi():
    def __init__(self):
        self.authorize_with_api()

    def get_health_status(self) -> dict:
        date = datetime.date(year=2023, month=3, day=16)
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
        server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
        server.browser_authorize()
        ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
        self.auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)


#FitBitApi().get_health_status()