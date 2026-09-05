
from APIRequest import APIRequest
from APIRequest import MQTT 
import pprint

class LIGHT:
    def __init__(self,NAME=""):
        self.state = 0
        self.name = NAME
    def ON(self):
        self.state = 1;
        return self.state


    
class smartMirror:

    BUSES_URL="https://transport.integration.sl.se/v1/sites/2232/departures?forecast=100"
    TRAINS_URL="https://transport.integration.sl.se/v1/sites/9668/departures?forecast=100" 

    buses = {}
    trains = {}
    poem  = {}
    soil = {}

    def __init__(self):
        self.mqttObj = MQTT()
        self.APIRequestObj = APIRequest()

    def call_inventory_api(self,mode):
        mqttObj = MQTT()
        #rest_api_call()
        out = self.mqttObj.listen_to_mqtt(mode)
        return {"banana"}
    
    def call_soil_api(self):
        out = self.mqttObj.listen_to_mqtt("soil")
        self.soil = {"status":"NA"}
        return self.soil
    def get_all_unique_destination(self,departures):
        unique_destination = set()
        for departure in departures:
            unique_destination.add(departure["destination"])
        print(unique_destination)
        return unique_destination
    def get_all_times_for_a_destination(self,destination,departures):
        all_times = []
        for departure in departures:
            if departure['destination'] == destination:
                print(departure['display'])
                all_times.append(departure['display'])

        return all_times

    def call_sl_api(self,mode):
        # TODO: Implement more
        out = {}
       
        if mode =="buses":
            
            try:
                out = self.APIRequestObj.get_json(self.BUSES_URL)
                AllDepartures = out['departures']
                #pprint.pp(AllDepartures)
            except:
                print("error occured")
            finally:
                return out
            

            pprint.pp(out['departures'])
            
            return out
            return {"Buses":[5,10,15,20]}
        if mode == "trains":
   
            try:
                out = self.APIRequestObj.get_json(self.TRAINS_URL)
                AllDepartures = out['departures']
                #pprint.pp(AllDepartures)
            except:
                print("error occured")
            finally:
                return out
    

    def make_api_call(self,url):
        out={}
        try:
            out = self.APIRequestObj.get_json(url)
            #print(out)
        except:
            print("Some Error Occured")
        finally:
            return out        

    def make_api_call_xml(self,url):
        out={}
        try:
            out = self.APIRequestObj.get_xml(url)
            #print(out)
        except:
            print("Some Error Occured")
        finally:
            return out           


    def call_poetry_db_api(self):
        # To Implement more
        
        out = {}
        try:
            POETRY_DB_URL="https://poetrydb.org/random"
            out = self.make_api_call(url=POETRY_DB_URL)
            print(out)
        except:
            print("Some Error Occured in call_poetry_db_api")
        finally:
            return out

    def get_soil_health(self):
        
        try:
            self.call_soil_api()
            
        except:
            return 1
        finally:
            return 0;
    def get_buses(self):
        try:
            self.buses=self.call_sl_api(mode="buses")
        except:
            return 1;
        finally:
            return self.buses

    def get_trains(self):
        try:
            self.trains=self.call_sl_api(mode="trains")
        except:
            return 1;
        finally:
            return self.trains


    def get_poem(self):
        try:
            self.poem=self.call_poetry_db_api()
        except:
            return 1;
        finally:
            return self.poem    
        
    def get_temperature(self,room):
        if room =="living_room" or room =="bed_room":
            mqttObj = MQTT()
            output = mqttObj.listen_to_mqtt(room);
            return output
            return {"temperature":30, "humidity":20}
        
    def get_date(self):
        # To Implement
        from datetime import datetime
        today = datetime.now()
        return {"day":today.day,"hour":today.hour,"minute":today.minute, "week":today.isocalendar()[1]}
    
    def get_overdue(self):
        out = self.call_inventory_api("overdue")
        return out
    

    def get_news(self):
        BBC_TOP_STORIES_URL = "https://feeds.bbci.co.uk/news/rss.xml"
        out = self.make_api_call(url=BBC_TOP_STORIES_URL)
        print(out)
        return out
    def add_overdue_to_mirror(self,json):
        # TODO: Implement Logic
        return True