from weatherAPI import WeatherAPI
from smartMirror import smartMirror
import pytest

TEST_DATA = ["Stockholm", "Chennai", "New Delhi"]
class TestWeather:

    def test_API_KEY_exists(self):
        weatherObj = WeatherAPI()
        assert weatherObj.read_api_key_from_env()

    @pytest.mark.parametrize("t",TEST_DATA)
    def test_check_api_key_works(self,t):
        weatherObj = WeatherAPI()
        out = weatherObj.load_weather(city=t)
        print(out)
        assert len(out)>0

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
