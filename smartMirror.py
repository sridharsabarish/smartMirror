import json
import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from buildHtml import buildHtml
from APIRequest import APIRequest
from HandleClothing import HandleClothing


#TODO : General reorganization/cleanup of the code below
def getSLDetails():
    
    apiRequest = APIRequest();
    #TODO: Perhaps raise an exception and handle it?
    val = apiRequest.buildSLQ()
    if not val:
        return []
    
    
    details_list = []
    for i, departure in enumerate(val['departures']):
        if i < 10:
            truncated_destination = departure['destination'].split()[0]
            details_list.append([truncated_destination, departure['display']])
        else:
            break
    return details_list




def buildWebPage():
    webpage = buildHtml();
    #Todo: Need to add weather to the info bar.
    clothing = HandleClothing()
    out1 = clothing.getWeatherDetails("stockholm");
    
    
    out = getSLDetails()
    if not out:
        return webpage.buildErrorCase(out)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    date_today=datetime.today().strftime('%d-%m-%y')
    
    # Weather Segment
    html = webpage.base_layout()
    html = webpage.weather_ux(html)
    html = webpage.create_div(html)
    html = webpage.create_div(html)
    html = webpage.sl_ux(html,out)
    html = webpage.add_node_red_dashboard(html)
    html = webpage.close_div(html)
    html = webpage.inventory_ux(html,names)
    html = webpage.close_div(html)
    

    html = webpage.updated_ux(html,current_time, date_today)
    html = webpage.close_html(html)
    # print("-----------")
    # print(html)
    # print("-----------")
    return html




def get_overdue():
    try:
        response = requests.get("http://0.0.0.0:5000/inventory/overdue")
        response.raise_for_status()
        #print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None



# General Code
names=[]
outjson=get_overdue()
if outjson:
    outjson = json.loads(outjson)
    size_of_inv=len(outjson['inventory'])
    for i in range(0,size_of_inv):
        names.append(outjson['inventory'][i]['name'])
        


#Flask Related Stuff
app = Flask(__name__)

@app.route('/')
def servePage():
    html = buildWebPage()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)





