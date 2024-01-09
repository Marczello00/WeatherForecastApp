from models.BaseWeatherForecastModel import BaseWeatherForecastModel


class HourlyForecastModel(BaseWeatherForecastModel):
    def __init__(self, date: str, temperature: str, weather_code: str):
        super().__init__(weather_code, date)
        self.temperature = temperature
