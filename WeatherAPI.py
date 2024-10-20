import os
import requests
import pprint


def getJson(url):
    response = requests.get(url)
    val = response.json()
    return val

def buildWeather():
    city = "Sollentuna" 

    api_key = "ca6db37f82fc4cba9cf51956241909"
    url = "http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes";
    return getJson(url)

def main():
    out = buildWeather()
    print(out["current"]["temp_c"])
    
main()


    
    
