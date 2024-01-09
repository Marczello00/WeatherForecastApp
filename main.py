import tkinter
from views.MainPage import MainPage
from services.DownloadDataService import DownloadDataService, getLatLong

if __name__ == '__main__':
    root = tkinter.Tk()
    app = MainPage(root)
    root.mainloop()