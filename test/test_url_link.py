
'''
Note : Testing is done with PyTest

Some simple tests on API Request to a specific location.
'''

import requests
from datetime import datetime
from flask import Flask, render_template_string

def get_json(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses
        
        val = response.json()
    except requests.exceptions.RequestException as e:
        val = None  # Or handle the error as needed
        print(f"An error occurred: {e}")
    return val




import pytest

@pytest.mark.parametrize("url", [
    "https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100",
    "http://0.0.0.0:5000/inventory/overdue"
])
def test_link(url):
    out = get_json(url)
    assert out!=None
    
    
# def test_flask_app_is_running():
#     out = get_json("http://0.0.0.0:2000/")
#     assert out!=None
    

