from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from APIRequest import APIRequest
import os


class WeatherAPI:

    def __init__(self):
        self.read_api_key_from_env()
        self.json = {}

    def load_weather(self,city="Stockholm"):
        #TODO : Implement the logic
        print("City is : ", city)
        WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?appid="+str(self.api_key)+"&q="+city+"&aqi=yes"      
        print(WEATHER_URL)

        try:
            apiRequestObj = APIRequest()
            self.json = apiRequestObj.get_json(WEATHER_URL)
            print(self.json)
        except:
            print("An Exception Occured")

        return  self.json


    def print_sunset(self,data):

        from datetime import datetime, timezone, timedelta

        sunrise_timestamp = data["sys"]["sunrise"]
        sunset_timestamp = data["sys"]["sunset"]
        timezone_offset = data["timezone"]

        local_tz = timezone(timedelta(seconds=timezone_offset))

        sunrise = datetime.fromtimestamp(sunrise_timestamp, tz=local_tz)
        sunset = datetime.fromtimestamp(sunset_timestamp, tz=local_tz)

        print("Sunrise:", sunrise.strftime("%H:%M"))
        print("Sunset:", sunset.strftime("%H:%M"))

    def read_api_key_from_env(self):
        load_dotenv(find_dotenv())
        self.api_key = os.getenv("API_KEY")

        return self.api_key is not None