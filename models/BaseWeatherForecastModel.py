from abc import ABC
from datetime import datetime


class BaseWeatherForecastModel(ABC):
    def __init__(self, weather_code:str, date:str):
        self.setWeather_code(weather_code)
        self.date = datetime.fromisoformat(date)
    def setWeather_code(self, weather_code):
        try:
            self.weather_code = int(weather_code)
        except:
            self.weather_code = -1
        