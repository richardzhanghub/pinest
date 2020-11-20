# Target display: 1024x600 touchscreen, raspberry pi 3
# Target resolution: mode 640x480
import os, time
import tkinter as tk

class CurrentWeatherGUI():
    def __init__(self):
        root = tk.Tk()
        root.title("Current Weather Forecast")
        root.geometry("1024x600")

        # background
        now = time.localtime()
        now_hr = now[3] # https://docs.python.org/3/library/time.html#time.struct_time
        base_path = os.path.dirname(__file__)
        bg_path = 'assets\\bg_night.png' if now_hr < 7 or now_hr > 19 else 'assets\\bg_day.png' # TODO: / for linux and \ for windows
        path = os.path.join(base_path, bg_path)
        bg = tk.PhotoImage(file=path)
        bg_label = tk.Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        root.mainloop()


if __name__ == "__main__":
    window = CurrentWeatherGUI()