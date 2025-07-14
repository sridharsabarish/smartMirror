import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv
from buildHtml import buildHtml
from loguru import logger
import sys
logger.remove()
logger.add(sys.stdout, format="{time} | {level} | {message}", serialize=True)
logger.add("logs.json", serialize=True)

class APIRequest:
    def get_json(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises HTTPError for bad responses
            val = response.json()
        except requests.exceptions.RequestException as e:
            val = None  # Or handle the error as needed
            logger.error(f"An error occurred: {e}")
        return val