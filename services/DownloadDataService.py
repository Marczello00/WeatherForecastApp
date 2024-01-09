import requests
from services.AnalyzeReplyService import *

def DownloadDataService(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,relative_humidity_2m,is_day,rain,weather_code,wind_speed_10m,wind_direction_10m&hourly=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,wind_speed_10m_max,wind_direction_10m_dominant&timezone=auto&forecast_days=3"

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

