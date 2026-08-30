import requests
from datetime import datetime
from flask import Flask, render_template_string
import os
from dotenv import load_dotenv, find_dotenv

from loguru import logger
import sys
import xml.etree.ElementTree as ET
logger.remove()
logger.add(sys.stdout, format="{time} | {level} | {message}", serialize=True)
logger.add("logs.json", serialize=True)


import json
import paho.mqtt.subscribe as subscribe




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

    def get_xml(self,url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises HTTPError for bad responses

            val = ET.fromstring(response)
            print(val)

           
            return val
        except requests.exceptions.RequestException as e:
            val = None  # Or handle the error as needed
            print("error". e)
            logger.error(f"An error occurred: {e}")
        return val    
class MQTT:

    #TODO : Make the username and password part of the .env
    def __init__(self,port=1883,username="",password="",topic=""):
        self.username='robot'
        self.password='robot'
        self.broker="192.168.0.188"
        self.port=port
        self.topic=topic

    def connect_mqtt():
        return 


    def listen_to_mqtt(self,topic):
        #TODO : Implement the listener

        msg = subscribe.simple(
            topic,
            hostname=self.broker,
            port=1883,
            auth={
                "username": self.username,
                "password": self.password
            },
        )

        payload = json.loads(msg.payload.decode("utf-8"))

        print(payload)



        return {}

class Notify:
    def sendAlerts(self,message):
        #TODO: Implement the mechanism to send alerts
        print("Sending alert : ", message)