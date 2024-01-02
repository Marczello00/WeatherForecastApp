from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon, getIconNight
from helpers.WIndDirectionTranslator import getWindDirection

class CurrentWeatherItem(ttk.Frame):
    def __init__(self, parent, date, temperature, humidity, is_day, rain, weather_code, wind_speed, wind_direction):
        super().__init__(parent, width=260, height=290, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        date= date.split("T")
        date[0]=date[0].split("-")
        main_text= "Today is " + date[0][2]+"."+date[0][1]+"."+date[0][0] + "\n" + "Time is " + date[1]
        label_text = str(temperature) + "°C" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Rain: " + str(rain) + "mm" + "\n" + "Wind speed: " + str(wind_speed) + "km/h" + "\n" + "Wind direction: " + getWindDirection(wind_direction)
        if is_day:
            image= getIcon(weather_code)
        else:
            image= getIconNight(weather_code)
        image = image.resize((150, 150))
        self.img = ImageTk.PhotoImage(image)
        ttk.Label(self, text=main_text, font=("Arial", 25)).grid(row=0, column=0, sticky="n")
        ttk.Label(self, text=label_text, font=("Arial", 20)).grid(row=0, column=1, sticky="n")
        ttk.Label(self, image=self.img).grid(row=0, column=2, sticky="n")
        















        # date = date.split("-")
        # date = date[2] + "." + date[1]

        # label_text = str(temperature_min) + "°C" + " - " + str(temperature_max) + "°C"

        # image= getIcon(weather_code)
        # image = image.resize((150, 150))
        # self.img = ImageTk.PhotoImage(image)

        # ttk.Label(self, image=self.img).grid(sticky="n")
        # ttk.Label(self, text=label_text).grid(sticky="n")
        # ttk.Label(self, text=date).grid(sticky="n")