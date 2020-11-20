# Target display: 1024x600 touchscreen, raspberry pi 3

from tkinter import *

# function to find weather details
# of any city using openweathermap api
def tell_weather():

    # import required modules
    import requests
    import json

    # units
    units = "metric"

    # enter your api key here
    api_key = "6c8127bffa2c42cf54f288b29f19d144"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # take a city name from city_field entry box
    # city_name = city_field.get()
    city_name = "Montreal"

    # complete_url variable to store complete url address
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=" + units

    # get method of requests module return response object
    response = requests.get(complete_url)

    # json method of response object convert json format data into python format data
    res = response.json()
    print(res)

    # return code 401 api key error
    if res["cod"] == 401:
        # message dialog box appear which shows given Error meassgae
        messagebox.showerror("Error", "API Key Invalid \n"
                             "Please activate or verify OpenWeather API key")

    # return code 404 city not found
    elif res["cod"] == 404:
        # message dialog box appear which shows given Error meassgae
        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name")

        # clear the content of city_field entry box
        city_field.delete(0, END)

    else:
        # store the value of "main" key in variable y
        y = res["main"]

        # store the value corresponding to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding to the "feelslike" key of y
        current_feelslike = y["feels_like"]

        # store the value corresponding to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather" key in variable z
        z = res["weather"]

        # store the value corresponding to the "description" key
        # at the 0th index of z
        weather_description = z[0]["description"]

        # insert method inserting the
        # value in the text entry box.
        temp_field.insert(15, str(current_temperature) + " Celcius")
        feelslike_field.insert(10, str(current_feelslike) + " Celcius")
        humid_field.insert(15, str(current_humidiy) + " %")
        desc_field.insert(10, str(weather_description))


# Function for clearing the contents of all text entry boxes
def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    feelslike_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)

    # set focus on the city_field entry box
    city_field.focus_set()


# Driver code
if __name__ == "__main__":

    # Create a GUI window
    root = Tk()

    # set the name of tkinter GUI window
    root.title("Gui Application")

    # Set the background colour of GUI window
    root.configure(background="light green")

    # Set the configuration of GUI window
    root.geometry("425x175")

    # Create a Weather Gui Application label
    headlabel = Label(root, text="Weather Gui Application",
                      fg='black', bg='red')

    # Create a City name : label
    label1 = Label(root, text="City name : ",
                   fg='black', bg='dark green')

    # Create a City name : label
    label2 = Label(root, text="Temperature :",
                   fg='black', bg='dark green')

    # Create a atm pressure : label
    label3 = Label(root, text="atm pressure :",
                   fg='black', bg='dark green')

    # Create a humidity : label
    label4 = Label(root, text="humidity :",
                   fg='black', bg='dark green')

    # Create a description :label
    label5 = Label(root, text="description  :",
                   fg='black', bg='dark green')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=3, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    label4.grid(row=5, column=0, sticky="E")
    label5.grid(row=6, column=0, sticky="E")

    # Create a text entry box
    # for filling or typing the information.
    city_field = Entry(root)
    temp_field = Entry(root)
    feelslike_field = Entry(root)
    humid_field = Entry(root)
    desc_field = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    # ipadx keyword argument set width of entry space .
    city_field.grid(row=1, column=1, ipadx="100")
    temp_field.grid(row=3, column=1, ipadx="100")
    feelslike_field.grid(row=4, column=1, ipadx="100")
    humid_field.grid(row=5, column=1, ipadx="100")
    desc_field.grid(row=6, column=1, ipadx="100")

    # Create a Submit Button and attached
    # to tell_weather function
    button1 = Button(root, text="Submit", bg="red",
                     fg="black", command=tell_weather)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root, text="Clear", bg="red",
                     fg="black", command=clear_all)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    button1.grid(row=2, column=1)
    button2.grid(row=7, column=1)

    # Start the GUI
    root.mainloop()
