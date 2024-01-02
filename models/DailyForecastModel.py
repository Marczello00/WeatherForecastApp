from datetime import datetime
from models.BaseWeatherForecastModel import BaseWeatherForecastModel
#Should I store some of the data as int or should I leave it as a string? Later then it will be again converted to string so is it really necessary to convert it now to int? For example temperature_min.
#Maybe it is better as an int because of the validation?

#Should I store weather_code as a code or load into memory image now? I think it is better to store it as a code and then load image when it is needed.

class DailyForecastModel(BaseWeatherForecastModel):
    def __init__(self, date:str, weather_code:str, temperature_min:str, temperature_max:str, sunrise:str, sunset:str, rain_sum:str, wind_speed:str, wind_direction:str):
        super().__init__(weather_code, date)
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.sunrise = datetime.fromisoformat(sunrise)      #"2023-12-29T07:17"
        self.sunset = datetime.fromisoformat(sunset)        #"2023-12-29T14:59"
        self.rain_sum = rain_sum
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
