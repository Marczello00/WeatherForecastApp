import json
from models.WeatherForecastModel import WeatherForecastModel
from models.DailyForecastModel import DailyForecastModel
from models.HourlyForecastModel import HourlyForecastModel


def AnalyzeReplyService(weather_data):
    # Convert the JSON string to a dictionary
    weather_data_dict = json.loads(weather_data)

    # Extract data from 'current'
    current_data = weather_data_dict['current']
    date = current_data['time']
    temperature = current_data['temperature_2m']
    humidity = current_data['relative_humidity_2m']
    is_day = current_data['is_day']
    rain = current_data['rain']
    weather_code = current_data['weather_code']
    wind_speed = current_data['wind_speed_10m']
    wind_direction = current_data['wind_direction_10m']

    # Extract data from 'daily'
    daily_forecast_data = weather_data_dict['daily']
    #first_daily_forecast = daily_forecast_data['time'][0]
    daily_forecast = []
    for i in range(len(daily_forecast_data['time'])):
        daily_forecast.append({
            'date': daily_forecast_data['time'][i],
            'weather_code': daily_forecast_data['weather_code'][i],
            'temperature_min': daily_forecast_data['temperature_2m_min'][i],
            'temperature_max': daily_forecast_data['temperature_2m_max'][i],
            'sunrise': daily_forecast_data['sunrise'][i],
            'sunset': daily_forecast_data['sunset'][i],
            'rain_sum': daily_forecast_data['rain_sum'][i],
            'wind_speed': daily_forecast_data['wind_speed_10m_max'][i],
            'wind_direction': daily_forecast_data['wind_direction_10m_dominant'][i]
        })

    # Extract data from 'hourly'
    hourly_forecast_data = weather_data_dict['hourly']
    #first_hourly_forecast = hourly_forecast_data['time'][0]
    hourly_forecast = []
    for i in range(len(hourly_forecast_data['time'])):
        hourly_forecast.append({
            'date': hourly_forecast_data['time'][i],
            'temperature': hourly_forecast_data['temperature_2m'][i],
            'weather_code': hourly_forecast_data['weather_code'][i]
        })

    # Create the main WeatherForecastModel
    weather_forecast = WeatherForecastModel(date=date, temperature=temperature, humidity=humidity,
                                            is_day=is_day, rain=rain, weather_code=weather_code,
                                            wind_speed=wind_speed, wind_direction=wind_direction,
                                            dailyForecast=daily_forecast, hourlyForecast=hourly_forecast)

    return weather_forecast




