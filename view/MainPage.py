from tkinter import ttk
from PIL import Image, ImageTk
from PIL import Image, ImageTk


def get_icon(weather_code):
    if weather_code == 0:               #Clear sky
        return "sunny.png"
    elif weather_code in [1,2,3]:       #Mainly clear, partly cloudy, and overcast
        return "cloudy.png"
    elif weather_code in [45,48]:       #Fog and depositing rime fog
        return "foggy.png"
    elif weather_code in [51,53,55]:    #Drizzle: Light, moderate, and dense intensity
        return "drizzle.png"
    elif weather_code in [56,57]:       #Freezing Drizzle: Light and dense intensity
        return "drizzle.png"
    elif weather_code in [61,63,65]:    #Rain: Slight, moderate and heavy intensity
        return "rain.png"
    elif weather_code in [66,67]:       #Freezing Rain: Light and heavy intensity
        return "freezing-rain.png"
    elif weather_code in [71,73,75]:    #Snow fall: Slight, moderate, and heavy intensity
        return "snowfall.png"
    elif weather_code in [78]:          #Snow grains
        return "snowfall.png"
    elif weather_code in [80,81,82]:    #Rain showers: Slight, moderate, and violent
        return "showers.png"
    elif weather_code in [85,86]:       #Snow showers slight and heavy
        return "snowfall.png"
    elif weather_code in [95]:          #Thunderstorm: Slight or moderate
        return "thunderstorm.png"
    elif weather_code in [96,99]:       #Thunderstorm with slight and heavy hail
        return "thunderstorm.png"
    else:
        return "sunny.png"

class DailyForecastItem(ttk.Frame):
    def __init__(self, parent, date, weather_code, temperature):
        super().__init__(parent, width=260, height=290, style='Frame1.TFrame')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        date = date.split("-")
        date = date[2] + "." + date[1]

        label_text = str(temperature) + "°C"

        image_path = "./resources/" + get_icon(weather_code)
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize the image to fit the frame
        self.img = ImageTk.PhotoImage(image)

        ttk.Label(self, image=self.img).grid(sticky="n")
        ttk.Label(self, text=label_text).grid(sticky="n")
        ttk.Label(self, text=date).grid(sticky="n")


class MainPage:
    def __init__(self, root):
        root.title("Weather forecast application")
        root.geometry('800x600')
        root.config(bg="skyblue")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        s = ttk.Style()
        s.configure('TFrame')
        s.configure('Frame1.TFrame')

        upper_frame = ttk.Frame(root, width=790, height=290)
        upper_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        upper_frame.columnconfigure(0, weight=1)
        upper_frame.rowconfigure(0, weight=1)

        lower_frame = ttk.Frame(root, width=790, height=290)
        lower_frame.grid(row=1, column=0, padx=5, pady=(0,5), sticky="nsew")
        lower_frame.columnconfigure(0, weight=1)
        lower_frame.columnconfigure(1, weight=1)
        lower_frame.columnconfigure(2, weight=1)
        lower_frame.rowconfigure(0, weight=1)

        day1 = DailyForecastItem(lower_frame, "2023-12-27",0, 15)
        day1.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        day2 = DailyForecastItem(lower_frame, "2023-12-28", 56, -5)
        day2.grid(column=1, row=0, pady=5, sticky="nsew")

        day3 = DailyForecastItem(lower_frame, "2023-12-29", 78, 20)
        day3.grid(column=2, row=0, padx=5, pady=5, sticky="nsew")
        
