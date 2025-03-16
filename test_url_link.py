
'''
Note : Testing is done with PyTest

Some simple tests on API Request to a specific location.
'''

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

def test_sl_api_reacheable():
    out = getJson("https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100")
    assert out!=None
    
# def test_inventory_app_is_running():
#     out = getJson("http://0.0.0.0:5000/inventory/overdue")
#     assert out!=None
    
    
# def test_flask_app_is_running():
#     out = getJson("http://0.0.0.0:2000/")
#     assert out!=None
    

