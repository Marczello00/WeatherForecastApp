from models.WeatherForecastModel import WeatherForecastModel
from models.DailyForecastModel import DailyForecastModel
from models.HourlyForecastModel import HourlyForecastModel
from services.DownloadDataService import DownloadDataService


def AnalyzeReplyService(weather_data):
    
    date = weather_data['current']['time']
    temperature = weather_data['current']['temperature_2m']
    humidity = weather_data['current']['relative_humidity_2m']
    is_day = weather_data['current']['is_day']
    rain = weather_data['current']['rain']
    weather_code = weather_data['current']['weather_code']
    wind_speed = weather_data['current']['wind_speed_10m']
    wind_direction = weather_data['current']['wind_direction_10m']

    daily_forecast_data = weather_data['daily']
    daily_forecast = DailyForecastModel(date=date, weather_code=weather_code,
                                        temperature_min=daily_forecast_data['temperature_2m_min'][0],
                                        temperature_max=daily_forecast_data['temperature_2m_max'][0],
                                        sunrise=daily_forecast_data['sunrise'][0],
                                        sunset=daily_forecast_data['sunset'][0],
                                        rain_sum=daily_forecast_data['rain_sum'][0],
                                        wind_speed=daily_forecast_data['wind_speed_10m_max'][0],
                                        wind_direction=daily_forecast_data['wind_direction_10m_dominant'][0])

    hourly_forecast_data = weather_data['hourly']
    hourly_forecast = HourlyForecastModel(date=date, temperature=hourly_forecast_data['temperature_2m'][0],
                                          weather_code=hourly_forecast_data['weather_code'][0])

    weather_forecast = WeatherForecastModel(date=date, temperature=temperature, humidity=humidity,
                                            is_day=is_day, rain=rain, weather_code=weather_code,
                                            wind_speed=wind_speed, wind_direction=wind_direction,
                                            dailyForecast=daily_forecast, hourlyForecast=hourly_forecast)

    return weather_forecast




