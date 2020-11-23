# Target display: 1024x600 touchscreen, raspberry pi 3
# Target resolution: mode 640x480
import os, time
import tkinter as tk

class CurrentWeatherGUI():
    def __init__(self):
        root = tk.Tk()
        root.title("Current Weather Forecast")
        root.geometry("640x480")

        # background
        now = time.localtime()
        now_hr = now[3] # https://docs.python.org/3/library/time.html#time.struct_time
        base_path = os.path.dirname(__file__)
        # TODO: / for linux and \ for windows
        bg_file = 'assets\\scaled\\bg_night.png' if now_hr < 7 or now_hr > 19 else 'assets\\scaled\\bg_day.png'
        bg_path = os.path.join(base_path, bg_file)
        bg = tk.PhotoImage(file=bg_path)
        bg_label = tk.Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Gray 25% transparent
        gray_path = os.path.join(base_path, 'assets\\scaled\\transpBlack25.png')
        gray = tk.PhotoImage(file=gray_path)

        # Weather icons
        sunny_path = os.path.join(base_path, 'assets\\scaled\\sunny.png')
        sunny_icon = tk.PhotoImage(file=sunny_path)

        # Top half weather display
        frm_weather = tk.Frame(master=root, width=640, height=240)
        frm_weather.pack(fill=tk.BOTH, side=tk.TOP, padx=40, pady=(40, 20), expand=True)

            # Weather at a glance left
        frm_current_weather = tk.Frame(master=frm_weather, width=280, height=240)
        frm_current_weather.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

                # Current city
        frm_current_city = tk.Frame(master=frm_current_weather, width=280, height=100, pady=20)
        frm_current_city.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        gray_label = tk.Label(frm_current_city, image=gray)
        gray_label.place(x=0, y=0, relwidth=1, relheight=1)

        lbl_city = tk.Label(master=frm_current_city, text='[City]', justify=tk.CENTER)
        lbl_city.config(font=('Roboto', 40), anchor='center')
        lbl_city['text'] = 'Montreal'
        lbl_city.pack()

                # Current conditions
        frm_current_conditions = tk.Frame(master=frm_current_weather, width=280, height=140, bg='green')
        frm_current_conditions.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

                # Current conditions icon
        frm_current_sun = tk.Frame(master=frm_current_conditions, width=140, height=140)
        frm_current_sun.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        lbl_current_sun = tk.Label(master=frm_current_sun, image=sunny_icon)
        lbl_current_sun.place(x=0, y=0, relwidth=1, relheight=1)

        frm_current_temp = tk.Frame(master=frm_current_conditions, width=140, height=140, pady=40)
        frm_current_temp.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        lbl_current_temp = tk.Label(master=frm_current_temp, text='273°K', justify=tk.CENTER)
        lbl_current_temp.config(font=('Roboto', 40), anchor='center')
        lbl_current_temp['text'] = '21°C'
        lbl_current_temp.pack()
        
        # Weather details right
        frm_current_details = tk.Frame(master=frm_weather, width=320, height=240, bg='blue')
        frm_current_details.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        # Bottom half precipitation display
        frm_precipitation = tk.Frame(master=root, width=640, height=240, bg='gray')
        frm_precipitation.pack(fill=tk.BOTH, side=tk.BOTTOM, padx=40, pady=(20, 40), expand=True)

        root.mainloop()


if __name__ == "__main__":
    window = CurrentWeatherGUI()