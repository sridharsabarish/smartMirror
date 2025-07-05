import json
import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from src.buildHtml import buildHtml
from src.APIRequest import APIRequest
from src.HandleClothing import HandleClothing
from loguru import logger


class smartMirror:
    def get_sl_details(self):
        
        apiRequest = APIRequest();
        #TODO: Perhaps raise an exception and handle it?
        
        url = "https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100"
        val = apiRequest.get_json(url)
        if not val:
            return []
        
        
        details_list = []
        for i, departure in enumerate(val['departures']):
            if i < 10:
                truncated_destination = departure['destination'].split()[0]
                logger.debug(truncated_destination)
                if(truncated_destination == ""):
                    continue
                else:
                    details_list.append([truncated_destination, departure['display']])
            else:
                break
        return details_list

    def build_web_page(self):
        webpage = buildHtml();
        #Todo: Need to add weather to the info bar.
        # clothing = HandleClothing()
        # # out1 = clothing.get_weather_details("stockholm");
        # # logger.debug("Weather details: " + str(out1))
        
        
        
        
        
        out = self.get_sl_details()
        if not out:
            return webpage.buildErrorCase(out)
        
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        date_today=datetime.today().strftime('%d-%m-%y')
        
        # Weather Segment
        html = webpage.build_UI(out,current_time,date_today)
        return html

    def get_overdue(self):
        try:
            response = requests.get("http://0.0.0.0:5000/inventory/overdue")
            response.raise_for_status()
            logger.trace(response.text)
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")
            return None

    def __init__(self):
        names=[]
        outjson=self.get_overdue()
        if outjson:
            outjson = json.loads(outjson)
            size_of_inv=len(outjson['inventory'])
            for i in range(0,size_of_inv):
                names.append(outjson['inventory'][i]['name'])     
                pass

