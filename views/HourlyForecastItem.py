from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon
from models.HourlyForecastModel import HourlyForecastModel


class HourlyForecastItem(ttk.Frame):
    def __init__(self, parent, hourly_forecast: HourlyForecastModel):
        super().__init__(parent, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        image = getIcon(hourly_forecast.weather_code)
        image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(image)
        temperature_label_text = str(hourly_forecast.temperature) + "°C"
        time_label_text = hourly_forecast.date.strftime("%H:%M")

        ttk.Label(self, image=self.img).grid(column=0, row=0, sticky="n")
        ttk.Label(self, text=temperature_label_text).grid(column=0, row=1, sticky="n")
        ttk.Label(self, text=time_label_text).grid(column=0, row=2, padx=5, pady=5, sticky="n")
