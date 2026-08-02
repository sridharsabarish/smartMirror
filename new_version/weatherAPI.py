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
        WEATHER_URL = "http://api.weatherapi.com/v1/current.json?key="+str(self.api_key)+"&q="+city+"&aqi=yes"      
        print(WEATHER_URL)

        try:
            apiRequestObj = APIRequest()
            self.json = apiRequestObj.get_json(WEATHER_URL)
            print(self.json)
        except:
            print("An Exception Occured")

        return  self.json


    def read_api_key_from_env(self):

        load_dotenv(find_dotenv())
        self.api_key = os.getenv("API_KEY")

        return self.api_key is not None