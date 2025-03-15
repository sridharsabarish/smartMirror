import requests
from datetime import datetime
from flask import Flask, render_template_string
import assets
import os
from dotenv import load_dotenv, find_dotenv



def getJson(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses
        val = response.json()
    except requests.exceptions.RequestException as e:
        val = None  # Or handle the error as needed
        print(f"An error occurred: {e}")
    return val
def buildSLQ():
    url = "https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100"
    try:
        return getJson(url)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def getSLDetails():
    #TODO: Perhaps raise an exception and handle it?
    val = buildSLQ()
    if not val:
        return []
    
    
    details_list = []
    for i, departure in enumerate(val['departures']):
        if i < 4:
            truncated_destination = departure['destination'].split()[0]
            details_list.append([truncated_destination, departure['display']])
        else:
            break
    return details_list


def getWeatherDetails(city):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY not found in .env file.")

    else:
        url="http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes"      
        val = getJson(url);
        print(val)
     

def buildErrorCase(out):
    if not out:
        print("Error: Could not build SL details page")
        html = """
        <html>
        <head>
            <title>SL decided to take a break</title>
            <style>
                body {
                    background-color: #f2f2f2;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                h1 {
                    color: #ff6347;
                    font-size: 4rem;
                    margin-bottom: 2rem;
                }
                p {
                    font-size: 2rem;
                    line-height: 1.5;
                }
            </style>
            <meta http-equiv="refresh" content="30">
        </head>
        <body>
            <div class="container">
                <h1>Fika Time!</h1>
                <p>Get that Coffee!</p>
            </div>
        </body>
        </html>
    <script>
        setTimeout(function(){
            window.location.reload(1);
        }, 6000);
    </script>        
        """
        return html
    

def base_layout():
    html = """
    <html>
    <head>
        <title></title>
        <style>
            .title {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
        </style>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <style>
            body {
                background-color: #1a202c;
            }
            .container {
                margin-top: 3rem;
            }
            .list-group-item {
                margin-top: 0.5rem;
                border-radius: 0.25rem;
                background-color: #2d3748;
                border: none;
                padding: 1rem;
            }
            .list-group-item:first-child {
                margin-top: 0;
            }
            .list-group-item h1,
            .list-group-item h2,
            .list-group-item h3 {
                color: #fff;
            }
            .list-group-item h1 {
                font-size: 2.5rem;
            }
            .list-group-item h2 {
                font-size: 1.75rem;
            }
            .list-group-item h3 {
                font-size: 1.25rem;
            }
            .list-group {
                max-width: 40rem;
            }
        </style>
    </head>
    <body>
     """
    return html
def weather_ux(html):
    html += """
            <a class="weatherwidget-io" href="https://forecast7.com/en/59d4417d94/sollentuna/" data-label_1="SOLLENTUNA" data-label_2="WEATHER" data-theme="original" >SOLLENTUNA WEATHER</a>
    <script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    </script>
    """
    return html

def sl_ux(html,out):
   
    html += """
        <div style="display: inline-block; vertical-align: top; width: 70%; text-align: center;">
            <div class="list-group">
    """
    for i, dep in enumerate(out[:3]):

        color = assets.ColorsInHex.BLUE  # default color
        if dep[1][:2] == "Nu":
            continue
        
        elif 3 <= int(dep[1][:2]) < 7:
            color = assets.ColorsInHex.GREEN
        
        html += f"<li class='list-group-item'><h{i+1}><span style='color: #ffa500;'>{dep[0]}</span> <span style='color: #a0aec0;'> | </span> <span style='color: {color};'>{dep[1]}</span></h{i+1}></li>"
    html += """
            </div>
        </div>
    """
    return html
    
    
def inventory_ux(html,names):
    html += f"""
    <div style="display: inline-block; vertical-align: top; width: calc(30% - 20px); text-align: center; background-color: #ffffe0; padding: 1px; border-radius: 1px; box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);">
            <p style="margin-bottom: 0; font-size: 1rem;">
            <h2 style="margin: 0.5rem 0; color: #ff0000;"><span style="color: #ff0000; font-size: 1.5rem; margin-right: 0.5rem; display: inline-block;"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-alert-triangle"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="9.01"></line><line x1="12" y1="15" x2="12.01" y2="15"></line></svg></span><i class="fas fa-triangle-exclamation" style="color: #ff0000;"></i> Overdue Items</h2>
        </p>
        <ul style="list-style: none; padding: 0; margin: 0 10px;">
        {"".join([f"<li style='margin-bottom: 0.5rem; font-size: 1.2rem;'><i class='fas fa-exclamation-circle' style='color: #ffcc00;'></i> {index + 1}. {name}</li>" for index, name in enumerate(names[:3])])}
        </ul>

    </div>
      """
    return html
def updated_ux(html,current_time, date_today):
    html += f"""
    <div style="width: 100%; text-align: center;">
        <p class='list-group-item' style='background-color: #45aaf2; color: #fff; margin: 0;'>
            Last updated: {current_time}, {date_today}
        </p>
    </div>
    """
    return html


def close_html(html):
    html+=f"""
    </body>
    </html>
    """
    return html




def buildWebPage():
    #Todo: Need to add weather to the info bar.
    out1 = getWeatherDetails("stockholm");
    
    
    out = getSLDetails()
    if not out:
        return buildErrorCase(out)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    date_today=datetime.today().strftime('%d-%m-%y')
    
    # Weather Segment
    html = base_layout()
    html = weather_ux(html)
    html = sl_ux(html,out)
    html = inventory_ux(html,names)
    html = updated_ux(html,current_time, date_today)
    html = close_html(html)
    print("-----------")
    print(html)
    print("-----------")
    return html
   


import json
import requests

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
    app.run(host='0.0.0.0', port=2000, debug=True)





