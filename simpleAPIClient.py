import requests

def getJson(url):
    try:
        response = requests.get(url)
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

def buildSLDetails():
    val = buildSLQ()
    if not val:
        return []
    
    details_list = []
    for i, departure in enumerate(val['departures']):
        if i < 4:
            details_list.append([departure['destination'], departure['display']])
        else:
            break
    return details_list



# def buildWeather():
#     city = "Stockholm"
#     api_key = "ca6db37f82fc4cba9cf51956241909"
#     url = "http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city+"&aqi=yes"
#     out = getJson(url)
#     return out['current']['temp_c']

def main():
    out = buildSLDetails()
    print(out)

def buildWebPage():
    out = buildSLDetails()
    if not out:
        print("Error: Could not build SL details page")
        return
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M")
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
           <a class="weatherwidget-io" href="https://forecast7.com/en/59d4417d94/sollentuna/" data-label_1="SOLLENTUNA" data-label_2="WEATHER" data-theme="original" >SOLLENTUNA WEATHER</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>

        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h1 class="display-4 text-white">SL Details</h1>
                    <ul class="list-group">
    """
   
    for i, dep in enumerate(out):

        color = "#45aaf2"  # default color
        if dep[1][:2] == "Nu":
            continue
        
        elif 3 <= int(dep[1][:2]) < 7:
            color = "#34C759"
        
        html += f"<li class='list-group-item'><h{0+i}><span style='color: #ffa500;'>{dep[0]}</span> <span style='color: #a0aec0;'> | </span> <span style='color: {color};'>{dep[1]}</span></h{0+i}></li>"
    html += """
                    </ul>
                </div>  
            </div>
        </div>
    </body>
    </html>
    <script>
        setTimeout(function(){
            window.location.reload(1);
        }, 60000);
    </script>
    """
    html += f"""
    <p class='list-group-item' style='background-color: #45aaf2; color: #fff'>
        Last updated: {current_time}
    </p>
    """ 
    
    return html

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def servePage():
    html = buildWebPage()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

main()

