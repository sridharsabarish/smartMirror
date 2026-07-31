from weatherAPI import load_weather,read_api_key_from_env
from smartMirror import smartMirror
class TestWeather:

    def test_API_KEY_exists(self):
        read_api_key_from_env()
        assert True

    def test_check_api_key_works(self):
        load_weather()
        assert True



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
