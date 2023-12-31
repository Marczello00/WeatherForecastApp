from tkinter import ttk
from PIL import ImageTk
from helpers.IconProvider import getIcon

class HourlyForecastItem(ttk.Frame):
    def __init__(self, parent, time, temperature, weather_code):
        super().__init__(parent, width=260, height=290, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)



        image= getIcon(weather_code)
        image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(image)
        label_text = str(temperature) + "°C"


        ttk.Label(self, image=self.img).grid(column=0, row=0,sticky="n")
        ttk.Label(self, text=label_text).grid(column=0, row=1,sticky="n")
        ttk.Label(self, text=time[11:16]).grid(column=0, row=2, padx=5, pady=5, sticky="n")