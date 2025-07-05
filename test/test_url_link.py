
'''
Note : Testing is done with PyTest

Some simple tests on API Request to a specific location.
'''

import requests
from datetime import datetime
from flask import Flask, render_template_string
from loguru import logger
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from APIRequest import APIRequest
import pytest

@pytest.mark.parametrize("url", [
    "https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100"
])
def test_link(url):
    apirequest = APIRequest()
    out = apirequest.get_json(url)
    assert out!=None
    

