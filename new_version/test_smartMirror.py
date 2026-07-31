from smartMirror import smartMirror, LIGHT
from APIRequest import MQTT
from pprint import pprint
import pytest
from paho.mqtt import client as mqtt_client


class TestTransport:
    def test_get_sl_buses(self):
        mirror = smartMirror()
        out = mirror.get_buses();
        assert len(out) >0 
        try:
            departures = out["departures"]
            assert departures is not None
            assert mirror.get_all_unique_destination(departures) is  not None
            assert mirror.get_all_times_for_a_destination(destination='Danderyds sjukhus',departures=departures) is not None
        except:
            assert False
    def test_get_sl_trains(self):
        mirror = smartMirror()
        out = mirror.get_trains();
        #print(out)
        assert len(out) >0 
        try:
            departures = out["departures"]
            assert departures is not None
            assert mirror.get_all_unique_destination(departures) is   not None
            assert mirror.get_all_times_for_a_destination(destination='Stockholms östra',departures=departures) is  not None
        except:
            assert False
 
class TestMisc:

    @pytest.mark.skip
    def test_get_random_poems(self):

        try:
            mirrorObj = smartMirror()
            out = mirrorObj.get_poem();
            print(out)
            assert out[0]["title"] is not None
        except:
            print("Some error occured")
            assert False

    def test_get_date(self):
        mirrorObj = smartMirror()
        out = mirrorObj.get_date()
        print(out)
        assert out["day"] is not None and out["hour"] is not None and out ["minute"] is not None and out["week"] is not None

    def test_get_news(self):
        mirrorObj = smartMirror()
        print(mirrorObj.get_news())
        assert mirrorObj.get_news() is  not None
    

class TestInventory:
    def test_get_overdue(self):
        mirror = smartMirror()
        assert len(mirror.get_overdue()) >0


class TestControl:
    def test_turn_on_lights(self):
        BEDROOM_LIGHT = LIGHT(NAME="Bedroom")
        assert LIGHT.ON(BEDROOM_LIGHT) == True

class TestMQTTListen:
    @pytest.mark.skip 

    def test_setup_mqtt(self):
        mqttObj = MQTT()
        assert mqttObj.port ==1883
        assert mqttObj.broker=="192.168.0.188"

    def connect_to_mqtt_livingroom(self):
        mqttObj = MQTT(topic="living_room")
        mqttObj.connect_mqtt()
        