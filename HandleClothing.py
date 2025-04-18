import json
import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from APIRequest import APIRequest
class HandleClothing:
# Todo : Think how to refactor this one.
    def getWeatherDetails(self,city):
        apiRequest = APIRequest();
        load_dotenv()
        api_key = os.getenv("API_KEY")

        if not api_key:
            print("Error: API_KEY not found in .env file.")

        else:
            url="http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes"      
            val = apiRequest.getJson(url);
            from pprint import pprint
            temperature = val['current']['temp_c']
            layers=self.buildLogicForClothing(temperature)
            
            
        
    def buildLogicForClothing(self,temperature):
        # Use the attributes from the weatherDetails and design clothing layers.
        layers = 1
        if temperature < 10:
            layers =4
        elif 10 <= temperature < 15:
            layers = 3
        elif 15 <= temperature < 20:
            layers = 2
        elif 20 <= temperature < 30:
            layers = 1
        else:
            layers = 0

        return layers
        
        

# clothing = HandleClothing()
# clothing.getWeatherDetails("stockholm")