from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon
from models.DailyForecastModel import DailyForecastModel


class DailyForecastItem(ttk.Frame):
    def __init__(self, parent, daily_forecast: DailyForecastModel):
        super().__init__(parent, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.date = daily_forecast.date.strftime("%A, %d. %B")

        label_text = str(daily_forecast.temperature_min) + "°C" + " / " + str(daily_forecast.temperature_max) + "°C"

        image = getIcon(daily_forecast.weather_code)
        image = image.resize((150, 150))
        self.img = ImageTk.PhotoImage(image)

        ttk.Label(self, image=self.img).grid(sticky="n")
        ttk.Label(self, text=label_text).grid(sticky="n")
        ttk.Label(self, text=self.date).grid(sticky="n")
