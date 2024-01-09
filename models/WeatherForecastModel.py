from models.HourlyForecastModel import HourlyForecastModel
from models.DailyForecastModel import DailyForecastModel
from models.BaseWeatherForecastModel import BaseWeatherForecastModel


class WeatherForecastModel(BaseWeatherForecastModel):
    def __init__(self, date:str, temperature:str, humidity:str, is_day:str, rain:str, weather_code:str, wind_speed:str, wind_direction:str,
                 dailyForecast:list, hourlyForecast:list):
        super().__init__(weather_code, date)
        self.temperature = temperature
        self.humidity = humidity
        self.setIs_day(is_day)
        self.rain = rain
        self.wind_speed = wind_speed
        self.setWind_direction(wind_direction)
        self.dailyForecast = dailyForecast
        self.hourlyForecast = hourlyForecast
    
    def setIs_day(self, is_day):
        try:
            self.is_day = bool(int(is_day))
        except ValueError:
            self.is_day = True
    def setWind_direction(self, wind_direction):
        try:
            self.wind_direction = float(wind_direction)
        except:
            self.wind_direction = None