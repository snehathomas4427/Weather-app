import requests
from datetime import datetime
from dataclasses import dataclass

api_key = 'ff13222f452ad448227993242c3afbec'

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temp: float
    temp_max: float
    temp_min: float

@dataclass
class HourlyData:
    time: float
    description: str
    temp: int
    icon: str
    temp_max: int
    temp_min: int
    precipitation: int

def get_lat_lon(city_name, state_code, country_code, api_key):

    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}').json()
    #print("resp:" , resp)
    '''if not resp:
        return None, None'''
    lat, lon = resp[0]['lat'], resp[0]['lon']
    return lat,lon


def get_current_weather(lat, lon, api_key):
    if lat == None or lon == None:
        return None
    else:
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial').json()
        #weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json()
        #print(weather_data)
        data = WeatherData(
            main = weather_data['weather'][0]['main'],
            description = weather_data['weather'][0]['description'],
            icon = weather_data['weather'][0]['icon'],
            temp = round(weather_data['main']['temp']),
            temp_max = round(weather_data['main']['temp_max']),
            temp_min = round(weather_data['main']['temp_min'])
        )
        return data

'''def hourly_weather(lat, lon, api_key):
    hour_data = requests.get(f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}").json()
    print(hour_data)'''

def daily_weather(lat, lon, api_key):
    day_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json()
    #api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=ff13222f452ad448227993242c3afbec
    #print(day_data)
    hourly_data = []
    for hour in day_data['list']:
        unx_time = datetime.utcfromtimestamp(hour['dt'])
        data = HourlyData(
            time = unx_time.strftime('%a %d %H:%M'),
            description=hour['weather'][0]['description'],
            temp=hour['main']['temp'],
            icon=hour['weather'][0]['icon'],
            temp_max=hour['main']['temp_max'],
            temp_min = hour['main']['temp_min'],
            precipitation = hour['pop']*100
        )
        hourly_data.append(data)
    hourly_data = hourly_data[::8]
    return hourly_data

def weather_map(api_key):
    map = requests.get(f"https://tile.openweathermap.org/map/precipitation_new/1/1/1.png?appid={api_key}").json()
    print(map)

def main_current_weather(city_name, state_name, country_name):
    location = True
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

def main_daily_weather(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = daily_weather(lat, lon, api_key)
    return weather_data

#print(main_daily_weather('Mission','KS', 'US'))
#print(main_current_weather('Mission','KS', 'US'))
#weather_map(api_key)

'''if __name__ == "__main__":
    lat, lon = get_lat_lon('Mission','KS', 'US', api_key)
    daily_weather(lat, lon, api_key)
    #print(get_current_weather(lat, lon, api_key))
    #hourly_weather(lat, lon, api_key)
    #get_lat_lon('zxdtj','afds', 'sfs', api_key)'''


