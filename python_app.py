import requests
import datetime as dt

api_key = 'ff13222f452ad448227993242c3afbec'
user_input = input("Enter city: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}").json()

print(weather_data)

if weather_data['cod'] == '404': #if there is 404 status error, which means the city is not found, then print
    print('no city found')
else:

    def kelvin_to_celsius_fah(kelvin):
        celsius =(kelvin-273.15) 
        fahrenheit = (celsius * (9/5)+32)
        return round(celsius), round(fahrenheit)

    temp_kelvin = weather_data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fah(temp_kelvin)

    feels_like_kelvin = weather_data['main']['feels_like']
    feel_celsius, feel_fahrenheit = kelvin_to_celsius_fah(feels_like_kelvin)

    temp_max = weather_data['main']['temp_max']
    celsius_max, farenheit_max = kelvin_to_celsius_fah(temp_max)

    temp_min = weather_data['main']['temp_min']
    celsius_min, farenheit_min = kelvin_to_celsius_fah(temp_min)

    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    sunrise = dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise'] + weather_data['timezone'])
    sunset = dt.datetime.utcfromtimestamp(weather_data['sys']['sunset']+ weather_data['timezone'])

    print(f"current: {sunrise}")
