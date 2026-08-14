from weatherAPI import WeatherAPI
from smartMirror import smartMirror
from APIRequest import Notify
import pytest

TEST_DATA = ["Stockholm", "Chennai", "New Delhi"]
INCORRECT_TEST = ["Lalaland"]
class TestWeather:

    def test_API_KEY_exists(self):
        weatherObj = WeatherAPI()
        assert weatherObj.read_api_key_from_env()

    @pytest.mark.skip
    @pytest.mark.parametrize("t",TEST_DATA)
    def test_weather(self,t):
        weatherObj = WeatherAPI()
        out = weatherObj.load_weather(city=t)
        print(out)
        assert len(out)>0

    @pytest.mark.parametrize("t",INCORRECT_TEST)
    def test_fail_incorrect_cities(self,t):
        weatherObj = WeatherAPI()
        out = weatherObj.load_weather(city=t)
        print(out)
        assert len(out) ==0

class TestClimate:
    def test_get_soil_health(self):
        mirror = smartMirror()
        assert  mirror.get_soil_health() == 0

    def test_get_livingroom_climate(self):
        mirror = smartMirror()
        out = mirror.get_temperature("living_room")
        assert out["temperature"] == 30 and out["humidity"] is not None 
    def test_get_bedroom_climate(self):
        mirror = smartMirror()
        out = mirror.get_temperature("bed_room")
        assert out["temperature"] == 30 and out["humidity"] is not None 
    def test_send_alert_for_low_temperature(self):
        notify = Notify()
        notify.sendAlerts("Something Gone wrong")
        assert True

 