from tkinter import *
from tkinter import ttk


class FirstPage:

    def __init__(self, root):
        root.title("Weather forecast application")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Our new application").grid(column=1, row=1, sticky=N)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
