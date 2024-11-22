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

outjson=get_overdue()
if outjson:
    outjson = json.loads(outjson)
    size_of_inv=len(outjson['inventory'])
    for i in range(0,size_of_inv):
        print(outjson['inventory'][i]['name'])
        
