import json
import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from APIRequest import APIRequest
class HandleClothing:
# Todo : Think how to refactor this one.
    def getWeatherDetails(city):
        apiRequest = APIRequest();
        load_dotenv()
        api_key = os.getenv("API_KEY")

        if not api_key:
            print("Error: API_KEY not found in .env file.")

        else:
            url="http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes"      
            val = apiRequest.getJson(url);
            from pprint import pprint
            pprint(val)
            
        
    def buildLogicForClothing():
        # Use the attributes from the weatherDetails and design clothing layers.
        print("Hello world")