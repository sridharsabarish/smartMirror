import json
import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from APIRequest import APIRequest
from loguru import logger
import sys


logger.remove()
logger.add(sys.stdout, format="{time} | {level} | {message}", serialize=True)
logger.add("logs.json", serialize=True)

class HandleClothing:
# Todo : Think how to refactor this one.
    def get_weather_details(self,city):
        apiRequest = APIRequest();
        load_dotenv()
        api_key = os.getenv("API_KEY")

        if not api_key:
            logger.error("Error: API_KEY not found in .env file.")

        else:
            url="http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes"      
            val = apiRequest.get_json(url);
            from pprint import pprint
            temperature = val['current']['temp_c']
            layers=self.find_layers(temperature)
            return layers
            
            
        
    def find_layers(self,temperature):
        # Use the attributes from the weatherDetails and design clothing layers.
        layers = 1
        if temperature < 10:
            layers =3
        elif 10 <= temperature < 15:
            layers = 2
        elif 15 <= temperature < 20:
            layers = 1
        elif 20 <= temperature < 30:
            layers = 0
        else:
            layers = 0

        return layers
        
        

# clothing = HandleClothing()
# clothing.get_weather_details("stockholm")