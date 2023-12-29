from tkinter import ttk
from PIL import Image, ImageTk


class MainPage:

    def __init__(self, root):
        root.title("Weather forecast application")
        root.geometry('800x600')
        root.config(bg="skyblue")
        s = ttk.Style()
        s.configure('TFrame', background='green')
        s.configure('Frame1.TFrame', background='red')

        upper_frame = ttk.Frame(root, width=790, height=290)
        upper_frame.grid(row=0, column=0, padx=5, pady=5)

        lower_frame = ttk.Frame(root, width=790, height=295)
        lower_frame.grid(row=1, column=0, padx=5, pady=0)

        day1 = ttk.Frame(lower_frame, width=260, height=290, style='Frame1.TFrame')
        day1.grid(column=0, row=0, padx=5, pady=5)

        day2 = ttk.Frame(lower_frame, width=260, height=290, style='Frame1.TFrame')
        day2.grid(column=1, row=0, pady=5)

        day3 = ttk.Frame(lower_frame, width=260, height=290, style='Frame1.TFrame')
        day3.grid(column=2, row=0, padx=5, pady=5)

        self.img = ImageTk.PhotoImage(Image.open("./resources/partly_cloudy.png"))
        ttk.Label(day1, image=self.img).grid()
        ttk.Label(day2, text="Our new application").grid()
        ttk.Label(day3, text="Our new application").grid()

        for child in day1.winfo_children():
            child.grid_configure(padx=5, pady=5)
