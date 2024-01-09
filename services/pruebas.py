from datetime import datetime
import json
import requests


class BaseWeatherForecastModel():
    def __init__(self, weather_code:str, date:str):
        self.setWeather_code(weather_code)
        self.date = datetime.fromisoformat(date)
    def setWeather_code(self, weather_code):
        try:
            self.weather_code = int(weather_code)
        except:
            self.weather_code = -1
        
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


class HourlyForecastModel(BaseWeatherForecastModel):
    def __init__(self, date:str, temperature:str, weather_code:str):
        super().__init__(weather_code, date)
        self.temperature = temperature

class WeatherForecastModel(BaseWeatherForecastModel):
    def __init__(self, date:str, temperature:str, humidity:str, is_day:str, rain:str, weather_code:str, wind_speed:str, wind_direction:str,
                 dailyForecast:DailyForecastModel, hourlyForecast:HourlyForecastModel):
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

def DownloadDataService(lati, longi):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lati}&longitude={longi}&current=temperature_2m,relative_humidity_2m,is_day,rain,weather_code,wind_speed_10m,wind_direction_10m&hourly=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,wind_speed_10m_max,wind_direction_10m_dominant&timezone=auto&forecast_days=3"
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Data downloaded successfully.")
            return AnalyzeReplyService(response.text)
        else:
            print(f"Error accessing the URL. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Connection error: {e}")
        return None
    

def getLatLong():
    url = "http://ip-api.com/json/"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            lat = data.get('lat')
            lon = data.get('lon')
            return(lat, lon)
        else:
            print(f"Error accessing the URL. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Connection error: {e}")



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
            'weather_code': hourly_forecast_data['weather_code'][i],
        })

    # Create the main WeatherForecastModel
    weather_forecast = WeatherForecastModel(date=date, temperature=temperature, humidity=humidity,
                                            is_day=is_day, rain=rain, weather_code=weather_code,
                                            wind_speed=wind_speed, wind_direction=wind_direction,
                                            dailyForecast=daily_forecast, hourlyForecast=hourly_forecast)

    return weather_forecast



print(DownloadDataService(41.3851, 2.1734).hourlyForecast)