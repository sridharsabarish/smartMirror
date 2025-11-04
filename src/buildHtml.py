import assets as assets
from loguru import logger
import sys
from getMeal import MealPlan
from HandleClothing import HandleClothing 
logger.remove()
logger.add(sys.stdout, format="{time} | {level} | {message}", serialize=True)
logger.add("logs.json", serialize=True)

class buildHtml:
    def buildErrorCase(self,out):
        if not out:
            logger.error("Error: Could not build SL details page")
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
        
    def base_layout(self):
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
                    width: 100%;
                }
                .list-group-item {
                    margin-top: 0.5rem;
                    border-radius: 0.25rem;
                    background-color: #2d3748;
                    border: none;
                    padding: 1rem;
                    width: 100%;
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
                    font-size: 7.5rem;
                }
                .list-group-item h2 {
                    font-size: 1.75rem;
                }
                .list-group-item h3 {
                    font-size: 1.25rem;
                }
                .list-group {
                    max-width: 100%;
                }
            </style>
        </head>
        <body>
        """
        return html
    def weather_ux(self,html):
        html += """
                <a class="weatherwidget-io" href="https://forecast7.com/en/59d4417d94/sollentuna/" data-label_1="SOLLENTUNA" data-label_2="WEATHER" data-theme="original" >SOLLENTUNA WEATHER</a>
        <script>
        !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
        </script>
        """
        
        return html

    def create_div(self,html):
        html += """
            <div>
        """
        return html

    def sl_ux(self,html,out):
        
        html += """
            <div style="display: block; vertical-align: top; width: 100%; height: 100vh; text-align: center;">
                <div class="list-group" style="height: 100%;">
        """
        logger.trace("i'm here")
        logger.debug(out)
        
        
        ## Todo : Good to refine a bit later
        out_dict = {}
        logger.debug(out_dict)
        for dep in out:
            if dep[0] not in out_dict:
                out_dict[dep[0]] = [dep[1]]
            else:
                out_dict[dep[0]].append(dep[1])
        
        logger.info(out_dict)
        
        
        
        html += """
            <div style="display: block; vertical-align: top; width: 100%; text-align: center;">
                <div class="list-group" style="height: 100%;">
        """
        for key, deps in out_dict.items():
            if not key:
                continue

            for i, dep in enumerate(deps):
                
                
                logger.debug(i)
                logger.debug(dep)
                logger.debug(dep[-3:])
                
                
                ## Todo : Remove this
                if (dep[-3:] != "min"):
                    continue
                if dep[:2] == "Nu":
                    continue
                color = assets.ColorsInHex.GREEN if 3 <= int(dep[:2]) < 7 else assets.ColorsInHex.BLUE
                
                
                if i ==0:
                    html += f"""
                    <li class='list-group-item' style="height: 100%; display: flex; align-items: center; justify-content: center;">
                        <h1 style='display: inline-block; font-size: 4rem; color: #ffa500;'>{key} <span style='color: {color};'>{dep}</span> </h1>
                        <div style='font-size: 2rem'>
                    """
                else:
                    html += f"<span style='color: #808080;'>{dep}</span> "
            html += """
                </div>
            </li>
            
                <script>
        setTimeout(function(){
            window.location.reload(1);
        }, 25000);
    </script>
            
            
            """
            
        html += """
                </div>
            </div>
        """
    
        return html


    def add_meals(self, html):
        # Todo : Fix logic below to make it read correct key
        print("Adding meals")
        mealPlan = MealPlan();
        json = mealPlan.return_json()
        print(json[1])
    



    def print_clothing_layers(self, html):
        layers = HandleClothing().get_weather_details("stockholm")
        print("Layers", layers)
        
        html += f"""
        <div style="
            background-color: #1E3A8A;  /* deep blue background */
            color: #F8FAFC;            /* almost white text */
            border-radius: 12px;
            padding: 16px;
            margin-top: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            font-family: 'Segoe UI', Roboto, sans-serif;
            font-size: 1.1rem;
            line-height: 1.5;
            text-align: center;
        ">
            <strong>Recommended Layers:</strong><br>{layers}
        </div>
        """
        return html

    def inventory_ux(self,html,names):
        
        logger.error("Came here")
        html += f"""
        <div style="display: inline-block; vertical-align: top; width: calc(30% - 20px); float: right; background-color: #ffffe0; padding: 1px; border-radius: 1px; box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2); text-align: right;">
            <div style="width: 100%;">
                <p style="margin-bottom: 0; font-size: 1rem;">
                <h2 style="margin: 0.5rem 0; color: #ff0000;"><span style="color: #ff0000; font-size: 1.5rem; margin-right: 0.5rem; display: inline-block;"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-alert-triangle"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="9.01"></line><line x1="12" y1="15" x2="12.01" y2="15"></line></svg></span><i class="fas fa-triangle-exclamation" style="color: #ff0000;"></i> Overdue Items</h2>
                </p>
                <ul style="list-style: none; padding: 0; margin: 0 10px;">
                {"".join([f"<li style='margin-bottom: 0.5rem; font-size: 1.2rem;'><i class='fas fa-exclamation-circle' style='color: #ffcc00;'></i> {index + 1}. {name}</li>" for index, name in enumerate(names[:10])])}
                </ul>
            </div>
        </div>
        """
        return html
    def updated_ux(self,html,current_time, date_today):
        html += f"""
        <div style="width: 100%; text-align: center;">
            <p class='list-group-item' style='background-color: #45aaf2; color: #fff; margin: 0;'>
                Last updated: {current_time}, {date_today}
            </p>
        </div>
        """
        return html

    def close_div(self,html):
        html+=f"""
        </div>
        """
        return html
    def close_html(self,html):
        html+=f"""
        </body>
        </html>
        """
        return html

    def add_node_red_dashboard(self, html):
        html += f"""
        <div style="width: 80%; height: 400px; text-align: left; margin-top: 10px; display: flex; justify-content: flex-start;">
            <div style="width: 58%; height: 80%;">
                <!-- Left component goes here -->
            </div>
            <div style="width: 58%; height: 100%;">
                <iframe src="http://192.168.0.107:1880/ui/" style="width: 100%; height: 100%; border: none;"></iframe>
            </div>
        </div>
        """
        return html
    def __init__(self):
        pass
    def build_UI(self,out,current_time, date_today,names):
        html = self.base_layout()
        html = self.weather_ux(html)
    
        html = self.create_div(html)
        html = self.create_div(html)
        html = self.print_clothing_layers(html)
        html = self.sl_ux(html,out)
        #html = self.add_node_red_dashboard(html)
        html = self.close_div(html)
        html = self.inventory_ux(html,names)
        html = self.close_div(html)
        
        self.add_meals(html)
        html = self.updated_ux(html,current_time, date_today)
        html = self.close_html(html)
        return html
