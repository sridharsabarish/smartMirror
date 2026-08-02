from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os
def load_weather():
    #TODO : Implement the logic
    json = {}
    return json


def read_api_key_from_env():
    #TODO: Implement Logic
    load_dotenv(find_dotenv())
    api_key = os.getenv("API_KEY")

    return api_key is not None