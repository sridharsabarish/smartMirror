import os
import requests
import pprint


def getJson(url):
    response = requests.get(url)
    val = response.json()
    return val

def buildWeather():
     

def main():
    out = buildWeather()
    print(out["current"]["temp_c"])
    
main()


    
    
