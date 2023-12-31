from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon

class DailyForecastItem(ttk.Frame):
    def __init__(self, parent, date, weather_code, temperature_min, temperature_max):
        super().__init__(parent, width=260, height=290, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        date = date.split("-")
        date = date[2] + "." + date[1]

        label_text = str(temperature_min) + "°C" + " - " + str(temperature_max) + "°C"

        image= getIcon(weather_code)
        image = image.resize((150, 150))
        self.img = ImageTk.PhotoImage(image)

        ttk.Label(self, image=self.img).grid(sticky="n")
        ttk.Label(self, text=label_text).grid(sticky="n")
        ttk.Label(self, text=date).grid(sticky="n")