import requests

def DownloadDataService(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,relative_humidity_2m,is_day,rain,weather_code,wind_speed_10m,wind_direction_10m&hourly=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,wind_speed_10m_max,wind_direction_10m_dominant&timezone=Europe%2FLondon&forecast_days=3"

    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            print("Datos descargados exitosamente.")
            return AnalyzeReplyService(respuesta.text)
        else:
            print(f"Error al acceder a la URL. Código de estado: {respuesta.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")
        return None


res = DownloadDataService(20.1, 1)
print(res)

