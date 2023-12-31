from tkinter import ttk
from views.DailyForecastItem import DailyForecastItem
from views.HourlyForecastItem import HourlyForecastItem


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
        for i in range(10):
            upper_frame.columnconfigure(i, weight=1)
        upper_frame.rowconfigure(0, weight=1)
        upper_frame.rowconfigure(1, weight=0)

        hour=[]
        for i in range(10):
            hour.append(HourlyForecastItem(upper_frame, "2023-12-29T00:00", 15, 0))
            hour[i].grid(column=i, row=1, padx=5, pady=5, sticky="w")
 

        lower_frame = ttk.Frame(root, width=790, height=290)
        lower_frame.grid(row=1, column=0, padx=5, pady=(0,5), sticky="nsew")
        lower_frame.columnconfigure(0, weight=1)
        lower_frame.columnconfigure(1, weight=1)
        lower_frame.columnconfigure(2, weight=1)
        lower_frame.rowconfigure(0, weight=1)
        lower_frame.rowconfigure(1, weight=1)

        ttk.Label(lower_frame, text="Daily forecast", font=("Arial", 15)).grid(column=0, row=0, padx=5, pady=5, sticky="w")
        day1 = DailyForecastItem(lower_frame, "2023-12-27",0, 15,17)
        day1.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        day2 = DailyForecastItem(lower_frame, "2023-12-28", 56, -5, -3)
        day2.grid(column=1, row=1, pady=5, sticky="nsew")

        day3 = DailyForecastItem(lower_frame, "2023-12-29", 78, 20, 25)
        day3.grid(column=2, row=1, padx=5, pady=5, sticky="nsew")
    