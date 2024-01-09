from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon, getIconNight
from helpers.WIndDirectionTranslator import obtainWindDirection


class CurrentWeatherItem(ttk.Frame):
    def __init__(self, parent, entire_forecast):
        super().__init__(parent, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        main_text = "Today is " + entire_forecast.date.strftime(
            "%A\n%d %b %Y") + "\n" + "Time is " + entire_forecast.date.strftime("%H:%M")
        label_text = str(entire_forecast.temperature) + "°C" + "\n" + "Humidity: " + str(
            entire_forecast.humidity) + "%" + "\n" + "Rain: " + str(
            entire_forecast.rain) + "mm" + "\n" + "Wind speed: " + str(
            entire_forecast.wind_speed) + "km/h" + "\n" + "Wind direction: " + obtainWindDirection(
            entire_forecast.wind_direction)
        if entire_forecast.is_day:
            image = getIcon(entire_forecast.weather_code)
        else:
            image = getIconNight(entire_forecast.weather_code)
        image = image.resize((150, 150))
        self.img = ImageTk.PhotoImage(image)
        ttk.Label(self, text=main_text, font=("Arial", 25)).grid(row=0, column=0, sticky="n")
        ttk.Label(self, text=label_text, font=("Arial", 20)).grid(row=0, column=1, sticky="n")
        ttk.Label(self, image=self.img).grid(row=0, column=2, sticky="n")
