from tkinter import ttk
from views.DailyForecastItem import DailyForecastItem
from views.HourlyForecastItem import HourlyForecastItem
from views.CurrentWeatherItem import CurrentWeatherItem
from models.DailyForecastModel import DailyForecastModel
from models.HourlyForecastModel import HourlyForecastModel
from models.WeatherForecastModel import WeatherForecastModel


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather forecast application")
        self.root.geometry('1000x800')
        self.root.config(bg="skyblue")
        s = ttk.Style()
        s.configure('TFrame')
        s.configure('Frame1.TFrame', background='lightblue')

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)


        #Sample data - after API integration, this will be replaced with API data
        self.entire_forecast = WeatherForecastModel("2023-12-29T16:33", "15", "77", "1", "8", "3", "10", "90",
                                                [
                                                    DailyForecastModel("2023-12-19", "lol", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0"),
                                                    DailyForecastModel("2023-12-29", "-23", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0"),
                                                    DailyForecastModel("2023-12-09", "78", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0")],
                                                [
                                                    HourlyForecastModel("2023-12-29T07:00", "10", "0"),
                                                    HourlyForecastModel("2023-12-29T08:00", "12", "1"),
                                                    HourlyForecastModel("2023-12-29T09:00", "15", "2"),
                                                    HourlyForecastModel("2023-12-29T10:00", "12", "55"),
                                                    HourlyForecastModel("2023-12-29T11:00", "0", "78"),
                                                    HourlyForecastModel("2023-12-29T12:00", "-5", "95"),
                                                    HourlyForecastModel("2023-12-29T13:00", "-1", "22"),
                                                    HourlyForecastModel("2023-12-29T14:00", "22", "lol"),
                                                    HourlyForecastModel("2023-12-29T15:00", "34", "-1"),
                                                    HourlyForecastModel("2023-12-29T16:00", "39", "0")]
                                                    )

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
        search_button = ttk.Button(navbar, text="Search", width=10, command=lambda: self.InsertData(self.entire_forecast))
        search_button.grid(column=1, row=0, padx=5, pady=5, sticky="w")
        autodetect_button = ttk.Button(navbar, text="Autodetect location")
        autodetect_button.grid(column=2, row=0, padx=5, pady=5, sticky="e")


    def ShowLoadingScreen(self):
        print("Loading...")


    def InsertData(self, currentWeather):
        ##Current weather
        current_weather = ttk.Frame(self.root, height=200 ,style='Frame1.TFrame')
        current_weather.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        current_weather.columnconfigure(0, weight=1)
        current_weather.rowconfigure(0, weight=0)
        current_weather.rowconfigure(1, weight=1)
        #TODO - change hardcoded city name
        ttk.Label(current_weather, text="Current weather in "+"Porto", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        current_weather_item = CurrentWeatherItem(current_weather, currentWeather)
        current_weather_item.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        ##Hourly forecast
        hourly_weather_count=len(currentWeather.hourlyForecast)
        hourly_weather = ttk.Frame(self.root ,style='Frame1.TFrame')
        hourly_weather.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        for i in range(hourly_weather_count):
            hourly_weather.columnconfigure(i, weight=1)
        hourly_weather.rowconfigure(0, weight=1)
        hourly_weather.rowconfigure(1, weight=1)
        #ttk.Label(hourly_weather, text="Hours", font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        for i, item in enumerate(currentWeather.hourlyForecast):
            HourlyForecastItem(hourly_weather, item).grid(column=i, row=1, padx=5, pady=5, sticky="nsew")
 
        ##Daily forecast
        daily_weather = ttk.Frame(self.root,  style='Frame1.TFrame')
        daily_weather.grid(row=3, column=0, padx=5, pady=(5,10), sticky="nsew")
        daily_weather.columnconfigure(0, weight=1)
        daily_weather.columnconfigure(1, weight=1)
        daily_weather.columnconfigure(2, weight=1)
        daily_weather.rowconfigure(0, weight=1)
        daily_weather.rowconfigure(1, weight=1)
        #ttk.Label(daily_weather, text="Daily forecast", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        for i, item in enumerate(currentWeather.dailyForecast):
            DailyForecastItem(daily_weather, item).grid(column=i, row=1, padx=5, pady=5, sticky="nsew")