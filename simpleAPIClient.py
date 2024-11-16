import requests
from datetime import datetime
from flask import Flask, render_template_string
import assets


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
                <h1>SL is currently on a coffee break</h1>
                <p>Don't worry, it's not you, it's them. Or maybe it's just the coffee. Either way, try again in a bit, maybe.</p>
                <p>In the meantime, take a deep breath, and remember: there's always another way to get where you need to go. Preferably with a coffee in hand.</p>
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
    

def buildWebPage():
    out = buildSLDetails()
    if not out:
        return buildErrorCase(out)

    
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

       
    """
   
    for i, dep in enumerate(out):

        color = assets.ColorsInHex.BLUE  # default color
        if dep[1][:2] == "Nu":
            continue
        
        elif 3 <= int(dep[1][:2]) < 7:
            color = assets.ColorsInHex.GREEN
        
        html += f"<li class='list-group-item'><h{i+1}><span style='color: #ffa500;'>{dep[0]}</span> <span style='color: #a0aec0;'> | </span> <span style='color: {color};'>{dep[1]}</span></h{i+1}></li>"
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
    <p class='list-group-item' style='background-color: #45aaf2; color: #fff; text-align: center; margin: 0 auto;'>
        Last updated: {current_time}
    </p>
    """ 
    
    return html

#Flask Related Stuff
app = Flask(__name__)

@app.route('/')
def servePage():
    html = buildWebPage()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)

