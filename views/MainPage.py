from tkinter import ttk
from views.DailyForecastItem import DailyForecastItem
from views.HourlyForecastItem import HourlyForecastItem
from views.CurrentWeatherItem import CurrentWeatherItem


class MainPage:
    def __init__(self, root):
        root.title("Weather forecast application")
        root.geometry('1000x800')
        root.config(bg="skyblue")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)



        s = ttk.Style()
        s.configure('TFrame')
        s.configure('Frame1.TFrame', background='lightblue')

        navbar = ttk.Frame(root, height=100, style='Frame1.TFrame')
        navbar.grid(row=0, column=0, padx=5, pady=(10,5), sticky="nsew")




        current_weather = ttk.Frame(root, height=200 ,style='Frame1.TFrame')
        current_weather.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        current_weather.columnconfigure(0, weight=1)
        current_weather.rowconfigure(0, weight=0)
        current_weather.rowconfigure(1, weight=1)
        ttk.Label(current_weather, text="Current weather", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        current_weather_item = CurrentWeatherItem(current_weather, "2023-12-29T00:00", 15, 0, 0, 0, 0, 0, 0)
        current_weather_item.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")


        hourly_weather_count=12
        hourly_weather = ttk.Frame(root ,style='Frame1.TFrame')
        hourly_weather.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        for i in range(hourly_weather_count):
            hourly_weather.columnconfigure(i, weight=1)
        hourly_weather.rowconfigure(0, weight=1)
        hourly_weather.rowconfigure(1, weight=0)
        ttk.Label(hourly_weather, text="Hours", font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        hour=[]
        for i in range(hourly_weather_count):
            hour.append(HourlyForecastItem(hourly_weather, "2023-12-29T00:00", 15, 0))
            hour[i].grid(column=i, row=1, padx=5, pady=5, sticky="nsew")
 

        daily_weather = ttk.Frame(root,  style='Frame1.TFrame')
        daily_weather.grid(row=3, column=0, padx=5, pady=(5,10), sticky="nsew")
        daily_weather.columnconfigure(0, weight=1)
        daily_weather.columnconfigure(1, weight=1)
        daily_weather.columnconfigure(2, weight=1)
        daily_weather.rowconfigure(0, weight=1)
        daily_weather.rowconfigure(1, weight=1)

        ttk.Label(daily_weather, text="Daily forecast", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        day1 = DailyForecastItem(daily_weather, "2023-12-27",0, 15,17)
        day1.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        day2 = DailyForecastItem(daily_weather, "2023-12-28", 56, -5, -3)
        day2.grid(column=1, row=1, pady=5, sticky="nsew")

        day3 = DailyForecastItem(daily_weather, "2023-12-29", 78, 20, 25)
        day3.grid(column=2, row=1, padx=5, pady=5, sticky="nsew")
    