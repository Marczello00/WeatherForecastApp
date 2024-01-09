from tkinter import ttk
from views.DailyForecastItem import DailyForecastItem
from views.HourlyForecastItem import HourlyForecastItem
from views.CurrentWeatherItem import CurrentWeatherItem
from models.DailyForecastModel import DailyForecastModel
from models.HourlyForecastModel import HourlyForecastModel
from models.WeatherForecastModel import WeatherForecastModel
from services.DownloadDataService import DownloadDataService


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather forecast application")
        self.root.geometry('1000x800')
        self.root.config(bg="skyblue")


        s = ttk.Style()
        s.configure('TFrame')
        s.configure('Frame1.TFrame')

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)


        #Main navbar
        #TODO - add functionality to buttons
        navbar = ttk.Frame(self.root, height=50, style='Frame1.TFrame')
        navbar.grid(row=0, column=0, padx=5, pady=(10,5), sticky="nsew")
        navbar.columnconfigure(0, weight=0)
        navbar.columnconfigure(1, weight=1)
        navbar.columnconfigure(2, weight=0)
        navbar.rowconfigure(0, weight=1)
        city_entry = ttk.Entry(navbar, width=50)
        city_entry.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        search_button = ttk.Button(navbar, text="Search", width=10, command=lambda: self.SearchButton_clicked())
        search_button.grid(column=1, row=0, padx=5, pady=5, sticky="w")
        autodetect_button = ttk.Button(navbar, text="Autodetect location")
        autodetect_button.grid(column=2, row=0, padx=5, pady=5, sticky="e")


        #Current weather
        self.current_weather = ttk.Frame(self.root, height=200 ,style='Frame1.TFrame')
        self.current_weather.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.current_weather.columnconfigure(0, weight=1)
        self.current_weather.rowconfigure(0, weight=0)
        self.current_weather.rowconfigure(1, weight=1)

        #Hourly forecast
        self.hourly_weather = ttk.Frame(self.root ,style='Frame1.TFrame')
        self.hourly_weather.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.hourly_weather.rowconfigure(0, weight=1)

        #Daily forecast
        self.daily_weather = ttk.Frame(self.root,  style='Frame1.TFrame')
        self.daily_weather.grid(row=3, column=0, padx=5, pady=(5,10), sticky="nsew")
        self.daily_weather.rowconfigure(0, weight=1)

    #TODO
    def ShowLoadingScreen(self):
        print("Loading...")


    def InsertData(self, currentWeather, city_name):
    ## Current weather
        ttk.Label(self.current_weather, text=f"Current weather in {city_name}", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        current_weather_item = CurrentWeatherItem(self.current_weather, currentWeather)
        current_weather_item.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

    ## Hourly forecast
        for i, item in enumerate(currentWeather.hourlyForecast[0:12]):
            self.hourly_weather.columnconfigure(i, weight=1)
            HourlyForecastItem(self.hourly_weather, item).grid(column=i, row=10, padx=5, pady=10, sticky="nsew")

    ## Daily forecast
        for i, item in enumerate(currentWeather.dailyForecast):
            self.daily_weather.columnconfigure(i, weight=1)
            DailyForecastItem(self.daily_weather, item).grid(column=i, row=0, padx=5, pady=15, sticky="nsew")


    def SearchButton_clicked(self):
        #To be obtained from another API

        cities_europe = {
            'Amsterdam': (52.3676, 4.9041),
            'Barcelona': (41.3851, 2.1734),
            'Berlin': (52.5200, 13.4050),
            'London': (51.5099, -0.1180),
            'Madrid': (40.4168, -3.7038),
            'Paris': (48.8566, 2.3522),
            'Rome': (41.9028, 12.4964),
            'Vienna': (48.8566, 16.3522),
            'Zurich': (47.3769, 8.5417)
        }

        city='Paris'
        lat, lon=cities_europe[city]
        data = DownloadDataService(lat, lon)
        self.InsertData(data,city)
